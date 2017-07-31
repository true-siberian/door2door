# door2door
I decided to create new KPI: Trip Schedule Gap (TSG).

TSG is an index disclosing a gap between initial estimation of trip duration and actual duration. Calculation formula is:

𝑇𝑆𝐺=(𝐷𝑟𝑜𝑝𝑜𝑓𝑓𝐸𝑇𝐴_𝑖𝑛𝑖𝑡𝑖𝑎𝑙 − 𝑃𝑖𝑐𝑘𝑢𝑝𝐸𝑇𝐴_𝑖𝑛𝑖𝑡𝑖𝑎𝑙) − (𝐷𝑟𝑜𝑝𝑜𝑓𝑓𝐴𝑇𝐴 − 𝑃𝑖𝑐𝑘𝑢𝑝𝐴𝑇𝐴),

where first part in parentheses means initially estimated date and time for trip start/end when booking was created and the second part means actual date and time of trip start/end.

It shows us a trip schedule shift and can indicate one of the following things:

-insufficient coverage areas (too few drivers/vehicles)
-areas with traffic jam/road works
-weekday traffic density increasing
-problems with driver’s navigation/discipline/skills
-vehicle’s bad condition

Using this index company can fit time estimations to real data and thus improve service level for problem areas. Also with using TSG it is posssible to control company's fleet en masse at longer timelenth.

I also made some conclusions about company's perfomance and business area in general:

1. ETA for these 3 days looks pretty precise and balanced though several cases with TSG over 50 minutes present.
2. 28% of trips with TSG over 10 minutes depart from Kreuzberg area and nearby areas. It is unlikely linked with traffic jam because such trips occur not only in rush hours. I dare to suppose there are a lot of nigth clubs/pubs there.
3. ETA for Western Berlin areas need to be refitted (whole area are experiencing problems with ETA so I guess road network is insufficient for current traffic level there).
4. It seems that service coverage for suburban areas is insufficient because 88% of outcoming trips and 84% of incoming ones belong to areas with zip codes 10***. Zip codes 12***, 13***, 14*** form minor part of destinations. It can be helpful for company's business to improve service in suburbs.
