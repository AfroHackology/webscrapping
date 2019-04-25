from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(),'html.parser')

# These are syntax for BeautifulSoup

# divs = soup.find('div',{'class': 'featured'})
# print(divs)

# 'get_text' strips away the tags leaving just a block of text.
# This can be done with all the tags

# featured_header = soup.find('div', {'class': 'featured'}).h2
# print(featured_header.get_text())

# using attrs= is a general use function and it looks like this:
# for button in soup.find(attrs={'class': 'button button--primary'}):
    #print(button)

# class_ is a common keyword used to find info
# for button in soup.find(class_='button button--primary'):
#     print(button)

# This is common use case to get hyper links
# for link in soup.find_all('a'):
#     print(link.get('href'))