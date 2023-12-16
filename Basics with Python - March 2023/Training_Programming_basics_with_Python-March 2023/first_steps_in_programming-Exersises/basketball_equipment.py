year_tax_basket = int(input())

kecove = year_tax_basket - (year_tax_basket * 0.4)
ekip = kecove - (kecove * 0.2)
topka = ekip * 1/4
aksesoari = 1/5 * topka
total_price = year_tax_basket + kecove + ekip + topka + aksesoari
print(total_price)

