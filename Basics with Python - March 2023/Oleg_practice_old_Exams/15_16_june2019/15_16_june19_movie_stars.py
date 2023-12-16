budget = float(input())
actor_name = input()
actor_salary = 0


while actor_name != "ACTION":

    if len(actor_name) <= 15:
        actor_salary = float(input())
    else:
        actor_salary = budget * 0.20

    budget -= actor_salary

    if budget <= 0:
        print(f"We need {abs(budget):.2f} leva for our actors.")
        break

    actor_name = input()

if budget > 0:
    print(f"We are left with {abs(budget):.2f} leva.")

