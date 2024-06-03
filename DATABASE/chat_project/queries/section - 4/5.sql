SELECT DISTINCT
    A1.username AS User1,
    A2.username AS User2
FROM
    GroupUsers GU1
    INNER JOIN GroupUsers GU2 ON GU1.groupID = GU2.groupID AND GU1.userID < GU2.userID
    INNER JOIN Account A1 ON GU1.userID = A1.ID
    INNER JOIN Account A2 ON GU2.userID = A2.ID;
