# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:41:43 2020

@author: abhil
"""

import sqlite3
import sqlite3 as sql
from flask import Flask, render_template, request

from datetime import date, timedelta
import datetime


#conn = sqlite3.connect('database.db')
#print ("Opened database successfully")
#
##conn.execute('CREATE TABLE Corona_Form_Students (ID INTEGER PRIMARY KEY,name TEXT, Travelled TEXT, Travelling_Spring_break TEXT, Expected_return_date TEXT, Symptoms Text)')
##print ("Table created successfully")
#conn.close()

app = Flask(__name__)


@app.route("/")

def index():
    return render_template('index_2.html')

@app.route('/enternew')
def new_student():
   return render_template('Corona_Form.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            ID = request.form['ID']
            name = request.form["name"]
            Travelled = request.form.get("Travelled")
            Travelling_Spring_break = request.form.get('Planning')
            Expected_return_date = request.form.get("Expected_return_date")
            Symptoms = request.form.get('CheckingSymptomns')

            with sql.connect("database.db") as con:
                print ("Opened database successfully")
                cur = con.cursor()
                cur.execute("INSERT INTO Corona_Form_Students (ID,name,Travelled,Travelling_Spring_break,Expected_return_date,Symptoms) VALUES (?,?,?,?,?,?)",(ID,name,Travelled,Travelling_Spring_break,"2020/07/18",Symptoms) )
                con.commit()
                msg = "Record successfully added"
        
        except:
            
            con.rollback()
            msg = "error in insert operation"
         
        finally:
            return render_template("result.html",msg = msg)
            con.close()
@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from Corona_Form_Students")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)  
