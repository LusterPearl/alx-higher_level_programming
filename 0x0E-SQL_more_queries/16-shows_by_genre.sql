-- Selecting show title and genre name and displaying the result
SELECT a.title, b.name
FROM tv_shows AS a
LEFT JOIN tv_show_genres AS d ON a.id = d.show_id
LEFT JOIN tv_genres AS b ON d.genre_id = b.id
ORDER BY a.title, b.name;
