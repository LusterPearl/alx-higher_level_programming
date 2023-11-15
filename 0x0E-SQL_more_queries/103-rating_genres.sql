-- Selecting genres by their rating sum
SELECT name, SUM(rate) AS rating
FROM tv_genres AS d
INNER JOIN tv_show_genres AS e ON e.genre.id = d.id
INNER JOIN tv_show_ratings AS f ON f.show.id = e.show_id
GROUP BY name
ORDER BY rating DESC;
