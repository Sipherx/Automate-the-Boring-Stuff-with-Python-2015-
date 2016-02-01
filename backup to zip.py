#! python3.5
# backup to zip.py - copes an entire folder and its contents into
# a zip file whose filename increments.

import zipfile, os

def backuptoZip(folder):
    # backup the entire contents of "folder" into a zip file.

    folder = os.path.abspath(folder)  # make sure folder is absolute
    os.chdir(folder)    # change directory to the current working folder
    # figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # create the zip file
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # add the current folder to the zip file.
        backupZip.write(foldername)
        # add all the files in this folder to the zip file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't backup the backup zip files
            backupZip.write(os.path.join(foldername, filename))
        backupZip.close()
        print('Done')

backuptoZip('c:\\users\kevin\\desktop\\test')
