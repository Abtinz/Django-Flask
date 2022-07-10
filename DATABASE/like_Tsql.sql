use AdventureWorks2016

GO 
--start with ...
Select * FROM HumanResources.Department
WHERE Name LIKE 'P%'

--end with ...
Select * FROM HumanResources.Department
WHERE Name LIKE '%ing'