CREATE VIEW user_contacts AS
SELECT a.ID, a.Name, a.Username, a.Phone, c.chatID
FROM Contacts c
JOIN Account a ON c.userID = a.ID;