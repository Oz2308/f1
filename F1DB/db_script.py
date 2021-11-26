import requests
from bs4 import BeautifulSoup
import mysql.connector

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
mycursor.executemany(teamquery,val)
mydb.commit()

namequery = "INSERT INTO drivers (firstname, surname) VALUES (%s, %s)"
mycursor.executemany(namequery,vals)
mydb.commit()

# SHOW ALL ROWS IN TABLE ##
mycursor.execute("SELECT * FROM drivers")
myresult = mycursor.fetchall()
 
for result in myresult:
    print(result)


## DELETE TABLE ##
# del_table = "DROP TABLE *******table name*******"
# mycursor.execute(del_table)
