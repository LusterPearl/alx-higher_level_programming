-- Display the max temperature of each state ordered by State name.

-- Display max temperature of each state
SELECT state, MAX(temperature) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
