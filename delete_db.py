# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 07:25:10 2020

@author: abhil
"""

import sqlite3

from sqlite3 import Error

def create_connection(database):
    ##Creating Connection to the Databse
    
    conn = None
    
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)
    return conn

def delete_singlerecord_data(conn,table_name,ID):
    
    sqlDeleteQuery= "DELETE from"+ table_name+ "where ID=?"
    cur = conn.cursor()
    cur.execute(sqlDeleteQuery,(ID,))
    conn.commit()
    
def delet_whole_table_data(conn,table_name):
    sqlDeleteQuery= "DELETE from "+ table_name
    cur = conn.cursor()
    cur.execute(sqlDeleteQuery)
    conn.commit()
    

def main():
    database = r"database.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        delet_whole_table_data(conn,"Corona_Form_Students")
        


if __name__ == '__main__':
    main()    
        


