# Web scraping

# Author: @andvsilva
# date 2021-11-08

from bs4 import BeautifulSoup

import requests
site = requests.get("https://www.climatempo.com.br/").content


soup = BeautifulSoup(site, 'html.parser')

#print(soup.prettify())

temperature = soup.find("a", class_="link actTriggerGA")

print(soup.title.string)
print(temperature.string)