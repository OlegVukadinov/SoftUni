num_relaxing_days = int(input())

playing_time_working_days = (365 - num_relaxing_days) * 63
playing_time_relaxing_days = num_relaxing_days * 127

total_playing_time = playing_time_working_days + playing_time_relaxing_days
hour = abs(total_playing_time - 30000) // 60
minutes = round(((abs(total_playing_time - 30000) / 60) - hour) * 60)


if total_playing_time > 30000:
    print("Tom will run away")
    print(f'{hour} hours and {minutes} minutes more for play')

else:
    print("Tom sleeps well")
    print(f'{hour} hours and {minutes} minutes less for play')
