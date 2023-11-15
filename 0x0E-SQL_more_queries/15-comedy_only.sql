-- Selecting show titles for Comedy genre and displaying the result
SELECT m.title
FROM tv_shows AS m
INNER JOIN tv_show_genres AS d ON m.id = d.show_id
INNER JOIN tv_genres AS f ON f.id = d.genres.id
WHERE f.name = 'Comedy'
ORDER BY m.title;
