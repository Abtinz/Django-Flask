GO

ALTER TABLE Courses
--Adding a column
ADD Description NVARCHAR(150)


GO
ALTER TABLE Courses
ADD CourseInstituation NVARCHAR(30) NOT NULL DEFAULT 'SQL & DS'

--how to make a column nullable in sql
GO
ALTER TABLE Courses
ALTER COLUMN CourseInstituation NVARCHAR(30) NULL

GO
SP_RENAME 'Courses.CourseInstituation' , 'Instituation' , 'COLUMN'