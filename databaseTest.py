import mysql.connector

conn=mysql.connector.Connect(host="localhost",username="root",password="8810620696Vi@",database="face_recognition")
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()