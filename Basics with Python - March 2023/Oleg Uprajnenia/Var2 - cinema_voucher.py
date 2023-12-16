money_voucher = int(input())

counter_tickets = 0
counter_other = 0
articule_price = 0
counter_current_money = money_voucher

while True:
    articule = input()

    if articule == "End":
        break

    if len(articule) > 8:
        articule_price = ord(articule[0]) + ord(articule[1])
        if articule_price > counter_current_money:
            break
        counter_tickets += 1
        counter_current_money -= articule_price

    if len(articule) <= 8:
        articule_price = ord(articule[0])
        if articule_price > counter_current_money:
            break
        counter_current_money -= articule_price
        counter_other += 1

print(f"{counter_tickets}")
print(f"{counter_other}")
