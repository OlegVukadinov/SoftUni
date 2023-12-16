from math import floor

record_sek = float(input())
distance_m = float(input())
time_sek_for_m = float(input())

time_for_climbing_sec = distance_m * time_sek_for_m
delay = (floor(distance_m / 50)) * 30
total_time = time_for_climbing_sec + delay

if total_time < record_sek:
    print(f" Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {abs(record_sek - total_time):.2f} seconds slower.")
