import sys
import requests
from bs4 import BeautifulSoup
try:
    c = 0
    while c == 0:
        place = str(input('Enter place ? '))
        if place.upper == 'N':
            break
        search = "temperature in " + place
        url = f"http://www.google.com/search?&q={search}"
        r = requests.get(url)
        #print(r.text)
        s = BeautifulSoup(r.text, "html.parser")
        update = s.find("div", class_='BNeawe').text
        #print(update)
        if len(update) < 6:
            #print(len(update))
            print("Current temperature in ", place, " is ", update)
            c = 1
        else:
            print("Enter valid search place or 'n' to exit ")
except:
    print("not present")
    print(sys.exc_info())