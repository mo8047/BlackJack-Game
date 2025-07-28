import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


u_input = input("Would you like to play?: (y/n)")
while u_input == "y":
    from art import logo
    print(logo)
    user = []
    computer = []
    #Backend
    compile1 = random.choice(cards)
    compile2 = random.choice(cards)
    compile3 = random.choice(cards)
    compile4 = random.choice(cards)
    #compile5 = first user draw
    #compile7 = second user draw
    user.append(compile1)
    user.append(compile3)

    computer.append(compile2)
    computer.append(compile4)
    #sum print
    sum_user = sum(user)
    sum_computer = sum(computer)

    print(f"User cards are {user} and the sum is {sum_user}")
    print(f"Computer's first card is {computer[0]}")
    another_draw = input("Would you like to draw another card: (y/n)")

    if another_draw == "y":
        compile5 = random.choice(cards)
        user.append(compile5)
        sum_user = sum(user)
        print(f"Your cards are: {user} and the sum is :{sum_user}")

        secod_draw = input("Would you like another draw: (y/n)")
        if secod_draw == "y":
            compile7 = random.choice(cards)
            user.append(compile7)
            sum_user = sum(user)
            print(f"Your cards are: {user} and the sum is :{sum_user}")
        elif secod_draw == "n":
            print("Ok")
    elif another_draw == "n":
        print("Fine")

#make sure computer is >17
    while sum_computer < 17:
        computer.append(random.choice(cards))
        sum_computer = sum(computer)

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    if sum_user > 21:
        print("You Bust, Computer wins")
        u_input = ("Play again?: (y/n)")
        continue
    elif sum_computer > 21:
        print(f"Computer Bust, you win")
    elif sum_user == sum_computer:
        print("Draw")
    elif sum_computer > sum_user:
        print(f"Computer wins with a totsl of: {sum_computer}")
    elif sum_user > sum_computer:
        print(f"User wins with a total of: {sum_user}")

    print(f"Computer {sum_computer, computer} User: {sum_user, user}")

    u_input = input("Play again?: (y/n)")

