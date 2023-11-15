-- Selecting show titles for Comedy genre and displaying the result
SELECT t.title
FROM tv_shows AS t
INNER JOIN tv_show_genres AS s ON t.id = s.show_id
INNER JOIN tv_genres AS g ON g.id = s.genre.id
WHERE g.name = 'Comedy'
ORDER BY t.title;
