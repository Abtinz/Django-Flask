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

--SELF INNER JOIN
GO
SELECT C2.CourseTitle,C1.CourseTitle
FROM Courses AS C1
INNER JOIN Courses AS C2
ON C1.CategoryID = C2.ParentID

GO
SELECT  C3.CourseTitle, C2.CourseTitle,C1.CourseTitle
FROM Courses AS C1
INNER JOIN Courses AS C2
ON C1.CategoryID = C2.ParentID
INNER JOIN Courses AS C3
ON C2.CategoryID = C3.ParentID