n_number_comps = int(input())

num_sales = 0
rating = 0
possible_sales = 0

counter_rating = 0

for i in range(1, n_number_comps + 1):
    number_possible_sales_and_rating = input()

    rating = int(number_possible_sales_and_rating[len(number_possible_sales_and_rating) - 1])
    counter_rating += rating
    possible_sales = int(number_possible_sales_and_rating) // 10

    if rating == 2:
        num_sales += possible_sales * 0
    elif rating == 3:
        num_sales += possible_sales * 0.50
    elif rating == 4:
        num_sales += possible_sales * 0.70
    elif rating == 5:
        num_sales += possible_sales * 0.85
    elif rating == 6:
        num_sales += possible_sales * 1

print(f'{num_sales:.2f}')
print(f'{counter_rating / n_number_comps:.2f}')
