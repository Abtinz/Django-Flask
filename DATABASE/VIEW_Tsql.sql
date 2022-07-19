GO
CREATE VIEW NameView AS
SELECT SureName , LastName
FROM Persons

GO
CREATE VIEW ContactView AS
SELECT Email , PhoneNumber
FROM Persons
WHERE PersonId BETWEEN 5 AND 50