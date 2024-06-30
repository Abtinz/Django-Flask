--FIRST I am going to provide an access to DBMS For new administrator(i don't know who is Arousha_Azad,is it safe? i don't even know!!!)
CREATE USER Arousha2000azad WITH PASSWORD 'Arousha_Azad';

--ok arousha you can access to account now!
REVOKE SELECT ON account FROM Arousha2000azad;

--you are free to use INSERT, UPDATE, DELETE on account relation(don't disturb it!)
GRANT INSERT, UPDATE, DELETE ON account TO Arousha2000azad;