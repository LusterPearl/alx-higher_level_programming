-- Import table dump into hbtn_0c_0 database and display average temperature by city.
-- Display average temperature by city
SELECT city, AVG(temperature) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
