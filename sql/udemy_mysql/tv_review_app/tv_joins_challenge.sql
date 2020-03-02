USE tv_review_app;

-- SELECT 
--     reviewers.id,
--     first_name,
--     last_name,
--     COUNT(rating) AS COUNT,
--     IFNULL(MIN(rating), 0) AS MIN,
--     IFNULL(MAX(rating), 0) AS MAX,
--     IFNULL(AVG(rating), 0) AS AVG,
--     IF(COUNT(rating) >= 1,
--         'ACTIVE',
--         'INACTIVE') AS STATUS
-- FROM
--     reviewers
--         LEFT JOIN
--     reviews ON reviewers.id = reviews.reviewer_id
-- GROUP BY first_name , last_name;

SELECT 
    title,
    rating,
    CONCAT(first_name, ' ', last_name) AS reviewer
FROM
    series
        JOIN
    reviews ON series.id = reviews.series_id
        JOIN
    reviewers ON reviews.reviewer_id = reviewers.id
ORDER BY title;
