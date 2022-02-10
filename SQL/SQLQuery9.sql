declare @myloc geography
set @myloc = geography::STPointFromText('POINT(52.897460 -1.520680)', 4326)

 

select
     AddressID
    ,AddressLine1
    ,City
    ,SpatialLocation.STDistance(@myloc) / 1000 as DistanceFromMeKM
    ,SpatialLocation.STAsText()
from person.address
order by DistanceFromMeKM asc

/*
geography type in SQL:
- point (long | lat)
- linestring (many long|lat pairs forming a line)
- polygon (closed shapes, last and the first long|lat pair are the same)

*/