SELECT
    A.username
FROM
    Account A
    JOIN GroupMessage GM ON A.ID = GM.senderID
WHERE
    DATE(GM.Time) = '2024-03-06' 
GROUP BY
    A.ID,
    A.username
HAVING
    COUNT(DISTINCT GM.groupID) >= 2;