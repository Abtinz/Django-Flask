CREATE VIEW user_message_group AS
SELECT gm.ID, gm.text, gm.Time, a.Name AS SenderName, g.Name AS GroupName
FROM GroupMessage gm
JOIN Account a ON gm.senderID = a.ID
JOIN Groups g ON gm.groupID = g.ID;
