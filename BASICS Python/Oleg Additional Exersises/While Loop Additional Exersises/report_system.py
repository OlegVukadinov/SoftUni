expected_sum = int(input())

total_sum_counter = 0
cash_payment_counter = 0
card_payment_counter = 0
sucs_cash_payment_counter = 0
sucs_card_payment_counter = 0


while True:
    command = input()

    if command == "End":
        print("Failed to collect required money for charity.")
        break

    cash_payment = int(command)
    card_payment = int(input())

    if cash_payment <= 100:
        total_sum_counter += cash_payment
        cash_payment_counter += cash_payment
        sucs_cash_payment_counter += 1
        print("Product sold!")
    else:
        print("Error in transaction!")

    if card_payment >= 10:
        total_sum_counter += card_payment
        card_payment_counter += card_payment
        sucs_card_payment_counter += 1
        print("Product sold!")
    else:
        print("Error in transaction!")

    if total_sum_counter >= expected_sum:
        print(f"Average CS: {cash_payment_counter / sucs_cash_payment_counter:.2f}")
        print(f"Average CC: {card_payment_counter / sucs_card_payment_counter:.2f}")
        break