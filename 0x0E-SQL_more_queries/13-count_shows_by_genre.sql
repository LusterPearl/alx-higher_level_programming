-- Counting shows for each genre and displaying the result
SELECT d.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS d
INNER JOIN tv_show_genres AS f ON d.id = f.genre_id
GROUP BY d.name
ORDER BY number_of_shows DESC;
