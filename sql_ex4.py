import psycopg2

#establishing the connection
cnx = psycopg2.connect(
   database="sql_cwiczenie", 
   user='postgres', 
   password='postgres', 
   host='127.0.0.1', 
   port= '5432'
)

#Setting auto commit false
cnx.autocommit = True

#Creating a cursor object using the cursor() method ---> kursor jest obiektem służącym do bezpośredniej komunikacji z bazą
cursor = cnx.cursor()

#Retrieving data
cursor.execute('''SELECT * from EMPLOYEE''')

#Fetching 1st row from the table ---> udostępnia kolejny jeden wiersz tabeli wynikowej
result = cursor.fetchone();
print(result)

#Fetching all records from the table ---> udostępnia zawartość całej tabeli wynikowe
result = cursor.fetchall();
print(result)

#Commit your changes in the database ---> ostatecznie zatwierdza zmiany stanu bazy spowodowane żądaniami wysłanymi przy użyciu kursorów należących do obiektu połączenie
cnx.commit()

#Closing the connection
cnx.close()
