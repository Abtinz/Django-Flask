CREATE OR REPLACE FUNCTION get_recent_active_users()
RETURNS TABLE(user_id INT, last_active TIMESTAMP) AS $$
BEGIN
    RETURN QUERY
    SELECT senderID, MAX(Time) as last_active
    FROM ChatMessage
    WHERE Time >= NOW() - INTERVAL '30 days'
    GROUP BY senderID;
END;
$$ LANGUAGE plpgsql;


SELECT * FROM get_recent_active_users();