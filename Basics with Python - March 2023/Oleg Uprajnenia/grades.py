number_students = int(input())

counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5_6 = 0
counter_all_grades = 0

for i in range(1,number_students + 1):
    grade = float(input())

    if 2 <= grade <= 2.99:
        counter_2 += 1
        counter_all_grades += grade
    if 3 <= grade <= 3.99:
        counter_3 += 1
        counter_all_grades += grade
    if 4 <= grade <= 4.99:
        counter_4 += 1
        counter_all_grades += grade
    if 5 <= grade <= 6:
        counter_5_6 += 1
        counter_all_grades += grade

    average_grade = counter_all_grades / number_students

print(f"Top students: {counter_5_6 / number_students  * 100:.2f}%")
print(f"Between 4.00 and 4.99: {counter_4 / number_students  * 100:.2f}%")
print(f"Between 3.00 and 3.99: {counter_3 / number_students  * 100:.2f}%")
print(f"Fail: {counter_2 / number_students  * 100:.2f}%")
print(f"Average: {average_grade:.2f}")
