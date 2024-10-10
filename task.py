print("Welcome to the rollercoaster ride! We're happy to have you :)")
height = int(input("What is your height in cm? For security reasons"))
bill = 0

if height >= 120:
    print("Alright! You can ride the rollercoaster.")

    age = int(input("How old are you?"))
    if age < 12:
        bill = 5
        print("Child bills are $5")
    elif age <=18:
        bill = 8
        print("Youth bills are $8")
    else:
        bill = 12
        print("Adult bills are $12")

    want_photo = input("Do you want an extra photo taken, for memories, (y/n)? ")
    if want_photo == "y":
        bill += 3
        print("That'd be an extra $3")

    snacks = ["popcorn", "burger", "coke", "icecream", "tacos"]
    want_snacks = input("Would you love some snacks too? (y/n) ")
    if want_snacks == "y":
        print("These are the available snacks:", snacks)
        snacks_choice = input("What snack would you like? ")
        if snacks_choice == "popcorn":
            bill += 2
            print("That'd be $2")
        elif snacks_choice == "burger":
            bill += 6
            print("That'd be $6")
        elif snacks_choice == "coke":
            bill += 3
            print("That'd be $3")
        elif snacks_choice == "icecream":
            bill += 5
            print("That'd be $5")
        else:
            bill += 4
            print("That'd be $4")

    print(f"Your total bill is: ${bill}")
else:
    print("Sorry, you're not tall enough to ride the rollercoaster ;)")




