set statistics io on
set statistics time on

select
	productid,
	avg(linetotal) avg_spend_by_product
from Sales.SalesOrderDetail
group by
	ProductID