USE sude2fidan_prj;

CREATE TABLE
    IF NOT EXISTS Person (
        person_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        dob DATE NOT NULL
    );

CREATE TABLE
    IF NOT EXISTS Address (
        address_id INT AUTO_INCREMENT PRIMARY KEY,
        street VARCHAR(255) NOT NULL,
        city VARCHAR(255) NOT NULL,
        country VARCHAR(255) NOT NULL,
        zipcode VARCHAR(20) NOT NULL
    );

CREATE TABLE IF NOT EXISTS PersonAddress (
    person_id INTEGER NOT NULL,
    address_id INTEGER NOT NULL,
    FOREIGN KEY (person_id) REFERENCES Person(person_id),
    FOREIGN KEY (address_id) REFERENCES Address(address_id),
    PRIMARY KEY (person_id, address_id)
);

CREATE TABLE
    IF NOT EXISTS NeighboursPair (
        neighbour1_name VARCHAR(255) NOT NULL,
        neighbour1_email VARCHAR(255) NOT NULL,
        neighbour2_name VARCHAR(255) NOT NULL,
        neighbour2_email VARCHAR(255) NOT NULL,
        address_id INTEGER NOT NULL,
        FOREIGN KEY (address_id) REFERENCES Address (address_id),
        PRIMARY KEY (neighbour1_name, neighbour2_name, address_id)
    );

CREATE TABLE
    IF NOT EXISTS Favourite (
        favourite_id INT AUTO_INCREMENT PRIMARY KEY,
        type VARCHAR(255) NOT NULL,
        value VARCHAR(255) NOT NULL,
        person_id INT,
        FOREIGN KEY (person_id) REFERENCES Person (person_id)
    );

