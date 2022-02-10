use AdventureWorks
go
select
	category
	,NA,Black,Blue,Grey,Multi,Red,Silver,[Silver/Black],White,Yellow
from
(
select
	left(ProductNumber, charindex('-', productnumber)-1) category, --group by col (1st column in pivot table)
	isnull(color, 'NA') color, -- pivot col (1st row in pivot table)
	ListPrice -- measure by col (values in pivot table)
from Production.Product
) r
pivot
(
count(listprice) -- measure by col (values)
for color in (NA,Black,Blue,Grey,Multi,Red,Silver,[Silver/Black],White,Yellow) -- pivot col (1st row)
) p

-- how to determine color groups
/*
select
	Color
from Production.Product
group by 
	Color

select distinct
	color
from Production.Product
*/