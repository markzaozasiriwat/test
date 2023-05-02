import random
import sqlite3
import io

def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def create_db():
    with sqlite3.connect("docter.sqlite") as con:
        sql_cmd = """
            create table docter_profile(
              id integer PRIMARY KEY AUTOINCREMENT,
              name text,
              tel text,
              address char(150),
              gender text,
              photo blob
            )
        """
        con.execute(sql_cmd)

def insert():
    with sqlite3.connect("docter.sqlite") as con:
        sql_cmd = """
            insert into docter_profile(name, tel, address, gender, photo) values('mark', '0868515912', '671/11', 'Male', ?);
        """
        con.execute(sql_cmd)
def insert2(params):
    with sqlite3.connect("docter.sqlite") as con:
        sql_cmd = """
            insert into docter_profile(name, tel, address, gender, photo) values(?, ?, ?, ?, ?);
        """
        con.execute(sql_cmd, params)
def update():
    with sqlite3.connect("docter.sqlite") as con:
        sql_cmd = """
            update docter_profile set address = 'kku'
        """
        con.execute(sql_cmd)
def delete():
    with sqlite3.connect("docter.sqlite") as con:
        sql_cmd = """
            delete from docter_profile where gender = 'Male'
        """
        con.execute(sql_cmd)
def select():
    with sqlite3.connect("docter.sqlite") as con:
        sql_cmd = """
            select * from docter_profile
        """
        for row in con.execute(sql_cmd):
            print(row)


if __name__ == '__main__':
    #create_db() #commend in second time
    # insert()
    #insert(('hello', '123456789', '123/456', 'Female', ''))
    # for _ in range(2):
    #     n = input("input name:")
    #     t = input("input tel:")
    #     g = input("input gender:")
    #     a = input("input address:")
    #     p = input("input photo:")
    #     insert((n,t,g,a,p))
    # update()
    delete()
    select()
