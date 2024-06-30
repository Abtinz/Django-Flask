CREATE VIEW user_message_group AS
SELECT gm.ID, gm.text, gm.Time, a.Name AS SenderName, g.Name AS GroupName
FROM GroupMessage gm
JOIN Account a ON gm.senderID = a.ID
JOIN Groups g ON gm.groupID = g.ID;

--this sql will provide useful view for each users messages which have been sent in chat service groups
-- through natural join of account and GroupMessages on userID and with group id we are able to find user's group messages with their group names