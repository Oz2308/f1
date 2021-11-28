from typing import Optional
import requests
from bs4 import BeautifulSoup
import mysql.connector
from datapoints import constructors

## CREATE & CONNECT TO DB ##
mydb = mysql.connector.connect(
    host="127.0.0.1", 
    user="root", 
    password="f1root", 
    database="mydatabase"
)

mycursor = mydb.cursor()

## CREATE DB & TABLES ##
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
mycursor.execute("CREATE TABLE IF NOT EXISTS constructors (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(50) NOT NULL, PRIMARY KEY (id))")
mycursor.execute("CREATE TABLE IF NOT EXISTS drivers (id INT NOT NULL AUTO_INCREMENT, firstname VARCHAR(50) NOT NULL, surname VARCHAR(50) NOT NULL, PRIMARY KEY (id))")

# ## TESTING BLOCK ##
# year = 1986
# Constructors = f"http://ergast.com/api/f1/{year}/drivers"
# Constructors = "http://ergast.com/api/f1/2021/constructors"
# site = requests.get(Constructors)
# siteSRC = site.content

# ## TESTING API DATA PULL ##
# soup = BeautifulSoup(siteSRC, 'html.parser')
# teams = soup.find_all('name')

# ## TESTING BULK ADD CONSTRUCTORS ##
# val = []
# for team in teams:
#      val.append(tuple(team))

## INSERT DATA INTO TABLES ##
teamquery = "INSERT INTO constructors (name) VALUES (%s)"
mycursor.executemany(teamquery,)
mydb.commit()

# namequery = "INSERT INTO drivers (firstname, surname) VALUES (%s, %s)"
# mycursor.executemany(namequery,vals)
# mydb.commit()

## SHOW ALL ROWS IN TABLE ##
def table_results(table: str, limit: Optional[int] = None):
    sql = f"SELECT * FROM {table}"
    sql_with_limit = f"SELECT * FROM {table} LIMIT {limit}"

    mycursor.execute(sql_with_limit if limit else sql)
    myresult = mycursor.fetchall()

    for result in myresult:
        print(result)

# table_results()

#TODO FIND IF CAN CALL FUNC FROM TERMINAL OR CREATE FILE

# def delete_table(table):
#     del_table = f"DROP TABLE {table}"
#     mycursor.execute(del_table)

# delete_table('constructors')
