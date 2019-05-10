from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.kemetnu.com/')
soup = BeautifulSoup(html.read(),'html.parser')

divs = soup.find_all('div', {'class':'xr_txt Normal_te'})
for div in divs:
    print(div)