use hotel
go
--Q1
select
	*
from booking
inner join hotel
on booking.hotel_code = hotel.hotel_code

--Q2
;
with booking_guest_join as 
(
select
	booking_id,
	cost,
	hotel_code,
	first_name,
	last_name
from hotel.dbo.booking b
inner join hotel.dbo.guest g
on b.guest_id = g.guest_id
)

select
	booking_id,
	bg.cost,
	h.hotel_name,
	first_name,
	last_name
from booking_guest_join bg
inner join hotel h
on bg.hotel_code = h.hotel_code

--Q3
;
with booking_guest_join as 
(
select
	booking_id,
	cost,
	hotel_code,
	first_name,
	last_name,
	birth_date
from hotel.dbo.booking b
inner join hotel.dbo.guest g
on b.guest_id = g.guest_id
)

select
	booking_id,
	bg.cost,
	h.hotel_name,
	first_name,
	last_name,
	birth_date
from booking_guest_join bg
inner join hotel h
on bg.hotel_code = h.hotel_code
where year(birth_date) >= 1990

--Q4
select
	guest.guest_id,
	first_name,
	last_name,
	count(booking.guest_id) cnt
from guest
left join booking
on guest.guest_id = booking.guest_id
group by guest.guest_id, guest.first_name, guest.last_name

--Q5
select
	hotel_name
from hotel
where hotel_code not in(select hotel_code from booking)

--Q6
select 
	g.guest_id,
	g.first_name,
	g.last_name
from booking b
inner join guest g
on b.guest_id = g.guest_id
where
month(check_in) <=2 and month(check_out) >= 3
or month(check_in) = 3

--Q7
select 
	g.guest_id,
	g.first_name,
	g.last_name
from guest g
left join
(
select 
	g.guest_id,
	g.first_name,
	g.last_name
from booking b
inner join guest g
on b.guest_id = g.guest_id
where
month(check_in) <=2 and month(check_out) >= 3
or month(check_in) = 3
) r
on g.guest_id = r.guest_id
where r.guest_id is null

