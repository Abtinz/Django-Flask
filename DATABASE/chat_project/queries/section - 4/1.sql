SELECT
    A.ID,
    A.username,
    A.phone,
    A.NAME,
    A.fullname,
    G.Name AS GroupName
FROM
    Account A
    INNER JOIN GroupUsers GU ON A.ID = GU.userID
    INNER JOIN Groups G ON GU.groupID = G.ID;
