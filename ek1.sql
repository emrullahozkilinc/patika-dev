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
