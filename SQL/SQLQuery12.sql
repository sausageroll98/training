select distinct
	year(orderdate) as orderyear,
	count(*) over (partition by year(orderdate)) order_count_by_year -- counts non null values
	,count(*) over () total_count
	,round(count(*) over (partition by year(orderdate)) / cast(count(*) over () as float) * 100, 1) count_as_percent
from Sales.SalesOrderHeader

order by count_as_percent