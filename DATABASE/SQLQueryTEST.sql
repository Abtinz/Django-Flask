use AdventureWorks2016

GO

select 'Test'

GO 

-- AS --> COLUMNS NAME
SELECT 'SECOND TEST' AS 'COLUMN TEST'

GO
-- * IS FOR ALL COLUMNS OF TABLE
SELECT * FROM Person.Address
-- specific column ' ' from table
SELECT City FROM Person.Address
GO 
SELECT StateProvinceID AS StateIdNumber FROM Person.Address


GO 
-- conditional selection

SELECT * FROM HumanResources.Employee 
WHERE SickLeaveHours > 50

GO
SELECT * FROM HumanResources.Employee 
WHERE BusinessEntityID % 2 = 0 ;
SELECT * FROM HumanResources.Employee 
WHERE BusinessEntityID BETWEEN 40 AND 80 ;

GO
SELECT * FROM HumanResources.Employee 
WHERE Gender  = 'M' ;

--REMOVE REPEATED DATA
GO 
SELECT DISTINCT StoreID FROM Sales.Customer