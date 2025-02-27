import pandas as pd
import mysql.connector
import sys

# Load the Excel file
df = pd.read_excel('Assessment/DataCaseScenario.xlsx')

# Convert the 'DOB' column to the correct date format
df['DOB'] = pd.to_datetime(df['DOB']).dt.strftime('%Y-%m-%d')

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='sude2fidan',
    password='Sude2fidaN10+$++',
    database='sude2fidan_prj'
)

cursor = conn.cursor()

def insert_person(row):
    cursor.execute("""
        INSERT INTO Person (name, email, dob)
        VALUES (%s, %s, %s)
    """, (row['Name'], row['Email'], row['DOB']))
    return cursor.lastrowid

def insert_address(row):
    cursor.execute("""
        INSERT INTO Address (street, city, country, zipcode)
        VALUES (%s, %s, %s, %s)
    """, (row['Street'], row['City'], row['Country'], row['Zip Code']))
    return cursor.lastrowid

def insert_person_address(person_id, address_id):
    cursor.execute("""
        INSERT INTO PersonAddress (person_id, address_id)
        VALUES (%s, %s)
    """, (person_id, address_id))

def insert_favourite(row, person_id):
    cursor.execute("""
        INSERT INTO Favourite (type, value, person_id)
        VALUES ('Book', %s, %s)
    """, (row['Favourite Book'], person_id))
    cursor.execute("""
        INSERT INTO Favourite (type, value, person_id)
        VALUES ('Drink', %s, %s)
    """, (row['Favourite Drink'], person_id))
    cursor.execute("""
        INSERT INTO Favourite (type, value, person_id)
        VALUES ('Activity', %s, %s)
    """, (row['Favourite Activity'], person_id))

def insert_neighbours_pair(row, address_id):
    cursor.execute("""
        INSERT INTO NeighboursPair (neighbour1_name, neighbour1_email, neighbour2_name, neighbour2_email, address_id)
        VALUES (%s, %s, %s, %s, %s)
    """, (row['Neighbour 1 Name'], row['Neighbour 1 Email'], row['Neighbour 2 Name'], row['Neighbour 2 Email'], address_id))

if __name__ == "__main__":
    for index, row in df.iterrows():
        person_id = insert_person(row)
        address_id = insert_address(row)
        insert_person_address(person_id, address_id)
        insert_favourite(row, person_id)
        insert_neighbours_pair(row, address_id)

    # Commit the transaction
    conn.commit()