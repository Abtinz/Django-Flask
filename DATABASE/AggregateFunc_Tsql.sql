use AdventureWorks2016

GO
SELECT COUNT(NationalIDNumber) AS 'Employee Count'
FROM HumanResources.Employee

GO
SELECT COUNT(VacationHours) AS 'Lazy Employee Count'
FROM HumanResources.Employee
WHERE VacationHours > 40

GO
SELECT SUM(VacationHours) AS 'Sumation of VacationHours of Lazy Employees'
FROM HumanResources.Employee
WHERE VacationHours > 40

GO
SELECT AVG(VacationHours) AS 'AVG of VacationHours of Lazy Employees'
FROM HumanResources.Employee

GO
SELECT MIN(VacationHours) AS 'MIN of VacationHours of Lazy Employees'
FROM HumanResources.Employee

GO
SELECT MAX(VacationHours) AS 'MAX of VacationHours of Lazy Employees'
FROM HumanResources.Employee
