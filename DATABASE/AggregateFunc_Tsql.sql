use AdventureWorks2016

GO
SELECT COUNT(NationalIDNumber) AS 'Employee Count'
FROM HumanResources.Employee

GO
SELECT COUNT(VacationHours) AS 'Lazy Employee Count'
FROM HumanResources.Employee
WHERE VacationHours > 40