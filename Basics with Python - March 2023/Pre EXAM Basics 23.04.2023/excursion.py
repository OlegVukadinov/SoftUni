number_people_in_group = int(input())
number_nights = int(input())
number_transport_cards = int(input())
number_ticket_museum = int(input())

price_per_night = 20
price_card_transport = 1.60
price_museum_ticket = 6

price_per_one = price_per_night * number_nights + price_card_transport * number_transport_cards \
    + price_museum_ticket * number_ticket_museum

price_for_all = price_per_one * number_people_in_group

total_price = price_for_all + price_for_all * 0.25

print(f'{total_price:.2f}')
