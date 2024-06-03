SELECT
    A.ID,
    A.username,
    CN.chatID,
    GU.groupID
FROM
    Account A
    INNER JOIN Contacts CN ON A.ID = CN.userID
    LEFT JOIN GroupUsers GU ON A.ID = GU.userID
WHERE
    GU.groupID  is NOT  NULL;
