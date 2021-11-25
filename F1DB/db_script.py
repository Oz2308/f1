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

## CREATE DB & TABLE ##
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
mycursor.execute("CREATE TABLE IF NOT EXISTS constructors (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(50) NOT NULL, PRIMARY KEY (id))")

# ## TESTING VARS ##
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

query = "INSERT INTO constructors (name) VALUES (%s)"
mycursor.executemany(query,)
mydb.commit()

## SHOW ALL ROWS IN TABLE ##
mycursor.execute("SELECT * FROM constructors")
myresult = mycursor.fetchall()
 
for x in myresult:
    print(x)


## DELETE TABLE ##

# dely = "DROP TABLE constructors"
# mycursor.execute(dely)
