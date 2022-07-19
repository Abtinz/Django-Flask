GO

ALTER TABLE Courses
--Adding a column
ADD Description NVARCHAR(150)

GO
ALTER TABLE Courses
ADD CourseInstituation NVARCHAR(30) NOT NULL DEFAULT 'SQL & DS'

GO
ALTER TABLE Courses
ALTER COLUMN CourseInstituation NVARCHAR(30) NULL