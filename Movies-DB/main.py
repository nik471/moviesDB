from cgitb import reset
import mysql.connector

mydb=mysql.connector.connect(
                            host="localhost",
                            user="nikhil",
                            password="1234",
                            database="moviesdb"
                            )

mycursor=mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS moviesdb")


s="CREATE TABLE IF NOT EXISTS Movies(name varchar(50),actor varchar(50), actress varchar(50), year int,director varchar(50))"


mycursor.execute(s)


n="INSERT INTO movies(name,actor,actress,year,director) VALUES(%s ,%s ,%s ,%s ,%s)"
b1=('Gabbar','Akshay','Shruti',2015,'Krish')

# mycursor.execute(n,b1)


n="INSERT INTO movies(name,actor,actress,year,director) VALUES(%s ,%s ,%s ,%s ,%s)"
b1=('War','Hrithik Roshan','Vaani Kapoor',2019,'Siddharth Anand')

# mycursor.execute(n,b1)


n="INSERT INTO movies(name,actor,actress,year,director) VALUES(%s ,%s ,%s ,%s ,%s)"
b1=('Parmanu','John Abraham','Anuja Sathe',2018,'Abhishek Sharma')

# mycursor.execute(n,b1)

# mydb.commit()

j="SELECT * from movies"

mycursor.execute(j)

result=mycursor.fetchall()

for i in result:
    print(i)