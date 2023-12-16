price_baggage_over20kg = float(input())
kg_baggage = float(input())
days_till_trip = int(input())
pcs_baggage = int(input())

baggage_price = 0

if kg_baggage < 10:
    baggage_price = price_baggage_over20kg * 0.20
elif 10 <= kg_baggage <= 20:
    baggage_price =  price_baggage_over20kg * 0.50 
elif kg_baggage > 20:
    baggage_price = price_baggage_over20kg

if days_till_trip > 30:
    baggage_price = baggage_price + baggage_price * 0.10
elif 7 <= days_till_trip <= 30:
    baggage_price = baggage_price + baggage_price * 0.15
elif days_till_trip <= 7:
    baggage_price = baggage_price + baggage_price * 0.40

total_price = pcs_baggage * baggage_price

print(f" The total price of bags is: {total_price:.2f} lv. ")