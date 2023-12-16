hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

exam_time_in_min = hour_of_exam * 60 + minute_of_exam
arrival_time_in_min = hour_of_arrival * 60 + minute_of_arrival

diff = abs(exam_time_in_min - arrival_time_in_min)
hours = diff // 60
minutes = diff % 60

if exam_time_in_min == arrival_time_in_min:
    print("On time")

elif exam_time_in_min > arrival_time_in_min:
    if diff <= 30:
        print("On time")
        print(f'{diff} minutes before the start')
    elif 30 < diff <= 59:
        print("Early")
        print(f'{diff} minutes before the start')
    elif diff >= 60:
        print("Early")
        print(f'{hours}:{minutes:02d} hours before the start')
else:
    print('Late')
    if diff < 60:
        print(f'{diff} minutes after the start')
    else:
        print(f'{hours}:{minutes:02d} hours after the start')


