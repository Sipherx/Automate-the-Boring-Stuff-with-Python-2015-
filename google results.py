#! python3.5
# lucky.py - opens several google search results

import requests, sys, webbrowser, bs4

print('Googling...')
res  = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
