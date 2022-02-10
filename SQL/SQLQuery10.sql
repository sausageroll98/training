--window functions do not summarise the rows
-- they leave them in their detail state
select
	productnumber,
	color,
	listprice,
	avg(listprice) over (partition by color) as avg_price_by_color,
	price_diff = listprice - avg(listprice) over (partition by color),
	count(color) over (partition by color) as color_no
	/* other stats functions include: sum, min, max, stdev,  */
from Production.Product

-- summarise the rows - not using a window function
select
	color,
	avg(listprice) as avg_price_by_color
from Production.Product
group by
	Color