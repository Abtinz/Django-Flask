use AdventureWorks2016

GO 
--start with ...
Select * FROM HumanResources.Department
WHERE Name LIKE 'P%'

--end with ...
Select * FROM HumanResources.Department
WHERE Name LIKE '%ing'

--SECOND CHAR IS ...
Select * FROM HumanResources.Department
WHERE Name LIKE '_a%'

--THIRD CHAR IS ...
Select * FROM HumanResources.Department
WHERE Name LIKE '__m%'

--SECOND CHAR FROM LASTS CHARACTERS IS ...
Select * FROM HumanResources.Department
WHERE Name LIKE '%n_'

--CONTAINS ... CHARACTERS
Select * FROM HumanResources.Department
WHERE Name LIKE '%an%'
