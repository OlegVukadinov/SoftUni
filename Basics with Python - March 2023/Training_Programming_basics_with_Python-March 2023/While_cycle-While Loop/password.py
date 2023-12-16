username = input()
password = input()

data = input()

while password != data:
  data = input()

if password == data:
    print(f"Welcome {username}!")