select
	SalesOrderID,
	OrderDate,
	ShipDate,
	DeliveryPeriod = cast((ShipDate - OrderDate)as int),
	TotalDue,
	SubTotal,
	TaxAmt,
	Freight,
	Differenceamt = TotalDue - SubTotal - TaxAmt - Freight
from Sales.SalesOrderHeader