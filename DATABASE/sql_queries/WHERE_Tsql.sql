use AdventureWorks2016

GO 
--sorting
Select VacationHours FROM HumanResources.Employee
WHERE VacationHours > 30 
ORDER BY SickLeaveHours desc;

GO
Select VacationHours FROM HumanResources.Employee
WHERE VacationHours > 30 AND Gender = 'M'
ORDER BY VacationHours desc;

GO
--NOTEQUAL IN SQL
Select * FROM HumanResources.Employee
WHERE  NationalIDNumber <> 295847284

GO
Select * FROM HumanResources.Employee
WHERE NationalIDNumber = 295847284 OR NationalIDNumber = 509647174

--top of the table
GO
Select TOP 50 * FROM HumanResources.Employee

--min and max
GO 
Select min(VacationHours) FROM HumanResources.Employee

GO 
Select min(SickLeaveHours) FROM HumanResources.Employee

GO 
Select max(VacationHours) FROM HumanResources.Employee

GO 
Select max(SickLeaveHours) FROM HumanResources.Employee
