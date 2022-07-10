use AdventureWorks2016

GO 
--sorting
Select VacationHours FROM HumanResources.Employee
WHERE VacationHours > 30 
ORDER BY SickLeaveHours desc