#! python3.5
# Deleting Unneeded Files - print files larger than 100MB

import os

def largefile(dirs):
    dirs = os.path.abspath(dirs) # make sure path is absolute
    
    for folders, subfolders, filenames in os.walk(dirs):
        for filename in filenames:
            path = os.path.join(dirs, filename)
            size = os.path.getsize(path)
            mb = 102400
            if  size > 100 * mb:
                print('A file with %s MB can be found at %s' % (round(size/mb,2), path))
                

enterFolder = input('Enter the folder path\n')

largefile(enterFolder)

            
    
