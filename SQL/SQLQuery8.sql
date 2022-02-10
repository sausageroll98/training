use AdventureWorks
go
--select
--	--SalesOrderID,
--	--OrderDate,
--	--datediff(dd, OrderDate, getdate()) Age_of_Order,
--	datename(dw, OrderDate) Day_of_Week,
--	-- datepart(dw, orderdate) as Day_of_week_number
--	TotalDue,
--from sales.SalesOrderHeader

select
	ProductNumber,
	charindex('-', productnumber) as hyph_pos,
	left(ProductNumber, charindex('-', productnumber)-1) Left_two_char,
	right(ProductNumber, len(productnumber)-charindex('-', productnumber)) Right_four_char,
	[name],
	color,
	ListPrice
from Production.Product

