--SQL SET operations

--select 'david' as fname, 'portas' as lname, 'data' as skill
--union all
--select 'martin' as fname, 'palmer' as lname, 'cloud' as skill


set statistics time on
select
	firstname, lastname, 'person.person' as src
from Person.Person
union all
select
	productnumber, color, 'production.product' as src
from Production.Product
