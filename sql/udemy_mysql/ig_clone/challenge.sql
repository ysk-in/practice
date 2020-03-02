USE ig_clone;

SELECT 
    *
FROM
    users
ORDER BY created_at
LIMIT 5;

SELECT 
    DAYNAME(created_at) AS day, COUNT(*) AS count
FROM
    users
GROUP BY day
ORDER BY count DESC;

SELECT 
    users.id AS user_id,
    username,
    IFNULL(COUNT(image_url), 0) AS photo_count
FROM
    users
        LEFT JOIN
    photos ON users.id = photos.user_id
WHERE
    photos.image_url = NULL
;