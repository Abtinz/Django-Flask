use SchoolDB

go 
SELECT SureName , LastName FROM Persons
UNION 
SELECT Name , LastName FROM FootBallTeam

go
SELECT SureName , LastName FROM Persons
UNION ALL 
SELECT Name , LastName FROM FootBallTeam

go
SELECT SureName , LastName FROM Persons
intersect 
SELECT Name , LastName FROM FootBallTeam
