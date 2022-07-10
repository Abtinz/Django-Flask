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