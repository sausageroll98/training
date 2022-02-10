use AdventureWorks
go

--Q1
select
	Color,
	sum(actualCost) SumActualCost,
	rank() over (order by sum(actualcost) desc) RankPosition
from Production.TransactionHistory th
left join Production.Product p
on th.ProductID = p.ProductID
group by Color

--Q2
;with inter as
(
select
	Color,
	ReorderPoint,
	[Weight]
from Production.Product
where ReorderPoint > 10
)
select
	Color,
	sum([Weight]) SumWeight,
	avg([Weight]) AvgWeight
from inter
group by Color

--Q3
select top 10
	Color,
	Style,
	avg(listprice) avgListPrice
from Production.Product
group by Color, Style
order by avgListPrice desc
