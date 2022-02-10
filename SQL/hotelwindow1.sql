use hotel
go

--Q1
select
	booking_id,
	hotel_code,
	room_type,
	cost,
	DENSE_RANK() over (order by cost desc) rnk
from booking

--Q2
select
	booking_id,
	hotel_code,
	room_type,
	cost,
	DENSE_RANK() over (partition by room_type order by cost desc) rnk
from booking
order by room_type, booking_id

--Q3
select
	guest.guest_id,
	first_name,
	last_name,
	count(booking.guest_id) num_bookings,
	sum(booking.cost) tot_cost,
	rank() over (order by sum(booking.cost) desc) rnk
from guest
left join booking
on guest.guest_id = booking.guest_id
group by guest.guest_id, guest.first_name, guest.last_name

--Q4.1
select
	guest.guest_id,
	first_name,
	last_name,
	count(booking.guest_id) num_bookings,
	sum(booking.cost) tot_cost,
	rank() over (order by count(booking.guest_id) desc) rnk
from guest
left join booking
on guest.guest_id = booking.guest_id
group by guest.guest_id, guest.first_name, guest.last_name

--Q4.2
select top 10
	guest.guest_id,
	first_name,
	last_name,
	count(booking.guest_id) num_bookings,
	sum(booking.cost) tot_cost
from guest
left join booking
on guest.guest_id = booking.guest_id
group by guest.guest_id, guest.first_name, guest.last_name
order by num_bookings desc