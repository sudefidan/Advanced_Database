import pandas as pd
import mysql.connector

# Load the Excel file
df = pd.read_excel('1NF.xlsx')

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

# Create the table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS 1NF (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        dob DATE NOT NULL,
        street VARCHAR(255) NOT NULL,
        city VARCHAR(255) NOT NULL,
        country VARCHAR(255) NOT NULL,
        zipcode VARCHAR(20) NOT NULL,
        favourite_book VARCHAR(255) NOT NULL,
        favourite_drink VARCHAR(255) NOT NULL,
        favourite_activity VARCHAR(255) NOT NULL,
        neighbour_name VARCHAR(255) NOT NULL,
        neighbour_email VARCHAR(255) NOT NULL
    )
""")

# Insert data into the database
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO 1NF (name, email, dob, street, city, country, zipcode, favourite_book, favourite_drink, favourite_activity, neighbour_name, neighbour_email)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['name'], row['email'], row['dob'], row['street'], row['city'], row['country'], row['zipcode'],
        row['favorite_book'], row['favorite_drink'], row['favorite_activity'], row['neighbour_name'], row['neighbour_email']
    ))

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()