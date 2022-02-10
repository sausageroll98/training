use hotel
go

--Q1
select
	first_name,
	last_name,
	birth_date,
	year(cast(getdate() as date)) - year(birth_date) Age
from hotel.dbo.guest
where (year(cast(getdate() as date)) - year(birth_date)) >=30

--Q2
select
	*
from hotel.dbo.booking
where 
month(check_in) <=2 and month(check_out) >= 3
or month(check_in) = 3

--Q3
select
	*,
	datediff(dd, check_in, check_out) number_of_nights
from hotel.dbo.booking

--Q4
select
	*
from hotel.dbo.guest
where birth_date is null and points>100

--Q5
select
	booking_id,
	hotel_code,
	cost,
	discount,
	(cost + isnull(discount, 0)) fullcost
from booking