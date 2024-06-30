CREATE OR REPLACE FUNCTION search_messages_groups(search_keyword VARCHAR(250))
RETURNS TABLE(message_id INT, sender_id INT, message_text VARCHAR(250), message_time TIMESTAMP) AS $$
BEGIN
    RETURN QUERY
    SELECT GM.ID AS message_id, GM.senderID AS sender_id, GM.text AS message_text, GM.Time AS message_time
    FROM GroupMessage AS GM
    WHERE GM.text LIKE '%' || search_keyword || '%';
END;
$$ LANGUAGE plpgsql;

SELECT * FROM search_messages_group('visca');
