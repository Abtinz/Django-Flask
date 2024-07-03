--FIRST I am going to provide an access to DBMS For new administrator(i don't know who is Arousha_Azad,is it safe? i don't even know!!!)
CREATE USER Arousha2000azad WITH PASSWORD 'Arousha_Azad';

--you are no able to use INSERT, UPDATE, DELETE on account relation(don't disturb it!)

REVOKE INSERT, UPDATE, DELETE ON account FROM Arousha2000azad;

--ok arousha you can access to account now!
GRANT SELECT ON account TO Arousha2000azad;