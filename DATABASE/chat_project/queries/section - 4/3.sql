SELECT
    G.Name AS GroupName,
    A.username AS Username,
    COUNT(GM.ID) AS NumberOfMessages
FROM
    GroupMessage GM
    INNER JOIN Account A ON GM.senderID = A.ID
    INNER JOIN Groups G ON GM.groupID = G.ID
GROUP BY
    G.Name,
    A.username;
