num_students_at_exam = int(input())

counter_two = 0
counter_three = 0
counter_four = 0
counter_five = 0
counter_all_rates = 0

for i in range(1, num_students_at_exam + 1):
    rate = float(input())

    if 2.00 <= rate <= 2.99:
        counter_two += 1
        counter_all_rates += rate

    elif 3.00 <= rate <= 3.99:
        counter_three += 1
        counter_all_rates += rate

    elif 4.00 <= rate <= 4.99:
        counter_four += 1
        counter_all_rates += rate

    elif 5.00 <= rate:
        counter_five += 1
        counter_all_rates += rate

average_rate = counter_all_rates / num_students_at_exam

perc_rate_two = counter_two / num_students_at_exam * 100
perc_rate_three = counter_three / num_students_at_exam * 100
perc_rate_four = counter_four / num_students_at_exam * 100
perc_rate_five = counter_five / num_students_at_exam * 100

print(f"Top students: {perc_rate_five:.2f}%")
print(f"Between 4.00 and 4.99: {perc_rate_four:.2f}%")
print(f"Between 3.00 and 3.99: {perc_rate_three:.2f}%")
print(f"Fail: {perc_rate_two:.2f}%")
print(f"Average: {average_rate:.2f}")
