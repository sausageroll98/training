--common table expressions (CTE)
-- a way of aliasing the entire query
;with pricerank
as
(
select
    ProductNumber
	,ListPrice
	,rank() over (order by listprice desc) as pricerankdesc
	,dense_rank() over (order by listprice desc) as pricedenserankdesc
from Production.Product
--order by ListPrice desc (not allowed an order by inside a common table expression)
)
select
	productnumber,
	listprice,
	pricerankdesc,
	pricedenserankdesc
from pricerank