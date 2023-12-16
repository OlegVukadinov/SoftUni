actor_name = input()
start_points = float(input())
number_of_evaluation = int(input())

counter_points = start_points

for current_number_of_evaluation in range(1, number_of_evaluation + 1):
    eval_name = input()
    points = float(input())

    counter_points += len(eval_name) * points / 2

    if counter_points > 1250.5:
        break

if counter_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {counter_points:.1f}!")

else:
    print(f"Sorry, {actor_name} you need {(1250.5 - counter_points):.1f} more!")
