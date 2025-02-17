USE sude2fidan_prj;

CREATE UNIQUE INDEX person_id_index ON Person (id);
CREATE UNIQUE INDEX address_id_index ON Address (id);
CREATE UNIQUE INDEX neighbour_id_index ON Neighbour (id);
CREATE UNIQUE INDEX person_address_id_index ON PersonAddress (id);
CREATE UNIQUE INDEX person_neighbour_id_index ON PersonNeighbour (id);
CREATE UNIQUE INDEX favourite_id_index ON Favourite (id);



-- Display person's name and their age in years:
SELECT name,
       TIMESTAMPDIFF(YEAR, dob, CURDATE()) AS age
FROM Person;

-- Group Persons by their favourite drink and return average age of each group
SELECT f.value AS favourite_drink,
       ROUND(AVG(TIMESTAMPDIFF(YEAR, p.dob, CURDATE())), 2) AS average_age
FROM Person p
JOIN Favourite f ON p.id = f.person_id
WHERE f.type = 'Drink'
GROUP BY f.value;

-- Display average age of people who likes Hiking
SELECT f.value as activity, ROUND(AVG(TIMESTAMPDIFF(YEAR, dob, CURDATE())), 2) AS average_age
FROM Person p
JOIN Favourite f ON p.id = f.person_id
WHERE f.type = 'Activity' AND f.value = 'Hiking';

-- Display the total number of people from each City and sort it in ascending order by total number of people
SELECT a.city, COUNT(pa.person_id) AS total_number_of_people
FROM Address a
JOIN PersonAddress pa ON a.id = pa.address_id
GROUP BY a.city
ORDER BY total_number_of_people ASC;

-- Display name of person(s) whose neighbour is neighbour C
SELECT p.name AS person_name, n.name AS neighbour_name
FROM Person p
JOIN PersonNeighbour pn ON p.id = pn.person_id
JOIN Neighbour n ON pn.neighbour_id = n.id
WHERE n.name = 'Neighbor C';


