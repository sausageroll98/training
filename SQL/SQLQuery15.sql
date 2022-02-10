use AdventureWorks
go
/*
Conditional: Statements | Expressions
IF... ELSE...
CASE... WHEN THEN .... END
*/
--conditional statement, not a select query
if datename(wk, getdate()) = '3'
begin
print 'True'
end
else
print 'False'

select
	BusinessEntityID,
	FirstName,
	MiddleName,
	LastName,
	-- produce a flag to say if middlename is present
	case
		when middlename is null then
		case
			-- people with no middle name and short last name
			when len(lastname) < 5 then 3
			-- no middle name and a long last name 
			else 2
		end
		else 1
	end as middlenamepresent
from Person.Person