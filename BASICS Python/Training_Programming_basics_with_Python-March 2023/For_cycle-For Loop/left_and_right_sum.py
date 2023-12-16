n = int(input())

left_sum = 0
right_sum = 0

for number in range(1, n+1):
    num = int(input())
    left_sum += num

for number in range(1, n+1):
    num = int(input())
    right_sum += num

if left_sum == right_sum:
    print(f" Yes, sum = {right_sum}")

else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")