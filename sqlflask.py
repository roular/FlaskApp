import json
import requests
from flask import Flask,request
import psycopg2

# Print PostgreSQL Connection properties
# print ( connection.get_dsn_parameters(),"\n")
# connect to the PostgreSQL database
connection = psycopg2.connect(user = "postgres",
                              password = "",
                              host = "127.0.0.1",
                              port = "5432",
                              database = "<Enter DB name>")
  # create a new cursor
cursor = connection.cursor()

app = Flask(__name__)
@app.route('/students')
def display_users():       
  
  # get the table's elements
  select_query = """SELECT * FROM students"""
  # execute the query
  cursor.execute(select_query)
  # get the generated id back
  names = cursor.fetchall()
  count = cursor.rowcount
  print(names)
  print(count)
  return "hi"

@app.route('/add_student', methods=["POST"])
def insert_student():
  # insert an element to the student table
  name = request.get_json()['name']
  id = request.get_json()['id']
  age = request.get_json()['age']
  print(id)
  print(age)
  print(name)
  insert_query = """INSERT INTO students ("Id", "Age", "Name") VALUES (%s,%s,%s) """
  records_to_insert = (id,age,name)
  cursor.execute(insert_query,records_to_insert)
  connection.commit()
  count = cursor.rowcount
  print(count,"hmmmm")

  # close communication with the database
  #cursor.close()
  return "Student added succesfully"

@app.route('/get_student/<int:post_id>')
def get_student(post_id):
  # insert an element to the student table
  get_query = """SELECT * FROM students WHERE "Id" = %s """
  cursor.execute(get_query,[post_id])
  std = cursor.fetchone()
  print(std,"hmmmm")
  # close communication with the database
  return "Student extracted"

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 