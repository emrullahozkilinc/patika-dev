select count(*)
from film
where length >
(
select avg(length) 
from film
);


select count(*)
from film
where rental_rate =
(
select max(rental_rate)
from film
);


(
select title
from film
where length =
	(
	select max(length)
	from film
	)
)
union
(
select title
from film
where replacement_cost =
	(
	select min(replacement_cost)
	from film
	)
);


select *
from customer
where customer_id = any
(
select customer_id 
from payment
group by customer_id 
order by count(*) desc
limit 5
);
