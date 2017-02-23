from urllib.parse import urljoin

from bs4 import BeautifulSoup
# import urllib.parse
import urllib.request
import re

# myJason = json.dumps(md, ensure_ascii=False)
# sys.stdout
# json.loads(myJason)

#### glob module ###
# import glob
# glob.glob('*', recursive=True)

# baseUrl = 'https://www.vfo.se/sv/artiklar/herr/index.html'
def getVfoObjects(url='https://www.vfo.se/sv/artiklar/herr/index.html', *, errors='warn'):
    '''

    :param url:
    :return: A list of objects scraped from vfo
    '''
    # url = 'https://www.vfo.se/sv/artiklar/herr/nyheter-2/index.html'
    # if errors not in {'info', 'warn', 'silent'}:
    #     raise ValueError("errors must be on of the following 'info', 'warn', 'silent'")

    urlPattern = re.compile("^(http|https):\/\/(www\.)?vfo.se")

    if not urlPattern.match(url):
        raise ValueError("Url must start with http(s)://www.vfo.se/")

    try:
        u = urllib.request.urlopen(url)
    # except Exception as err: # Catches all errors (dangerous)
    except urllib.error.URLError as err: # Catches all errors (dangerous)
        print('Could not open: ' + url)
        print("Error message: " + str(err))
        exit(2)

    data = u.read()
    soup = BeautifulSoup(data, 'html.parser')

    vfo_data = soup.find_all(class_='PT_Wrapper')



    for rowNum, vfo in enumerate(vfo_data, start=1):
        print("{}. {} -- {} -- {} -- {} -- {}".format(rowNum, \
                                                  vfo.find(class_='brand').get_text(), \
                                                  vfo.find(class_='PT_Beskr').get_text(), \
                                                  urljoin(url, vfo.find('img').get('data-original')), \
                                                  urljoin(url, vfo.find(class_='PT_Beskr').a.get('href')), \
                                                  vfo.find(class_='PT_Pris').get_text()))

getVfoObjects()
# getVfoObjects('https://www.vfo.se/sv/artiklar/dam/nyheter/ALLA/sida.html')
