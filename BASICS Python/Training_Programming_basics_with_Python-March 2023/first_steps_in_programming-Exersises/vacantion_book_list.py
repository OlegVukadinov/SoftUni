numbers_of_pages = int(input())
pages_for_hour = int(input())
numbers_of_days = int(input())

total_time_reading = numbers_of_pages // pages_for_hour

needed_hours_per_day = total_time_reading // numbers_of_days
print(needed_hours_per_day)

