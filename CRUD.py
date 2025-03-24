import mysql.connector
import mysql
from sqlalchemy import create_engine
import pandas as pd
import pymysql


#connect to database server
try:
    conn = mysql.connector.connect(
        host ='localhost',user='root',password='jarvis',database='flight')
    mycursor = conn.cursor()
    print('connection established')
except:
    print('connection error')

# Database created
#mycursor.execute("CREATE DATABASE flight")
#conn.commit()

#create table
# airport- airport-id- code - name-city
# mycursor.execute("""
# CREATE TABLE airport(
#         airport_id INT PRIMARY KEY,
#         code VARCHAR(10) NOT NULL,
#         city VARCHAR(50) NOT NULL,
#         name VARCHAR(255) NOT NULL
#
# )
# """)
# conn.commit()

# Insert data into table
# mycursor.execute("""
# INSERT INTO airport VALUES
# (1,'DEL','New Delhi','IGIA'),
# (2,'CCU','kolkata','NSCA'),
# (3,'BOM','Mumbai','CSMA')
# """)
# conn.commit()

# search/retrieve operation
# mycursor.execute("""
# SELECT * FROM airport
# WHERE airport_id > 1
# """)
# data = mycursor.fetchall()
# print(data)

# Update city name from mumbai to bombay
# mycursor.execute("""
#     UPDATE airport
#     SET city = 'Bombay'
#     WHERE airport_id = 3
# """)
# conn.commit()

# search/retrieve operation
# mycursor.execute("""
# SELECT * FROM airport
# WHERE airport_id > 1
# """)
# data = mycursor.fetchall()
# print(data)

#DELETE from table
#mycursor.execute("DELETE FROM airport WHERE airport_id = 1")
#conn.commit()

# mycursor.execute("SELECT * FROM airport")
# data = mycursor.fetchall()
# print(data)

# exporting data from python to sql
engine = create_engine("mysql+pymysql://root:jarvis@localhost/flight")
df = pd.read_csv('flights.csv')
df.to_sql("flight",con=engine,if_exists='append')