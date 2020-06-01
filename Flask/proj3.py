import requests, sys
from flask import Flask, jsonify, request, json

rt = input('Enter route: ')
ul = 'http://127.0.0.2:6000/' + rt
dt = {'1':'381611359203'}
try:
    if rt == 'getAll':
        r = requests.get(ul, verify=False)
    else:
        r = requests.post(url = ul, json = dt, timeout=3)
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
