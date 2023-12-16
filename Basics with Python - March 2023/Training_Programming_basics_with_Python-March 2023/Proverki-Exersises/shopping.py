budget = float(input())
pcs_videocards = int(input())
pcs_procesors = int(input())
pcs_ram_memory = int(input())

price_videocards = pcs_videocards * 250
price_procesors = pcs_procesors * price_videocards * 0.35
price_ram_memory = pcs_ram_memory * price_videocards * 0.10

total_price = price_videocards + price_procesors + price_ram_memory

if pcs_videocards > pcs_procesors:
    total_price = total_price - total_price * 0.15

if total_price <= budget:
    print(f'You have {budget - total_price:.2f} leva left!')

else:
    print(f'Not enough money! You need {total_price - budget:.2f} leva more!')
