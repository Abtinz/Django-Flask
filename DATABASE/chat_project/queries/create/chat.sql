-- Active: 1717423284045@@127.0.0.1@5433@postgres
CREATE TABLE Chat (
    ID INT PRIMARY KEY,
    firstUserID INT,
    secondUserID INT,
    FOREIGN KEY (firstUserID) REFERENCES Account(ID),
    FOREIGN KEY (secondUserID) REFERENCES Account(ID)
);