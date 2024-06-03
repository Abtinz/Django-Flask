-- Active: 1717423284045@@127.0.0.1@5433@postgres

CREATE TABLE Account (
    ID INT PRIMARY KEY,
    Name VARCHAR(255),
    Fullname VARCHAR(255),
    Phone VARCHAR(255) UNIQUE,
    Username VARCHAR(255) UNIQUE
);
