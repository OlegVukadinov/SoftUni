neobh_nylon = int(input())
neobh_paint = int(input())
neobh_razreditel = int(input())
working_hours = int(input())

sum_for_nylon = (neobh_nylon + 2) * 1.50
sum_for_paint = (neobh_paint + (neobh_paint * 0.10)) * 14.50
sum_for_razreditel = neobh_razreditel * 5.00

total_sum_for_materials = sum_for_nylon + sum_for_paint + sum_for_razreditel + 0.40
sum_for_workers = 0.3 * total_sum_for_materials * working_hours
final_sum = total_sum_for_materials + sum_for_workers
print(final_sum)




