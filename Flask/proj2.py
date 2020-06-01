import sys
from flask import Flask, jsonify, request
#from Day2 import D2_2 as mul
import proj1 as table

app = Flask(__name__)

@app.route("/getAll")
def get_All():
    try:
        call_list = table.getAll()
        print('call_list',call_list)
        # print(a)
        print('request.query_string',request.query_string)
        print('request.args',request.args)
        # person_list = mul.multiplication(int(2))
        return jsonify(call_list), 200
        #return jsonify({"msg":"Hello World!"})
    except TypeError:
        print(sys.exc_info())

@app.route("/get", methods=["POST"])
def get():
    try:
        table.get(request.json)
        return jsonify(table.get(request.json)), 200
    except TypeError:
        print(sys.exc_info())
        return jsonify({"msg":"Error"}), 500

@app.route("/delete", methods=["DELETE"])
def delete():
    try:
        table.delete(request.json)
        return jsonify(table.delete(request.json)), 200
    except TypeError:
        print(sys.exc_info())
        return jsonify({"msg":"Error"}), 500

@app.route("/deleteAll")
def delete_All():
    try:
        table.deleteAll()
        return jsonify(table.deleteAll()), 200
    except TypeError:
        print(sys.exc_info())

@app.route("/insert", methods=["POST"])
def insert():
    try:
        table.insert(request.json)
        return jsonify(table.insert(request.json)), 200
    except TypeError:
        print(sys.exc_info())

if __name__=='__main__':
    app.run(host='127.0.0.2', port=6000)
