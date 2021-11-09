# Verification of Phone

# Author: @andvsilva
# date 2021-11-09

import phonenumbers
from phonenumbers import geocoder

phone_number = input("Type the phone number, e.g. 55 11 40028922: ")

phone_number = phonenumbers.parse(phone_number)

print(geocoder.description_for_number(phone_number, 'pt'))