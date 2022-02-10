select
	*,
	Region = t.CountryRegionCode + ' - ' + t.[Group]
from Sales.SalesOrderHeader as o
full outer join Sales.SalesTerritory as t
	on o.TerritoryID = t.TerritoryID