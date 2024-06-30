CREATE OR REPLACE FUNCTION user_conversations_history(user1_id INT, user2_id INT, limits INT)
RETURNS TABLE(message_id INT, sender_id INT, message_text VARCHAR(250), message_time TIMESTAMP) AS $$
BEGIN
    RETURN QUERY
    SELECT cm.ID AS message_id, cm.senderID AS sender_id, cm.text AS message_text, cm.Time AS message_time
    FROM ChatMessage cm
    WHERE cm.chatID IN (SELECT c.ID FROM Chat c WHERE (c.firstUserID = user1_id AND c.secondUserID = user2_id) OR (c.firstUserID = user2_id AND c.secondUserID = user1_id))
    ORDER BY cm.Time DESC
    LIMIT limits;
END;
$$ LANGUAGE plpgsql;

SELECT * 
FROM user_conversations_history(1, 2, 10);