import random

def fortune_teller():
    print("Welcome to the Fortune Teller!")
    print("I will tell your fortune using your number.\n")

    try:
        lucky_number = int(input("Enter your lucky number"))
        years_future = float(input("How many years into the future do you want to see? "))
        magical_number = float(input("Enter a magical number"))

        random_number = random.randint(1, 10)

        score = lucky_number + years_future + magical_number + random_number

        print("\nYour future is...")

        if score < 20:
            print("You will have a calm and peaceful week.")
        elif score < 40:
            print("Something surprising will happen soon!")
        elif score < 60:
            print("You will meet somone who changes your day.") 
        elif score < 80:
            print("You will have a calm and peaceful week.")
        else:
            print("Good fortune and happiness are on the way to you!")

    except ValueError:
        print("\nThat wasn't a number! Try again.\n")
        fortune_teller()
fortune_teller()