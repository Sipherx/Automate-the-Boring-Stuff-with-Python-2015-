#! python3.5
# downloadXkcd.py - downloads every single XKCD comic.

import requests, os, bs4

url = 'http://xkcd.com'                 # starting url
os.makedirs('xkcd', exist_ok=True)      # store comics in ./xkcd

while not url.endswith('#'):
   
        # download the page.
        print('Downloading page %s...' % url)
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # find the url of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            try:
                comicUrl = comicElem[0].get('src')
                trueUrl = 'http:' + comicUrl
             
                # download the image.
                print('Downloading image %s...' % (trueUrl))
                res = requests.get(trueUrl)
                res.raise_for_status()

                # save the image to ./xkcd.
                imageFile = open(os.path.join('xkcd', os.path.basename(trueUrl)), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
            except requests.exceptions.MissingSchema:
                pass
        # get the prev button's url.
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
        
    
 
print('Done.')
