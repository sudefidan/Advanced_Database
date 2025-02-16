import pandas as pd
import mysql.connector

# Load the Excel file
df = pd.read_excel('1NF.xlsx')

# Print the column names to verify
print(df.columns)

# Convert the 'dob' column to the correct date format
df['dob'] = pd.to_datetime(df['dob']).dt.strftime('%Y-%m-%d')

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='sude2fidan',
    password='Sude2fidaN10+$++',
    database='sude2fidan_prj'
)

cursor = conn.cursor()

# Create the tables if they don't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Person (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        dob DATE NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Address (
        id INT AUTO_INCREMENT PRIMARY KEY,
        person_id INT,
        street VARCHAR(255) NOT NULL,
        city VARCHAR(255) NOT NULL,
        country VARCHAR(255) NOT NULL,
        zipcode VARCHAR(20) NOT NULL,
        FOREIGN KEY (person_id) REFERENCES Person(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Favourite (
        id INT AUTO_INCREMENT PRIMARY KEY,
        type VARCHAR(255) NOT NULL,
        value VARCHAR(255) NOT NULL,
        person_id INT,
        FOREIGN KEY (person_id) REFERENCES Person(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Neighbour (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS PersonNeighbour (
        id INT AUTO_INCREMENT PRIMARY KEY,
        person_id INT,
        neighbour_id INT,
        FOREIGN KEY (person_id) REFERENCES Person(id),
        FOREIGN KEY (neighbour_id) REFERENCES Neighbour(id)
    )
""")

# Track added persons to avoid duplicates
added_persons = set()

# Insert data into the tables
for index, row in df.iterrows():
    person_key = (row['zipcode'])
    if person_key not in added_persons:
        cursor.execute("""
            INSERT INTO Person (name, email, dob)
            VALUES (%s, %s, %s)
        """, (row['name'], row['email'], row['dob']))
        person_id = cursor.lastrowid
        added_persons.add(person_key)

        # Insert data into the Address table
        cursor.execute("""
            INSERT INTO Address (person_id, street, city, country, zipcode)
            VALUES (%s, %s, %s, %s, %s)
        """, (person_id, row['street'], row['city'], row['country'], row['zipcode']))

        # Insert data into the Favorite table
        cursor.execute("""
            INSERT INTO Favourite (type, value, person_id)
            VALUES ('Book', %s, %s)
        """, (row['favorite_book'], person_id))
        cursor.execute("""
            INSERT INTO Favourite (type, value, person_id)
            VALUES ('Drink', %s, %s)
        """, (row['favorite_drink'], person_id))
        cursor.execute("""
            INSERT INTO Favourite (type, value, person_id)
            VALUES ('Activity', %s, %s)
        """, (row['favorite_activity'], person_id))

    # Insert data into the Neighbour table
    cursor.execute("""
        INSERT INTO Neighbour (name, email)
        VALUES (%s, %s)
    """, (row['neighbour_name'], row['neighbour_email']))
    neighbour_id = cursor.lastrowid

    # Insert data into the PersonNeighbour table
    cursor.execute("""
        INSERT INTO PersonNeighbour (person_id, neighbour_id)
        VALUES (%s, %s)
    """, (person_id, neighbour_id))

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()