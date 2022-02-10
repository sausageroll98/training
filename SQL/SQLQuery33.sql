use datalab_ce02
go
-- manually insert
/*
insert into patientdata
(nhsnumber, fname, lname, dob)
VALUES
('918273859346', 'lois', 'griffin', '1969-08-17'),
('029475867382', 'Chris', 'griffin', '1992-12-25')
*/
--copy/paste insert
insert into patientdata
(nhsnumber, fname, lname)
SELECT top 10
	'zzzzzzzzzzzz',
	firstname,
	lastname
from AdventureWorks.Person.Person
truncate table patientdata (to empty an entire table)
--delete from patientdata where patient_id = 2 --(to delete specific rows using a WHERE clause)
dbcc checkident(patientdata, reseed, 0)
select * from patientdata