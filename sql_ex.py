import psycopg2

#establishing the connection
cnx = psycopg2.connect(
   database="postgres", 
   user='postgres', 
   password='postgres', 
   host='127.0.0.1', 
   port= '5432'
)
cnx.autocommit = True

#Creating a cursor object using the cursor() method
cursor = cnx.cursor()

#Preparing query to create a database
sql = '''CREATE database sql_cwiczenie'''

#Creating a database
cursor.execute(sql)
print("Database created successfully........")

#Closing the connection
cnx.close()
