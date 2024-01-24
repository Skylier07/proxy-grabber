import requests
import re
from bs4 import BeautifulSoup

url = "https://free-proxy-list.net/"
page = requests.get(url)
assert page.status_code==200
soup = BeautifulSoup(page.text, 'lxml')

asia_countries_near_taiwan = [
    "China",
    "Japan",
    "Philippines",
    "Vietnam",
    "South Korea",
    "Malaysia",
    "Indonesia",
    "Thailand",
    "Singapore",
    "Myanmar",
    "Cambodia",
    "Brunei",
    "East Timor",
    "Laos",
    "Mongolia",
    "Hong Kong",
    "Macau",
]



info = soup.find_all('td')

def remove_html_tags(text):
    colortags = re.compile(r"&[a-zA-Z]+;")
    text_without_entities = colortags.sub("", text)
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text_without_entities)


def get_proxy(attempts:int=104):
    test = []
    for i in range(0, attempts):
        test.append(remove_html_tags(str(info[i])))

    for i in range(0, attempts, 8):
        if test[i+6] == "yes":
            if test[i+3] in asia_countries_near_taiwan:
                
                return test[i]
            else:
                saved = test[i]
    print("None in Asia found")
    return saved

            
print(get_proxy())

            



#add geo api stuff
#testing