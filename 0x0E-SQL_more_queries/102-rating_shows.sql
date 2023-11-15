-- Selecting shows by their rating sum
SELECT title, SUM(rate) AS rating
FROM tv_shows AS d
INNER JOIN tv_show_ratings AS f ON d.id = f.show_id
GROUP BY title
ORDER BY rating DESC;
