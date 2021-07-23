select city, country 
from city
inner join country
on city.city_id = country.country_id;

select concat(first_name,' ',last_name) 
as "İsim Soyisim"
from payment
inner join customer
on payment.customer_id = customer.customer_id;

select concat(first_name,' ', last_name)
	   as "İsim Soyisim"
from rental
inner join customer
on customer.customer_id = rental.customer_id;



--Her bir kişinin sipariş sayısı (büyükten küçüğe)

select distinct concat(first_name,' ',last_name)
	   as "İsim Soyisim",
	   count(*)
	   as "Sipariş Sayısı"
from payment
inner join customer
on payment.customer_id = customer.customer_id
group by first_name, last_name
order by count(*) desc;
