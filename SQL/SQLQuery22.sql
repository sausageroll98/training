--create view jeevan_pivotfreight
--as
select
	orderyear,
	Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,[Dec]
from (
select
	year(orderdate) as orderyear,
	left(orderdate,4) month_value,
	freight
from Sales.SalesOrderHeader
) r
pivot
(
	sum(freight)
	for month_value in (Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,[Dec])
) p