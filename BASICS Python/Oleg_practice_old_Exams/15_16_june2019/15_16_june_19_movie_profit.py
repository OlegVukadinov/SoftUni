movie_name = input()
days_pcs = int(input())
tickets_pcs = int(input())
ticket_price = float(input())
percent_for_cinema =  int(input())

price_for_tickets_per_day = tickets_pcs * ticket_price
money_for_all_period = days_pcs * price_for_tickets_per_day
money_for_cinema = money_for_all_period * percent_for_cinema / 100
movie_profit = money_for_all_period - money_for_cinema

print(f"The profit from the movie {movie_name} is {movie_profit:.2f} lv.")