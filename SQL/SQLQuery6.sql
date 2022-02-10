select
	p.Name,
	p.Color,
	s.SalesOrderDetailID,
	s.OrderQty
from Sales.SalesOrderDetail as s
inner join  Production.Product as p
	on s.ProductID = p.ProductID
