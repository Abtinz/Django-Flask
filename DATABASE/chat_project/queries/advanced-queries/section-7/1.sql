CREATE OR REPLACE FUNCTION count_messages_between_users(user1_id INT, user2_id INT)
RETURNS INT AS $$
DECLARE
    message_count INT;
BEGIN
    SELECT COUNT(*) INTO message_count
    FROM ChatMessage
    WHERE (senderID = user1_id AND chatID IN (SELECT ID FROM Chat WHERE firstUserID = user2_id OR secondUserID = user2_id))
       OR (senderID = user2_id AND chatID IN (SELECT ID FROM Chat WHERE firstUserID = user1_id OR secondUserID = user1_id));
    RETURN message_count;
END;
$$ LANGUAGE plpgsql;
