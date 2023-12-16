name = input()

counter_grades = 0
counter_class = 0
counter_bad = 0

for i in range(1, 12 + 1):
    grade = float(input())

    if grade >= 4:
        counter_class += 1
        counter_grades += grade
    else:
        #counter_grades += grade
        counter_bad += 1

    if counter_bad == 1:
       counter_class += 1
    elif counter_bad > 1:
        print(f"{name} has been excluded at {counter_class} grade")
        break

print(f"{name} graduated. Average grade: {counter_grades / counter_class:.2f}")

 # 36/100