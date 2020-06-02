import sys
import requests
from bs4 import BeautifulSoup
try:
    c = 0
    while c == 0:
        place = str(input('Enter place ? '))
        if place.upper == 'N':
            print("Thank you")
            break
        search = "postal code " + place
        url = f"http://www.google.com/search?&q={search}"
        r = requests.get(url)
        #print(r.text)
        s = BeautifulSoup(r.text, "html.parser")
        update = s.find("div", class_='BNeawe').text
        #print(update)
        pin = update[:6:]
        #print(pin)
        i = update.find(pin, 7)
        #print(i)
        #print(update[6:i+6:])
        if len(update) > 9:
            print(update[6:i+6:])
            c = 1
        else:
            print("Enter valid search place or 'n' to exit ", end='')
except:
    print("not present")
    print(sys.exc_info())