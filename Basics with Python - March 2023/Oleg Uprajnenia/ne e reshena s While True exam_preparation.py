bad_grades = int(input())

counter_bad_grades = 0
counter_all_tasks = 0
counter_grades = 0

while True:
    name_task = input()
    grade = int(input())

    counter_all_tasks += 1
    counter_grades += grade

    if name_task == "Enough":
        print(f"Average score: {counter_grades / counter_all_tasks:.2f}")
        print(f"Number of problems: {counter_all_tasks}")
        print(f"Last problem: {name_task}")
        break

    if grade <= 4:
        counter_bad_grades += 1

    if counter_bad_grades == bad_grades:
        print(f"You need a break, {counter_bad_grades} poor grades")
        break