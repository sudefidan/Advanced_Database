import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='sude2fidan',
    password='Sude2fidaN10+$++',
    database='sude2fidan_prj'
)

cursor = conn.cursor()

# 1. Display person's name and their age in years
cursor.execute("""
    SELECT name, YEAR(CURDATE()) - YEAR(dob) AS age
    FROM Person;
""")
for (name, age) in cursor:
    print(f"Name: {name}, Age: {age}")