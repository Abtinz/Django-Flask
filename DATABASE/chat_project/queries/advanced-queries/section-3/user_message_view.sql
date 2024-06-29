CREATE VIEW user_message AS
SELECT cm.ID, cm.text, cm.Time, a.Name AS SenderName, a.Username AS SenderUsername
FROM ChatMessage cm
JOIN Account a ON cm.senderID = a.ID;
