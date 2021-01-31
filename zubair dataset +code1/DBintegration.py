import mysql.connector
cnx = mysql.connector.connect(user='root',password='',host='localhost',database='pdda')
print ("connection successfull!!!!")
cursor = cnx.cursor()
query = ("insert into pdda(plantname) values(%s)")
values= ("lemon")
cursor.execute(query,values)
nextvaluecode = cursor.lastrowid
print("next value is",nextvaluecode)
cnx.connect()
cursor.close()
cnx.close()
print("database created sucessfully!!!")