use AdventureWorks
go
select
	 [Name]
	 ,ProductNumber
	 ,[ProductNumber] + [Color] [Newname]
	 ,Color
	 ,ListPrice
	 ,StandardCost
	 ,profit = ListPrice-StandardCost
	 -- 'ListPrice-StandardCost profit' would also work

from [Production].[Product]

-- rules for object naming:
-- avoid space
-- avoid reserved SQL keywords
-- first character should be alphabetic (a-z)

declare @runtime int
set @runtime = 65


print 'The query ran in ' + '65' + ' seconds'
print 'The query ran in ' + cast(@runtime as varchar(10)) + ' seconds'