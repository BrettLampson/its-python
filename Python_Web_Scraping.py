

# ------------------------------------------------------------------------------------------------ #
# WEB SCRAPING


print('\n# ' + '-'*80 + ' #')
# ------------------------------------------------------------------------------------------------ #
# URLLIB library

from urllib.request import urlopen
html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())

# urlopen is used to open a remote object across a network and read it.
# It can read: HTML files, image files, other files.


print('\n# ' + '-'*80 + ' #')
# ------------------------------------------------------------------------------------------------ #
# BEAUTIFUL SOUP v4.0

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html, 'html.parser')
print(bs)
print('Getting Specific Tags')
print(bs.title)
print(bs.h1)

# Note this returns only the first instance of h1 tag found on the page.
# bs4 doesnt need .read() after the html either


print('\n# ' + '-'*80 + ' #')
# ------------------------------------------------------------------------------------------------ #
# POPULAR PARSERS
# html.parser  (bs = BeautifulSoup(html, 'html.parser')
# lxml         (bs = BeautifulSoup(html, 'lxml')
# html5lib     (bs = BeautifulSoup(html, 'html5lib')