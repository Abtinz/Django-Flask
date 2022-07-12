use SchoolDB

GO
SELECT MajorTypeID , MajorTitle FROM Persons
CROSS JOIN Majors


GO
SELECT MajorTypeID , MajorTitle FROM Persons
INNER JOIN Majors 
ON Persons.MajorTypeID = Majors.MajorID