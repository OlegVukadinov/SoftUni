book = input()

counter_books = 0

while True:
    next_book = input()
    if next_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {counter_books} books.")
        break
    if book == next_book:
        print(f"You checked {counter_books} books and found it.")
        break
    counter_books += 1







