input_text = input()

sum_vowels = 0

for vowel in input_text:
    if vowel == 'a':
        sum_vowels += 1
    elif vowel == 'e':
        sum_vowels += 2
    elif vowel == 'i':
        sum_vowels += 3
    elif vowel == 'o':
        sum_vowels += 4
    elif vowel == 'u':
        sum_vowels += 5

print(sum_vowels)

