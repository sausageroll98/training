use AdventureWorks
go

--Q1
;with subcatname
as
(
select
	SalesOrderID,
	ps.[name]
from sales.SalesOrderDetail sod
left join Production.Product pp
on sod.ProductID = pp.ProductID
left join Production.ProductSubcategory ps
on pp.ProductSubcategoryID = ps.ProductSubcategoryID
)

select
	subcatname.[name],
	min(soh.OrderDate) Min_order_date,
	max(soh.OrderDate) Max_order_date
from sales.SalesOrderHeader soh
left join subcatname
on soh.SalesOrderID = subcatname.SalesOrderID
group by subcatname.[name]

--Q2
;with inter
as
(
select
	CustomerID,
	sod.ProductID,
	p.[name],
	OrderDate,
	lead(orderdate) over (partition by sod.productid order by orderdate asc) NextOrderDate,
	datediff(dd, orderdate, lead(orderdate) over (partition by sod.productid order by orderdate asc)) DaysBetweenOrders
from Sales.SalesOrderheader soh
left join sales.SalesOrderDetail sod
on soh.SalesOrderID = sod.SalesOrderID
left join Production.Product p
on sod.ProductID = p.ProductID
)
select
	ProductID,
	[name],
	min(DaysBetweenOrders) MinDays,
	max(DaysBetweenOrders) MaxDays,
	avg(DaysBetweenOrders) AvgDays
from inter
group by ProductID, [name]
order by ProductID

--Q3
;with inter2
as
(
select
	soh.CustomerID,
	FirstName,
	MiddleName,
	LastName,
	TotalDue
from sales.SalesOrderHeader soh
left join sales.Customer c
on soh.CustomerID = c.CustomerID
left join person.Person p
on c.PersonID = p.BusinessEntityID
)

select
	CustomerID,
	FirstName,
	MiddleName,
	LastName,
	sum(totaldue) TotalSpend,
	ROW_NUMBER() over (order by sum(totaldue) desc) RankNumber
	--RANK() over (order by sum(totaldue) desc) RankPosition
from inter2
group by CustomerID, FirstName, MiddleName, LastName

--Q4
;with inter3 as
(
select
	ProductID,
	left(ProductNumber, charindex('-', productnumber)-1) ProductCat,
	(ListPrice - StandardCost) Profit,
	rank() over (order by (ListPrice - StandardCost) desc) ProfitRank
from Production.Product
)

select
	ProductCat,
	sum(Profit) TotalProfit,
	rank() over (order by sum(Profit) desc) TotalProfitRank
from inter3
group by ProductCat

--Q5
select
	datepart(dw, orderdate) day_of_week,
	datepart(yy, orderdate) year_of_order,
	sum(totaldue) SumTotalDue,
	rank() over (order by sum(totaldue)desc) SumTotalDueRank
from sales.SalesOrderHeader
group by datepart(dw, orderdate), datepart(yy, orderdate)
















