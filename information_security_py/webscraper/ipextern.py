# Looking for IP address

# Author: @andvsilva
# date 2021-11-09

import json
import re
from urllib.request import urlopen
from icecream import ic

url = 'https://ipinfo.io/json'

response = urlopen(url)

data = json.load(response)

ic(data)

ip = data['ip']
org = data['org']
city = data['city']
country = data['country']
region = data['region']

print('Details of the IP address\n')

print(f'IP address {ip}\nRegion: {region}\nCountry: {country}\nCity: {city}\nOrg: {org}')