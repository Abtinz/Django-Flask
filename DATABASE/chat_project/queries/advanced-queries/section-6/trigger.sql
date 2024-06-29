CREATE OR REPLACE FUNCTION log_inserts()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO AuditLog (TableName, OperationType, OperatorUsername, Changes)
    VALUES ('account', 'INSERT', CURRENT_USER, row_to_json(NEW)::text);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_after_insert
AFTER INSERT ON account
FOR EACH ROW EXECUTE FUNCTION log_inserts();


--Update
CREATE OR REPLACE FUNCTION log_updates()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO AuditLog (TableName, OperationType, OperatorUsername, Changes)
    VALUES ('account', 'UPDATE', CURRENT_USER, ('OLD: '||row_to_json(OLD)::text||', NEW: '||row_to_json(NEW)::text));
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_after_update
AFTER UPDATE ON account
FOR EACH ROW EXECUTE FUNCTION log_updates();


--DELETE
CREATE OR REPLACE FUNCTION log_deletes()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO AuditLog (TableName, OperationType, OperatorUsername, Changes)
    VALUES ('account', 'DELETE', CURRENT_USER, row_to_json(OLD)::text);
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_after_delete
AFTER DELETE ON account
FOR EACH ROW EXECUTE FUNCTION log_deletes();
