-- Selecting genres for the show Dexter and displaying the result
SELECT d.name
FROM tv_genres AS d
INNER JOIN tv_show_genres AS a ON d.id = a.genre_id
INNER JOIN tv_shows AS f ON f.id = a.show_id
WHERE f.title = 'Dexter'
ORDER BY d.name;
