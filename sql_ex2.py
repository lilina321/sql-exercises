import psycopg2

#establishing the connection
cnx = psycopg2.connect(
   database="sql_cwiczenie", 
   user='postgres', 
   password='postgres', 
   host='127.0.0.1', 
   port= '5432'
)

#Creating a cursor object using the cursor() method
cursor = cnx.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
sql = '''
CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''

#Creating a table
cursor.execute(sql)
print('Table created...')
cnx.commit()

#Closing the connection
cnx.close()
