-- Selecting shows by their rating sum
SELECT title, SUM(rate) AS rating_sum
FROM tv_shows AS d
INNER JOIN tv_show_ratings AS f ON d.id = f.show_id
GROUP BY title
ORDER BY rating_sum DESC;
