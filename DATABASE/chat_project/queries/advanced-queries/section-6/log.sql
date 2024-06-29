CREATE TABLE AuditLog (
    LogID SERIAL PRIMARY KEY,
    TableName VARCHAR(255),
    OperationType VARCHAR(10),
    OperationTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    OperatorUsername VARCHAR(255),
    Changes TEXT
);
