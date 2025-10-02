#Parameters AND arguments

#Create a function that adds two numbers together
def add(x, y):
    print(x+y)


add(10,30)

def add_five_numbers(a, b, c, d, e):
    print(a + b + c + d + e)

add_five_numbers(10, 20, 30, 40, 50)    
add_five_numbers(100, 200, 300, 400, 500)   
add_five_numbers(1, 2, 3, 4, 5)   

def full_name(first, last):
    print(first + "" + last)

first_name = input("Enter your first name\n")
last_name = input("Enter your last name\n")

full_name(first_name, last_name)

def area_calculator(length, width):
    print(length*width)

area_calculator(10, 2)
area_calculator(4, 9)
area_calculator(7, 5)

def word_smash(a, b):
    print(str(a) + str(b))

word_smash("Cat", "Dog")
word_smash("3", "Dog")
word_smash("Sup", "Dog")

def echo(word, times):
    print(srt(word) * times)

echo("you", 5)

def happy_birthday(Zach):
    print("Happy Birthdya to you, Happy Birthday to you, Happy Birthday dear, " + name)

happy_birthday    