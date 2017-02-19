from urllib.parse import urljoin

from bs4 import BeautifulSoup
# import urllib.parse
import urllib.request

# myJason = json.dumps(md, ensure_ascii=False)
# sys.stdout
# json.loads(myJason)

# baseUrl = 'https://www.vfo.se/sv/artiklar/herr/index.html'
baseUrl = 'https://www.vfo.se/sv/artiklar/herr/nyheter-2/index.html'
try:
    u = urllib.request.urlopen(baseUrl)
# except Exception as err: # Catches all errors (dangerous)
except urllib.error.URLError as err: # Catches all errors (dangerous)
    print('Could not open: ' + baseUrl)
    print("Error message: " + str(err))
    exit(2)

data = u.read()
soup = BeautifulSoup(data, 'html.parser')

vfo_data = soup.find_all(class_='PT_Wrapper')

for vfo in vfo_data:
    print("{} -- {} -- {} -- {} -- {}".format(vfo.find(class_='brand').get_text(), \
                                        vfo.find(class_='PT_Beskr').get_text(), \
                                        urljoin(baseUrl, vfo.find('img').get('data-original')), \
                                        urljoin(baseUrl, vfo.find(class_='PT_Beskr').a.get('href')), \
                                        vfo.find(class_='PT_Pris').get_text()))