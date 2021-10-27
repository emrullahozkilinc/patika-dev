-- 1
with dq as(
select date(payment_date) as pd,
	count(*) as toplam_satis
from payment
where extract(month from payment_date) = 3
group by pd
) 

select *,
	avg(toplam_satis)
		over(
		order by pd desc
		rows between 1 preceding and current row
		) as cum_sum
from dq


-- 2
select *,
	first_value(payment_id)
		over(
			partition by customer_id
			rows between unbounded preceding and unbounded following
		) as first_payment
from payment
