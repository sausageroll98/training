create nonclustered index ix_productid
on sales.salesorderdetail(productid)
include(linetotal)