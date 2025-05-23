import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert records and create the table
cursor = connection.cursor()

# Create the STUDENT table with the fields
table_info = """
CREATE TABLE STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT,
    AGE INT
);
"""
cursor.execute(table_info)

# Insert some sample records with Nepali names and relatable data
cursor.execute('''INSERT INTO STUDENT VALUES('Puja','Computer Science','A',88, 21)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Amit','Computer Science','B',74, 23)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Sunita','Business Management','A',79, 22)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Pratik','Business Management','B',81, 24)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Rajesh','Economics','A',68, 25)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Neha','Economics','B',83, 21)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Anil','Computer Science','A',91, 22)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Jyoti','Computer Science','B',87, 23)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Nabin','Business Management','A',75, 24)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Pratima','Business Management','B',89, 20)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Sushil','Economics','A',66, 22)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Rekha','Economics','B',71, 23)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Sarita','Computer Science','A',84, 21)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Hari','Computer Science','B',92, 24)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Maya','Business Management','A',78, 22)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Gopal','Business Management','B',80, 23)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Deepak','Economics','A',73, 21)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Binita','Economics','B',69, 22)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Rohit','Computer Science','A',86, 23)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Sharmila','Computer Science','B',77, 24)''')


# Display all the inserted records
print("The inserted records are:")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

# Commit your changes to the database
connection.commit()

# Close the connection to the database
connection.close()
