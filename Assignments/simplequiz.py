score = 0



def tallyscore(a, b):
    global score
    if a == b:
        print ("Correct")
        score = score + 1
    else:
        print("Wrong")


tallyscore(input("What is 7 + 5\n>"), "12")
tallyscore(input("What is 6 + 2\n>"), "8")
tallyscore(input("What is 3 + 8\n>"), "11")
tallyscore(input("What is 8 + 4\n>"), "12")
tallyscore(input("What is 1 + 9\n>"), "10")

print("You got " + str(score) + "/5")
