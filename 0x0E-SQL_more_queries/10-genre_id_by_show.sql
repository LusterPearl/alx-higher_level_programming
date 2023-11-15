-- Selecting shows with at least one genre linked
SELECT a.title, d.genre_id
FROM tv_shows AS a
INNER JOIN tv_show_genres AS d ON a.id = d.show_id
ORDER BY a.title, d.genre_id;
