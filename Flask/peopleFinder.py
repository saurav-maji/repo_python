import requests, sys
from flask import Flask, jsonify, request, json

hd = {'Authorization':'Basic ZHVtbXlVc2VyOnBhc3M='}
rt = input('Enter signum: ')
ul = 'https://gp-lb.internal.ericsson.com/people-finder/people-finder/people/search/' + rt
#print(headers)
try:
    r = requests.get(url=ul, headers=hd)
    cod = str(r.raise_for_status)
    print(cod[cod.index('<Response')+1:58])
    j = json.loads(r.text)
    print(json.dumps(j, indent=4))
except requests.exceptions.HTTPError as errh:
    print("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print("OOps: Something Else",err)
'''except:
    #print(sys.exc_info())
    str1=sys.exc_info()
    #print(str1[1])
    a= str(str1[1])
    print(a[a.index(':')+2:69], ' to ',a[a.index('(')+1:47])
    print(a[a.index('No'):314])'''