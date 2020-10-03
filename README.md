# kamata2wav

USAGE: python kamata2wav.py inputfile.kamata_programs

KORG gadget 2 に収録されている VSTi kamata の .kamata_programs 形式のユーザーファイルを WAV ファイル形式（8Bit, 48kHz, モノラル, 32 サンプル）に変換するスクリプトです。  
このスクリプトを実行すると、実施した時点の日時で "YYMMDDhhmmss" 形式で新しいフォルダが作られます。そして、フォルダの中には指定したユーザーファイルに収録されている波形に相当する数の wav ファイルが作成されます。  
wav ファイルの名前には、001 からの連番に続けて kamata で使われていた名前の先頭１２文字までが使われます。  

また、この wav ファイルは、SONICWARE社製 ELZ_1（エルザワン）　シンセサイザーの 8BIT WAVMEM SYNTH　波形データとして読み込ませることができると思います。  

このスクリプトは、私自身の python と github の勉強用に作ったものです。
Windows PC 上で python 3.8.3 を使用しました。  

まともに動かなかったりファイルが壊れたりしても当方は一切責任を負いません。リスクを承知の上で使ってください。

This script converts a kamata user file with extension .kamata_programs, which is made by KORG gadget 2 VSTi, into WAV files.  
Their format is 8Bit, 48kHz and monoral and they have 32 samples.
When you run this script, a new folder will be created with the "YYMMDDhhmmss" format as the date and time of execution.  
The script will create wav files inside the folder. Each file corresponds to one of user defined wavetables stored in the kamata user file.  
The wav files are named by sequential numbers from 001 followed by the first 12 characters of the name used in kamata.  

Those wav files are also expected to be able to be loaded as 8-bit WAVMEM SYNTH wavetable data on a SONICWARE ELZ_1 synthesizer.  

I made this script just for studying python and github.  
I used python 3.8.3 on Windows PC.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.   
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  

