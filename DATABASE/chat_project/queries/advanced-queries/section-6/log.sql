--ok now we are going to save logs of users and admins operations!
-- PK: LogID
-- TableName, OperationType -> which table is under which operation
-- OperationTimestamp , OperatorUsername -> who did this operations and when ?
--changes -> example: user abtin username has changed to abtinz through this operation.

CREATE TABLE AuditLog (
    LogID SERIAL PRIMARY KEY,
    TableName VARCHAR(255),
    OperationType VARCHAR(10),
    OperationTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    OperatorUsername VARCHAR(255),
    Changes TEXT
);
