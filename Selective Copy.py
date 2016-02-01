#! python3.5
# Selective Copy.py - walks through a folder tree and searches for files with a certain file extension
# then copy these files to a new folder

import os, shutil

# searches the folders with provided extension and directory.
def extsearch(ext, dirs, loc):
    dirs = os.path.abspath(dirs) # make sure folder is absolute
    loc = os.path.abspath(loc)  # make sure folder is absolute
    if not os.path.exists(loc):
        os.makedirs(loc)        # if folder doesn't exist, make one
    
    for folder, subfolders, filenames in os.walk(dirs):
        for filename in filenames:
            if filename.endswith(ext):
                print(filename)
                path = os.path.join(folder, filename)
                if path == os.path.join(loc, filename):
                    continue
                shutil.copy(path, loc)
               
    print('Moving these files to %s.....' % loc)            
    print('done')
    
directory = input('Please enter the directory you want to search\n')

extension = input('Please enter the file you want to search\n')

newfolder = input('Please enter the new folder you want to copy\n')

extsearch(extension, directory, newfolder)
            
