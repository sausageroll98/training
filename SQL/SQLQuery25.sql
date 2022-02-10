use AdventureWorks
go
set statistics io on
select
	name,
	productnumber,
	color,
	listprice
from Production.Product
where color = 'Grey'

--select
--	count(*) cnt,
--	color
--from Production.Product
--group by
--	color
--order by cnt desc