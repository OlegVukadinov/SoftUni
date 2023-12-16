from math import floor

record = float(input())
distance_meters = float(input())
time_in_sec_for_1m = float(input())

ivan_time = (distance_meters * time_in_sec_for_1m) + floor(distance_meters / 15) * 12.5
diff = abs(ivan_time - record)

if ivan_time < record:
    print(f'Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.')

else:
    print(f'No, he failed! He was {diff:.2f} seconds slower.')

