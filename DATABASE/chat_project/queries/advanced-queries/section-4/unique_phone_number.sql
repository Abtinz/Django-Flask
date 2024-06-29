CREATE OR REPLACE FUNCTION ensure_message_validity()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.senderID IS NULL OR NEW.chatID IS NULL THEN
        RAISE EXCEPTION 'Both senderID and chatID must be provided.';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_message_validity_assertion
BEFORE INSERT OR UPDATE ON ChatMessage
FOR EACH ROW EXECUTE FUNCTION ensure_message_validity();
