-- List top scorers from hbtn_0c_0.second_table
-- with score >= 10

SELECT
score, name
FROM
second_table
WHERE score >= 10
ORDER BY score DESC;
