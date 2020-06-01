import csv
import sqlite3, os, uuid, hashlib

def create():
    conn()
    cursor.execute("SELECT count(*) FROM sqlite_master WHERE type = 'table' AND name='SMS_LOG'")
    record = cursor.fetchone()
    #print('record:  ',record)
    if record[0] == 0:
        cursor.execute('''CREATE TABLE SMS_LOG (
                   id text,
                   date text,
                   number text,
                   message text
                    )''')
    print('SMS_LOG TABLE CREATED')

def insertAll():
    conn()
    cursor.execute("SELECT count(*) FROM SMS_LOG")
    count = cursor.fetchone()[0]
    #print(cursor.fetchone())

    cursor.execute("SELECT * FROM SMS_LOG")
    query = cursor.fetchall()

    if count == 0:
        line_count = 0
        path = os.path.abspath(os.path.dirname(__file__)) + "\\sms_log.csv"  # to be read from config file
        with open(path, 'r', encoding="utf-8-sig") as inp:
            reader = csv.DictReader(inp)
            for row in reader:
                if line_count == 0:
                    print(f'Header {", ".join(row)}')
                    line_count += 1
                print(f'{row["date"]} -- {row["number"]} -- {row["message"]}')
                line_count += 1
                cursor.execute("INSERT INTO SMS_LOG VALUES (?,?,?,?)",(str(uuid.uuid4()),str(row["date"]),str(row["number"]),str(row["message"])))
    connection.commit()
    print(line_count-1, ' lines inserted')

def insert(record):
    conn()
    record_insert = record
    line_count = 0

    for i, (num, v) in enumerate(record_insert.items()):
        print("index: {}, key: {}, value: {}".format(i, num, v))
        line_count += 1
        for j, (t, m) in enumerate(v.items()):
            print("index: {}, key: {}, value: {}, value2: {}".format(i, num, t, m))
            cursor.execute("INSERT INTO SMS_LOG VALUES (?,?,?,?)",
                           (str(uuid.uuid4()), str(t), str(num), str(m)))
            connection.commit()
    rtn = str(line_count) + ' records added'
    print(rtn)
    return({"msg":rtn})

def deleteAll():
    conn()
    cursor.execute("DELETE FROM SMS_LOG")
    connection.commit()
    print({"msg":"records deleted"})
    return({"msg":"records deleted"})

def getAll():
    conn()
    cursor.execute("SELECT * FROM SMS_LOG")
    get_All = {}
    get_details = {}
    for row in cursor.fetchall():
        id, date, number, message = row
        print(f'ID : {id}, date : {date}, number : {number}, message : {message}')
        get_details.update({date:message})
        get_All.update({number:get_details})
        get_details = {}
    print(get_All)
    return(get_All)

def get(record):
    conn()
    get_All = {}
    get_details = {}
    record_get = record
    line_count = 0
    d = ''

    for i, (num, val) in enumerate(record_get.items()):
        #print("index: {}, key: {}, value: {}".format(i, num, val))
        cursor.execute("SELECT * FROM SMS_LOG WHERE number in (?)", (val,))
        for row in cursor.fetchall():
            id, date, number, message = row
            print(f'ID : {id}, date : {date}, number : {number}, message : {message}')
            get_details.update({date: message})
            get_All.update({number: get_details})
            get_details = {}
        print(get_All)
    return({"msg":get_All})

def delete(record):
    conn()
    get_All = {}
    get_details = {}
    record_delete = record
    line_count = 0
    d = ''

    for i, (num, val) in enumerate(record_delete.items()):
        #print("index: {}, key: {}, value: {}".format(i, num, val))
        cursor.execute("DELETE FROM SMS_LOG WHERE number in (?)", (val,))
        connection.commit()
        line_count += 1
    rtn = str(line_count) + ' records deleted'
    print(rtn)
    return({"msg":rtn})

def conn():
    global basepath
    basepath = os.path.abspath(os.path.dirname(__file__))
    # print(basepath)
    global connection
    connection = sqlite3.connect(os.path.join(basepath, "sms_log.db")) #how to give custom path
    global cursor
    cursor = connection.cursor()

if __name__== '__main__':
    #basepath = os.path.abspath(os.path.dirname(__file__))
    # print(basepath)
    #connection = sqlite3.connect(os.path.join(basepath, "sms_log.db")) #how to give custom path
    #cursor = connection.cursor()
    #create()
    #d={'1':'381611434323'}
    #get(d)
    insertAll()
    #deleteAll()
    #record = {"1":"381611359456","2":"381611359203"}
    #delete(record)
    #print(delete(record))
    #print(insert(record))