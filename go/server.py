from flask import Flask, render_template, request
import sys
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/temp', methods=['POST'])
def temp():
    try:
        c = 0
        place = request.form['Place']
        l = len(place)
        if l == 0:
            return 'Please re-enter proper place name<br/> <br/> <a href="/">Back Home</a>'
        while c == 0:
            #place = str(input('Enter place ? '))
            if place.upper == 'N':
                break
            search = "temperature in " + place
            url = f"http://www.google.com/search?&q={search}"
            r = requests.get(url)
            #print(r.text)
            s = BeautifulSoup(r.text, "html.parser")
            update = s.find("div", class_='BNeawe').text
            # print(update)
            if len(update) < 6:
                # print(len(update))
                print("Current temperature in ", place, " is ", update)
                c = 1
                te = "Current temperature in " + place + " is "+ update
                return 'Current temperature in %s is %s <br/> <br/> <a href="/">Back Home</a>' % (place, update)
            else:
                print("Enter valid search place or 'n' to exit ")
                return 'Enter valid search place <br/> <br/> <a href="/">Back Home</a>'
    except:
        return 'Current temperature in not available, please re-enter proper place name<br/> <br/> <a href="/">Back Home</a>'
        print(sys.exc_info())

@app.route('/distance', methods=['POST'])
def distance():
    try:
        c = 0
        while c == 0:
            place1 = request.form['Starting_Place']
            place2 = request.form['Destination_Place']
            l1 = len(place1)
            l2 = len(place2)
            if l1 ==0 or l2 ==0:
                return 'Please re-enter proper place name<br/> <br/> <a href="/">Back Home</a>'
            # place1 = 'dankuni'
            # place2 = 'bally'
            if place1.upper == 'N':
                break
            search = "distance between " + place1 + " and " + place2
            url = f"http://www.google.com/search?&q={search}"
            r = requests.get(url)
            # print(r.text)
            s = BeautifulSoup(r.text, "html.parser")
            update = s.find("div", class_='BNeawe').text
            # print(update)
            if len(update) > 6:
                # print(len(update))
                print(update)
                return '%s<br/><br/>  <a href="/">Back Home</a>' % (update)
                c = 1
            else:
                print("Enter valid search place or 'n' to exit ")
    except:
        return 'Current distance in not available, please re-enter proper place name<br/> <br/> <a href="/">Back Home</a>'
        print(sys.exc_info())

if __name__ == '__main__':
  app.run(debug=True)