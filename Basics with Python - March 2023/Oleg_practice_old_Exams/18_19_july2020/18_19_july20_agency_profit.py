avio_name = input()
pcs_tickets_for_old = int(input())
pcs_tickets_for_kids = int(input())
neto_price_for_ticket_for_old = float(input())
tax = float(input())

neto_price_for_ticket_for_kid = neto_price_for_ticket_for_old - neto_price_for_ticket_for_old * 0.70
total_price = (pcs_tickets_for_old * (neto_price_for_ticket_for_old + tax)) + (pcs_tickets_for_kids *
                                                                               (neto_price_for_ticket_for_kid + tax))

profit = total_price * 0.20

print(f"The profit of your agency from {avio_name} tickets is {profit:.2f} lv.")
