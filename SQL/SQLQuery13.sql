select
	CustomerID,
	OrderDate,
	TotalDue,
	lead(TotalDue) over (partition by customerid order by orderdate asc) NextSpendAmtlead
	,lag(TotalDue) over (partition by customerid order by orderdate asc) NextSpendAmtlag
	-- show the next order date for the customer
	,lead(orderdate) over (partition by customerid order by orderdate asc) NextPurchaseDate
	-- once done that, how many days are there between current order and next?
	,datediff(dd, orderdate, lead(orderdate) over (partition by customerid order by orderdate asc)) DaystoNextOrder
from Sales.SalesOrderHeader
order by customerId