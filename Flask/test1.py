import csv
import sqlite3, os, uuid, hashlib



basepath = os.path.abspath(os.path.dirname(__file__))
#print(basepath)

def getAll():
    connection = sqlite3.connect(os.path.join(basepath,"sms_log.db"))
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM SMS_LOG")
    query = cursor.fetchall()

    for row in query:
        id, date, number, message = row
        print(f'ID : {id}, date : {date}, number : {number}, message : {message}')
    return(query)

if __name__=='__main__':
    getAll()


my_list = ['p','r','o','b','e']

print(my_list[:])

print(my_list[-5])