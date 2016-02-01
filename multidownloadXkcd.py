#! python3.5
# downloadXkcd.py - downloads every single XKCD comic.

import requests, os, bs4, threading, datetime
os.makedirs('xkcd1', exist_ok=True)      # store comics in ./xkcd

startTime = datetime.datetime.now()

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # downoad the page
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' %(urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            try:
                comicUrl = comicElem[0].get('src')
                trueUrl = 'http:' + comicUrl
                # download the image.
                print('Downloading image %s' % (trueUrl))
                res = requests.get(trueUrl)
                res.raise_for_status()

                # save the image
                imageFile = open(os.path.join('xkcd1', os.path.basename(trueUrl)), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
            except requests.exceptions.MissingSchema:
                print('%s didn\'t download sucessfully' % (trueUrl))
                pass

# create and start the Thread objects.
downloadThreads = []            # a list of all the Thread objects
for i in range(0, 1400, 100):   # loops 14 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()

endtime = datetime.datetime.now()
downloadtime = endtime - startTime
print('Downloads completed in: %s' % (str(downloadtime)))
print('Downloads have been completed.')
