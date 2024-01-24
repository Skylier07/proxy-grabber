import requests
import re
from bs4 import BeautifulSoup

url = "https://free-proxy-list.net/"
page = requests.get(url)
assert page.status_code==200
soup = BeautifulSoup(page.text, 'lxml')

class CountryNotFoundError(Exception):
    "Country not any continent lists. Please use the full name of the country (Capitalization does not matter)"
    pass

# Asia
asia = ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China", "Cyprus",
        "Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan",
        "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman", "Pakistan",
        "Palestine", "Philippines", "Qatar", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria", "Taiwan",
        "Tajikistan", "Thailand", "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam",
        "Yemen"]

# Africa
africa = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic",
          "Chad", "Comoros", "Democratic Republic of the Congo", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini",
          "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya",
          "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria",
          "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan",
          "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]

# Europe
europe = ["Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus",
          "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland",
          "Italy", "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco",
          "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino",
          "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom", "Vatican City"]

# North America
north_america = ["Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba", "Dominica", "Dominican Republic",
                 "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis",
                 "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United States"]

# South America
south_america = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Peru", "Suriname",
                 "Uruguay", "Venezuela"]

def find_continent(country: str):
    country = country.capitalize()
    if country in asia:
        return asia
    elif country in africa:
        return africa
    elif country in europe:
        return europe
    elif country in north_america:
        return north_america
    elif country in south_america:
        return south_america
    else:
        raise CountryNotFoundError



info = soup.find_all('td')

def remove_html_tags(text):
    colortags = re.compile(r"&[a-zA-Z]+;")
    text_without_entities = colortags.sub("", text)
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text_without_entities)


def get_proxy(country: str=None, attempts:int=10):
    test = []
    attempts*=8    
    for i in range(0, attempts):
        test.append(remove_html_tags(str(info[i])))

    for i in range(0, attempts, 8):
        if test[i+6] == "yes":
            if country is None:
                return test[i]
            if test[i+3] in find_continent(country):
                return test[i]
            else:
                saved = test[i]
    print("No avaliable proxy in your region, retrieving proxy in other continents now...")
    return saved

            
print(get_proxy("taiwan"))

            



#add geo api stuff
#testing