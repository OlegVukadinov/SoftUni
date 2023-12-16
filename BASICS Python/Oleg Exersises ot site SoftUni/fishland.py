price_skumria = float(input())
price_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_shells = int(input())

cena_shells = kg_shells * 7.5
cena_palamud = kg_palamud * (price_skumria + price_skumria * 0.60)
cena_safrid = kg_safrid * (price_caca + price_caca * 0.80)

smetka = (f"{(cena_palamud + cena_safrid + cena_shells):.2f}")
print(smetka)




