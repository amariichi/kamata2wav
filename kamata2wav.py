# -*- coding: utf-8 -*-
import os
import sys
import datetime
import struct
import wave

def argumentsparser():
    usage = "Usage: python {} inputfile.kamata_programs".format(__file__)
    arguments = sys.argv
    if len(arguments) == 1 or len(arguments) > 2:
        return usage
    arguments.pop(0)
    if not arguments[0].endswith('.kamata_programs') or arguments[0].startswith('-'):
        return usage

if __name__ == '__main__' :
    if argumentsparser() is None :
        filesize = os.path.getsize(sys.argv[0])
        readpoint = 96
        filenumber = 1
        now = datetime.datetime.now()
        dirname = "{0:%y%m%d%H%M%S}".format(now)
        fin = open(sys.argv[0], mode="rb")
        if readpoint < filesize :
            os.makedirs(dirname, exist_ok=True)

        print("inputfile size =", filesize)

        while readpoint < filesize :
            fin.seek(readpoint)
            filename = "{0:03d}".format(filenumber)
            data = struct.unpack("B", fin.read(1))
            i = 0
            while not data[0] == 0 and i < 12 :
                filename += chr(data[0])
                data = struct.unpack("B", fin.read(1))
                i += 1
            filename += ".wav"
            readpoint += 616
            
            fout = wave.Wave_write(dirname + "/" + filename)
            fout.setparams((
                1,                 # mono
                1,                 # 8 bits = 1 byte
                48000,             # sampling bitrate
                32,                # samples
                "NONE",            # not compressed
                "not compressed"   # not compressed
                ))

            for i in range(32):
                fin.seek(readpoint)
                valuekey = fin.read(4)
                bitvalue = round(struct.unpack('<f', valuekey)[0] * 255)           
                fout.writeframesraw(struct.pack("B", bitvalue))
                print("readpoint =", readpoint, " , ", bitvalue)
                readpoint += 12
            print("-----------------")
            
            fout.close()
            filenumber += 1
            readpoint += 4
            
        fin.close()
        print(filenumber - 1, "wave files are created in the", dirname, "folder successfully.")
        print("The format is monoral, 8-bit, 48kHz and 32 samples. Files are expected to be readable for an ELZ_1 synthesizer.")
    
    else: 
        print(argumentsparser())
        