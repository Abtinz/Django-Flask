CREATE VIEW user_message AS
SELECT cm.ID, cm.text, cm.Time, a.Name AS SenderName, a.Username AS SenderUsername
FROM ChatMessage cm
JOIN Account a ON cm.senderID = a.ID;

--this sql will provide useful view for each users messages which have been sent in chat service chat
-- we have a natural join of account and chatMessages on userID  and the sender ID! now we are able to find receiver and chat texts!