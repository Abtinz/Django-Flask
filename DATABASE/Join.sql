use SchoolDB

GO
SELECT MajorTypeID , MajorTitle FROM Persons
CROSS JOIN Majors


GO
SELECT MajorTypeID , MajorTitle FROM Persons
INNER JOIN Majors 
ON Persons.MajorTypeID = Majors.MajorID

GO
SELECT MajorTypeID , MajorTitle FROM Persons
LEFT JOIN Majors 
ON Persons.MajorTypeID = Majors.MajorID

GO
SELECT MajorTypeID , MajorTitle FROM Persons
RIGHT JOIN Majors 
ON Persons.MajorTypeID = Majors.MajorID