-- Selecting shows without a genre linked
SELECT a.title, d.genre_id
FROM tv_shows AS a
LEFT JOIN tv_show_genres AS d ON a.id = d.show_id
WHERE d.genre_id IS NULL
ORDER BY a.title, d.genre_id;
