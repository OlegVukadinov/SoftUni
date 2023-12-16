town = input()
type_paket = input()
vip_discount = input()
days = int(input())

price_per_day = 0

if town not in ["Bansko", "Borovets", "Varna", "Burgas"] or type_paket not in ["withEquipment", "noEquipment",
                                                                               "withBreakfast","noBreakfast"]:
    print("Invalid input!")

elif days < 1:
    print("Days must be positive number!")

else:
    if days > 7:
        days = days - 1

    if town == "Bansko" or town == "Borovets":
        if type_paket == "withEquipment":
            price_per_day = 100
            if vip_discount == "yes":
                price_per_day = price_per_day - price_per_day * 0.10

        elif type_paket == "noEquipment":
            price_per_day = 80
            if vip_discount == "yes":
                price_per_day = price_per_day - price_per_day * 0.05

    elif town == "Varna" or town == "Burgas":
        if type_paket == "withBreakfast":
            price_per_day = 130
            if vip_discount == "yes":
                price_per_day = price_per_day - price_per_day * 0.12

        elif type_paket == "noBreakfast":
            price_per_day = 100
            if vip_discount == "yes":
                price_per_day = price_per_day - price_per_day * 0.07


    print(f"The price is {(price_per_day * days):.2f}lv! Have a nice time!")