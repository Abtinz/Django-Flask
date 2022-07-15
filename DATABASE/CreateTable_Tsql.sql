CREATE DATABASE CoursesAtenders

CREATE TABLE SqlServerCourse(
        PersonID INT PRIMARY KEY,
		SureName NVARCHAR(20) ,
		LastName NVARCHAR(20)
);

CREATE TABLE APCourse(
        PersonID INT ,
		SureName NVARCHAR(20) ,
		LastName NVARCHAR(20) ,

		PRIMARY KEY(PersonID)
);

CREATE TABLE DataStructureCourse(
        PersonID INT ,
		SureName NVARCHAR(20) NOT NULL,
		LastName NVARCHAR(20) NOT NULL,

		PRIMARY KEY(PersonID)
);


--constraint
CREATE TABLE MLOnlineCourse(
        PersonID INT ,
		SureName NVARCHAR(20) ,
		LastName NVARCHAR(20) ,
		Country NVARCHAR(20) DEFAULT  'Tehran' ,
		NationID NVARCHAR(20) UNIQUE ,
		AGE INT
		CHECK (AGE>15 AND AGE<90)
		PRIMARY KEY(PersonID)
			
);


