from urllib.parse import urljoin

from bs4 import BeautifulSoup
# import urllib.parse
import urllib.request

# baseUrl = 'https://www.vfo.se/sv/artiklar/herr/index.html'
baseUrl = 'https://www.vfo.se/sv/artiklar/herr/nyheter-2/index.html'

u = urllib.request.urlopen(baseUrl)
data = u.read()
soup = BeautifulSoup(data, 'html.parser')

vfo_data = soup.find_all(class_='PT_Wrapper')

for vfo in vfo_data:
    print("{} -- {} -- {} -- {}".format(vfo.find(class_='brand').get_text(), \
                                        vfo.find(class_='PT_Beskr').get_text(), \
                                        urljoin(baseUrl, vfo.find(class_='PT_Beskr').a.get('href')), \
                                        vfo.find(class_='PT_Pris').get_text()))