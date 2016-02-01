#! python3.5
# filling in the gaps - rename file prefix that has gaps

import os, re, shutil

def rename(prefix, dirs):
    dirs = os.path.abspath(dirs)
    filename = [f for f in os.listdir(dirs) if os.path.isfile(os.path.join(dirs, f))]
    filecount = 0
    for f in filename:
        prefixRegex = re.compile(r'(^%s)(\d+)' % prefix)
        result = prefixRegex.search(f)
        if result != None:
            rename = result.group(2)
            lens = len(rename)
            filecount +=1
            if int(rename) != filecount:
                source = os.path.join(dirs, f)
                subname = prefixRegex.sub('%s%s' % (prefix, str(filecount).zfill(lens)), f)
                newname = os.path.join(dirs, subname)
                shutil.move(source, newname)
    print('Renaming files..........')
    print('Done')

search = input('Enter a prefix\n')
folder = input('Enter a folder\n')

rename(search, folder)
