import mysql.connector

database = mysql.connector.connect(
    host ="127.0.0.1",
    port ="3306",
    user = "root",
    password = "14114",

)

# prepare cursor object
cursorObject = database.cursor()

# create a database 
cursorObject.execute("Show databases")
databases = cursorObject.fetchall() 
for db in databases:
    print(db[0])

print("ALL DONE!")