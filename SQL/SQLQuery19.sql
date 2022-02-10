select
	Sales.SalesOrderDetail.SalesOrderID,
	avg(orderqty) avgorderqty,
	min(orderqty) minorderqty,
	max(orderqty) maxorderqty,
	sum(orderqty) sumorderqty
	
from Sales.SalesOrderDetail
inner join  Sales.SalesOrderHeader
on sales.SalesOrderDetail.SalesOrderID = Sales.SalesOrderHeader.SalesOrderID
group by sales.salesorderdetail.SalesOrderID

