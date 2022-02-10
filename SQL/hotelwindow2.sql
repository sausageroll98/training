use hotel
go

--Q1
select
	booking_id,
	hotel_code,
	check_in,
	cost,
	min(cost) over (partition by hotel_code) min_for_hotel,
	max(cost) over (partition by hotel_code) max_for_hotel,
	avg(cost) over (partition by room_type) avg_for_rmtyp
from booking
order by check_in

--Q2
select
	hotel_code,
	check_in,
	sum(cost) over (partition by hotel_code order by check_in) running_sum
from booking
order by hotel_code

--Q3
select
	booking_id,
	hotel_code,
	guest_id,
	cost,
	sum(cost) over (partition by guest_id) TotalGuestSpend
from booking
order by TotalGuestSpend desc
