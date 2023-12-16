depo_suma = float(input())
srok_depo_months = int(input())
lihv_procent_per_year = float(input())
suma = depo_suma + srok_depo_months * ((depo_suma * lihv_procent_per_year / 100 ) / 12)
print(suma)

