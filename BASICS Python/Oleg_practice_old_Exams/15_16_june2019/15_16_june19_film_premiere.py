movie_name = input()
packet_for_movie = input()
number_tickets = int(input())

single_ticket_price = 0
total_price = number_tickets * single_ticket_price

if movie_name == "John Wick" and packet_for_movie == "Drink":
    single_ticket_price = 12
elif movie_name == "John Wick" and packet_for_movie == "Popcorn":
    single_ticket_price = 15
elif movie_name == "John Wick" and packet_for_movie == "Menu":
    single_ticket_price = 19

if movie_name == "Star Wars" and packet_for_movie == "Drink":
    single_ticket_price = 18
elif movie_name == "Star Wars" and packet_for_movie == "Popcorn":
    single_ticket_price = 25
elif movie_name == "Star Wars"  and packet_for_movie == "Menu":
    single_ticket_price = 30

if movie_name == "Jumanji" and packet_for_movie == "Drink":
    single_ticket_price = 9
elif movie_name == "Jumanji" and packet_for_movie == "Popcorn":
    single_ticket_price = 11
elif movie_name == "Jumanji"  and packet_for_movie == "Menu":
    single_ticket_price = 14

total_price = number_tickets * single_ticket_price

if number_tickets >= 4 and movie_name == "Star Wars":
    total_price = total_price - total_price * 0.30

elif number_tickets == 2  and movie_name == "Jumanji":
    total_price = total_price - total_price * 0.15

print(f"Your bill is {total_price:.2f} leva.")