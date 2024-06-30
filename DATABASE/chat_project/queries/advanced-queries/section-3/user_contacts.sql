CREATE VIEW user_contacts AS
SELECT a.ID, a.Name, a.Username, a.Phone, c.chatID
FROM Contacts c
JOIN Account a ON c.userID = a.ID;

--this sql will provide useful view for each users contacts
-- through natural join of account and contact on userID we are able to find user's contacts and chats