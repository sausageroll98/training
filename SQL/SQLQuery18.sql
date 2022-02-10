use AdventureWorks
go
--select top 10
--	*
--from Sales.SalesOrderDetail
--summarise by PRODUCTID	
select
	ProductID,
	avg(orderqty) as avgorderqty,
	count(*) as ordercount,
	sum(orderqty) as totalitemssold,
	sum(linetotal) as totalvaluespend
from Sales.SalesOrderDetail
where UnitPrice > 500
group by
	ProductID
having avg(orderqty) > 2