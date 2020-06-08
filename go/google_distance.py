import sys
import requests
from bs4 import BeautifulSoup
try:
    c = 0
    while c == 0:
        place1 = str(input('Enter place 1 ? '))
        place2 = str(input('Enter place 2 ? '))
        #place1 = 'dankuni'
        #place2 = 'bally'
        if place1.upper == 'N':
            break
        search = "distance between " + place1 + " and " + place2
        url = f"http://www.google.com/search?&q={search}"
        r = requests.get(url)
        #print(r.text)
        s = BeautifulSoup(r.text, "html.parser")
        update = s.find("div", class_='BNeawe').text
        #print(update)
        if len(update) > 6:
            #print(len(update))
            print(update)
            c = 1
        else:
            print("Enter valid search place or 'n' to exit ")
except:
    print("not present")
    print(sys.exc_info())