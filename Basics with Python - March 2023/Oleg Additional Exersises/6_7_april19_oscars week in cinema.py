movie_name = input()
type_hall = input()
number_purchaised_tickets = int(input())

price = 0

if type_hall == "normal":
    if movie_name == "A Star Is Born":
        price = 7.50
    elif movie_name == "Bohemian Rhapsody":
        price = 7.35
    elif movie_name == "Green Book":
        price = 8.15
    elif movie_name == "The Favourite":
        price = 8.75

elif type_hall == "luxury":
    if movie_name == "A Star Is Born":
        price = 10.50
    elif movie_name == "Bohemian Rhapsody":
        price = 9.45
    elif movie_name == "Green Book":
        price = 10.25
    elif movie_name == "The Favourite":
        price = 11.55

elif type_hall == "ultra luxury":
    if movie_name == "A Star Is Born":
        price = 13.50
    elif movie_name == "Bohemian Rhapsody":
        price = 12.75
    elif movie_name == "Green Book":
        price = 13.25
    elif movie_name == "The Favourite":
        price = 13.95

total_price = price * number_purchaised_tickets

print(f"{movie_name} -> {total_price:.2f} lv.")