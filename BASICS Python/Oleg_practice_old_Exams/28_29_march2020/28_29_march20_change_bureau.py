number_bitcoins = int(input())
number_yuans = float(input())
percent_commision = float(input())

one_dollar = 1.76
one_bitcoin = 1168
one_yuan = 0.15 * one_dollar
one_euro = 1.95

all_euro = (number_bitcoins * one_bitcoin + number_yuans * one_yuan) / one_euro
commision = percent_commision * all_euro / 100

change_result = all_euro - commision

print(f'{change_result:.2f}')