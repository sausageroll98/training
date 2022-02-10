use datalab_ce02
go
--create table people1
--(
--fname varchar(10),
--lname varchar(10),
--dob date
--)
--go
--create table people2
--(
--fname varchar(10),
--lname varchar(10),
--dob date
--)
go
select * from people1
select * from people2
go
--insert into people1
--values
--('joe','bloggs','1990-02-01')
--go
--insert into people2
--values
--('joe','bloggs','1990-02-01')
--go
--insert into people1
--values
--('dave','higgins','1980-02-01')
--go

select fname, lname, dob from people1
union --removes any dupes
select fname, lname, dob from people2

select fname, lname, dob from people1
union all -- does not remove dupes
select fname, lname, dob from people2

select fname, lname, dob from people1
intersect --return rows that are common to both (all) tables
select fname, lname, dob from people2

select fname, lname, dob from people1
except --returns rows from the first table that are NOT in the second table
select fname, lname, dob from people2