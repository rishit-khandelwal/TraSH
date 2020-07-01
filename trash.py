from sys import argv
import os
from trashlib import prompt,trashParse
PWD = '~'
prev = PWD
paths = {
    '~': os.getenv("USERPROFILE"),
    '/c/': "C:",
    '/d/': "D:",
    '/': "C:"
}
try:
    f = argv[1]
except:
    command = ['echo']
    while command[0] != 'exit':
        try:
            os.chdir(paths[PWD])
            prev = PWD
        except KeyError:
            print(PWD,': Path not found')
            PWD = prev
            
        command = input(prompt)
        
        argz = trashParse(command)
        
        command = argz
        
        if command[0] == 'cd':
            PWD = command[1]
        
        if command[0] == 'say':
            for word in command[1:]:
                print(word,end='')
                print(' ',end='')
            print('')