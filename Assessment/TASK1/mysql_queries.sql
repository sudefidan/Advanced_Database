USE sude2fidan_prj;

CREATE UNIQUE INDEX person_id_index ON Person (person_id);
CREATE UNIQUE INDEX address_id_index ON Address (address_id);
CREATE UNIQUE INDEX favourite_id_index ON Favourite (favourite_id);
CREATE UNIQUE INDEX person_address_index ON PersonAddress (person_id, address_id);
CREATE UNIQUE INDEX neighbours_pair_index ON NeighboursPair (neighbour1_name, neighbour2_name, address_id);



DROP INDEX person_id_index ON Person;
DROP INDEX address_id_index ON Address;
DROP INDEX favourite_id_index ON Favourite;


-- Display person's name and their age in years:
SELECT name,
       TIMESTAMPDIFF(YEAR, dob, CURDATE()) AS age
FROM Person;

-- Group Persons by their favourite drink and return average age of each group
SELECT f.value AS favourite_drink,
       ROUND(AVG(TIMESTAMPDIFF(YEAR, p.dob, CURDATE())), 2) AS average_age
FROM Person p
JOIN Favourite f ON p.person_id = f.person_id
WHERE f.type = 'Drink'
GROUP BY f.value;

-- Display average age of people who likes Hiking
SELECT f.value as activity, ROUND(AVG(TIMESTAMPDIFF(YEAR, dob, CURDATE())), 2) AS average_age
FROM Person p
JOIN Favourite f ON p.person_id = f.person_id
WHERE f.type = 'Activity' AND f.value = 'Hiking';

-- Display the total number of people from each City and sort it in ascending order by total number of people
SELECT a.city, COUNT(pa.person_id) AS total_number_of_people
FROM Address a
JOIN PersonAddress pa ON a.address_id = pa.address_id
GROUP BY a.city
ORDER BY total_number_of_people ASC;

-- Display name of person(s) whose neighbour is neighbour C
SELECT p.name AS person_name, np.neighbour1_name AS neighbour_name
FROM Person p
JOIN PersonAddress pa ON p.person_id = pa.person_id
JOIN NeighboursPair np ON pa.address_id = np.address_id
WHERE np.neighbour1_name = 'Neighbour C' OR np.neighbour2_name = 'Neighbour C';

