#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import fnmatch

print('\n\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°  ')
print('                         CSV creator :                           ')  
print('                         -------------                           ')                
print('      -  adding CSV columns,                                            ')
print('      -  files location, bytes size, and transcription.           ')
print('              Vincent FOUCAULT,     Septembre 2017            ')
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\n')

def process():
    directory = raw_input('Paste here the location of your wavs:\n>> ')
    directory = directory.replace('file://','')
    textfile = raw_input('Paste here the location of your transcript text:\n>> ')
    textfile = textfile.replace('file://','')
    sentenceTextFile = open(textfile, 'rb')
    sentences = sentenceTextFile.readlines()
    csv_file = raw_input('Paste here the complete CVS file link:\n>> ')
    csv_file = csv_file.replace('file://','')
    transcriptions = open(csv_file, 'wb')

    wavDir = directory
    wav_prefix = raw_input('Enter the prefix of wav file (ex : if record.223.wav --> enter "record.") :\n>> ')
    wavs = directory+"/"+wav_prefix
    
    print('\n******************************************************************************************')
    print('your wav dir is : '+directory)
    print('wave prefix name is : '+wav_prefix)
    print('transcript is here : '+textfile)
    print('you want to save CSV here : '+csv_file)
    print('******************************************************************************************')
    
    content = len(fnmatch.filter(os.listdir(wavDir), '*.wav'))
    print('\nNumber of wav found : '+str(content)+'\n')
    transcriptions.write('wav_filename,wav_filesize,transcript\n')
    for i in range(content):
        wavPath = wavs+str(i+1)+'.wav'
        wavSize=(os.path.getsize(wavPath))
        transcript=sentences[i]        
        transcriptions.write(wavPath+","+str(wavSize)+','+transcript)
    transcriptions.close()
        
if __name__ == "__main__":
    try:
        process()
        print('--->  CSV passed !')
        print('\n\n --->  Bye !!\n\n')
    except:
        print('An error occured !! Check your links.')
        print('GOOD LUCK !!')

