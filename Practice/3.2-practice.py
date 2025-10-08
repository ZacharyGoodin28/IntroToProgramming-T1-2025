def password():
    real_password = "Knigihts"
    submitted_password = input("Zach\n>")

    if real_password == submitted_password:
        print("Correct")

    else:
        print("Wrong")
        check_password()


check_password()