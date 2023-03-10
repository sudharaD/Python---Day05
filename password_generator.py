import random

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
simple_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
simple_letter_count = 0
capital_letter_count = 0
password = []

while True:

    letter_count = int(input("How many letters do you need? "))
    number_count = int(input("How many numbers do you need? "))
    symbol_count = int(input("How many symbols do you need? "))

    if letter_count >= 0 and number_count >= 0 and symbol_count >= 0:
        break
    else:
        print("Please enter valid integers as inputs")

if letter_count > 1:
    simple_letter_count = random.randint(1, letter_count)
    capital_letter_count = letter_count - simple_letter_count

elif letter_count == 1:
    if random.randint(1, 2) == 1:
        simple_letter_count = letter_count
    else:
        capital_letter_count = letter_count

for i in range(1, simple_letter_count + 1):
    password.append(random.choice(simple_letters))

for i in range(1, capital_letter_count + 1):
    password.append(random.choice(capital_letters))

for i in range(1, number_count + 1):
    password.append(random.choice(numbers))

for i in range(1, symbol_count + 1):
    password.append(random.choice(symbols))

print(password)

def shuffle_password(password):
    random.shuffle(password)
    return ''.join(password)

shuffled_password = shuffle_password(password)
print(f"Here is your password: {shuffled_password}")