#!/opt/local/bin/python2.6
# coding=utf-8

import os,fileinput

textToSearch='Clear the record'
textToReplace='Clear the field'

def stringContained(filename,somestring):
    if somestring in open(filename).read():
        return True
    return False


for root, dirs, files in os.walk("."):  
    for filename in files:
        complete_path_filename=os.path.join(root, filename)
        if not stringContained(complete_path_filename,textToSearch):
            continue
        print(complete_path_filename)
        #f = fileinput.FileInput(files=(complete_path_filename),inplace=True, backup='.bak')
        #for line in f:
        #   print line.replace(textToSearch,textToReplace).rstrip()
        #f.close()        



