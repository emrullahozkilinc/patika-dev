select *
from film
where title like 'K%'
order by length desc, replacement_cost asc
limit 4;
	  
select rating
from film
group by rating
order by count(*) desc
limit 1;


select first_name, last_name
from customer
where customer_id = all
(
select customer_id
from payment
group by payment.customer_id
order by count(*) desc
limit 1
);


select name as "Kategori Adı", count(*) as "Film Sayısı"
from category
join film_category on category.category_id = film_category.category_id
join film on film.film_id = film_category.film_id
group by name;


select count(*)
from film
where title ilike '%e%e%e%e%';
