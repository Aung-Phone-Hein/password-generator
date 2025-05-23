import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
              'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                  'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
list_pw = []
for i in range(0,nr_letters):
    let = random.choice(letters)
    list_pw.append(let)
for i in range(0,nr_symbols):
    symb = random.choice(symbols)
    list_pw.append(symb)
for i in range(0,nr_numbers):
    numb = random.choice(numbers)
    list_pw.append(numb)
    
random.shuffle(list_pw)
password = "".join(str(e) for e in list_pw)
print(f"Your password is {password}")