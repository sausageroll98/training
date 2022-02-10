--Q1
select
	*
from hotel.dbo.guest
where last_name = 'Peterson'

--Q2
select
	*
from hotel.dbo.guest
where last_name <> 'Peterson'

--Q3
select
	title,
	first_name,
	last_name
from hotel.dbo.guest
where title = 'Mr'

--Q4
select
	title,
	first_name,
	last_name
from hotel.dbo.guest
where title = 'Mr' and last_name = 'Peterson'

--Q5
select
	*
from hotel.dbo.account
where hotel_code = 'LOHR' and netamt > 1000

--Q6
select
	*
from hotel.dbo.account
where hotel_code = 'LOHR' and netamt > 1000 or hotel_code = 'MANC' and netamt > 1000

--Q7
select
	transaction_id,
	netamt,
	taxamt,
	netamt + taxamt grossamt
from hotel.dbo.account
where hotel_code = 'LOHR' and netamt > 1000 or hotel_code = 'MANC' and netamt > 1000

--Q8
select
	transaction_id,
	netamt,
	taxamt,
	netamt + taxamt grossamt,
	cast(round((taxamt/(netamt+taxamt)*100),2) as decimal(8,2)) taxamt_as_percent
from hotel.dbo.account
where hotel_code = 'LOHR' and netamt > 1000 or hotel_code = 'MANC' and netamt > 1000