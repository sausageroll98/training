use AdventureWorks
go
-- example of using CASE in a select query
-- making continuous values discrete:
-- binning
-- descretisation (making discrete)
select
	productnumber,
	color,
	listprice,
	case 
		/*
		during the case comparisons against each row if you have multiple when conditions
		then as soon as a true condition is found, the case exits.
		*/
		when listprice = 0 then 'FREE'
		when listprice >= 1000 then 'Expensive'
		when listprice >= 100 then 'Moderate'
		else 'Cheap'

	end as pricebins
from Production.Product
