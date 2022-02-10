select
	ProductNumber,
	ListPrice,
	avg(listprice) over () avgprice,
	stdev(listprice) over ()stdevprice,
	ceiling(abs((listprice - avg(listprice) over ()) / stdev(listprice) over ())) zscore
from Production.Product
order by zscore desc


--rounding methodology in TSQL
--select
--	ceiling(0.78324) as with_ceiling
--	,floor(0.78324) as with_floor
--	,round(0.78324,2) as with_round
--	,round(76523.9873, -2)