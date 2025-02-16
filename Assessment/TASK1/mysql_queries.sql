-- Display person's name and their age in years:
SELECT name,
       TIMESTAMPDIFF(YEAR, dob, CURDATE()) AS age
FROM Person;

-- Group Persons by their favourite drink and return average age of each group
SELECT f.value AS favorite_drink,
       ROUND(AVG(TIMESTAMPDIFF(YEAR, p.dob, CURDATE())), 2) AS average_age
FROM Person p
JOIN Favorite f ON p.id = f.person_id
WHERE f.type = 'Drink'
GROUP BY f.value;

-- Display average age of people who likes Hiking
SELECT f.value as activity, ROUND(AVG(TIMESTAMPDIFF(YEAR, dob, CURDATE())), 2) AS average_age
FROM Person p
JOIN Favorite f ON p.id = f.person_id
WHERE f.type = 'Activity' AND f.value = 'Hiking';

-- Display the total number of people from each City and sort it in ascending order by total number of people
SELECT a.city, COUNT(p.id) AS total_number_of_people
FROM Person p
JOIN Address a ON p.id = a.person_id
GROUP BY a.city
ORDER BY total_number_of_people ASC;

-- Display name of person(s) whose neighbour is neighbour C
SELECT p.name as person_name, n.name as neighbour_name
FROM Person p
JOIN PersonNeighbour pn ON p.id = pn.person_id
JOIN Neighbour n ON pn.neighbour_id = n.id
WHERE n.name = 'Neighbor C';



