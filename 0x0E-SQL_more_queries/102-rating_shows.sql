-- Selecting shows by their rating sum
SELECT tv_shows.title, SUM(rating) AS rating_sum
FROM tv_shows
INNER JOIN tv_shows_rate ON tv_shows.id = tv_shows_rate.tv_show_id
GROUP BY tv_shows.id
ORDER BY rating_sum DESC;
