CREATE OR REPLACE FUNCTION ensure_unique_phone_number()
RETURNS TRIGGER AS $$
DECLARE
    existing_user_id INT;
BEGIN
    -- Check if the phone number already exists for another user
    SELECT ID INTO existing_user_id FROM Account WHERE Phone = NEW.Phone AND ID != NEW.ID;
    IF found THEN
        RAISE EXCEPTION 'Phone number % already exists for user ID %.', NEW.Phone, existing_user_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_unique_phone_number
BEFORE INSERT OR UPDATE ON Account
FOR EACH ROW EXECUTE FUNCTION ensure_unique_phone_number();