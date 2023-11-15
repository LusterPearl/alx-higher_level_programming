-- Selecting all shows and their respective genre IDs
SELECT a.title, d.genre_id
FROM tv_shows AS a
LEFT JOIN tv_show_genres AS d ON a.id = d.show_id
ORDER BY a.title, d.genre_id;
