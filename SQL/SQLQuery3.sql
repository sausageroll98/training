-- I want to project some data about each product 
-- (name, listprice, color)
-- I also want to see each subcategory name and each category name for each product
-- 5 columns, spanning 3 tables which all relate

select
	p.[name] as ProductName,
	p.listprice,
	p.color,
	s.[name] as SubcatName, --[Production].[ProductSubcategory]
	c.[name] as CatName --[Production].[ProductCategory]
from [Production].[Product] as p
join [Production].[ProductSubcategory] as s
	on p.ProductSubcategoryID = s.ProductSubcategoryID
join [Production].[ProductCategory] as c
	on s.ProductCategoryID = c.ProductCategoryID
