import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def result(p1, p2):
    if p1 <=21 and p2 <=21:
        if p2 > p1:
            print("you lose")
        elif p2 < p1:
            print("You Won")
        else:
            print("Draw")
    elif p1>21:
        print("You lose")
    else:
        print("You Won")


def game():
    val1 = random.choice(cards)
    val2 = random.choice(cards)
    print(f"Your cards: [{val1}, {val2}], current score: ", val1 + val2)
    val3 = random.choice(cards)
    val4 = random.choice(cards)
    print("Computer first card:", val3)
    con = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if con == 'y':
        val5 = random.choice(cards)
        print(f"Your final hand: [{val1}, {val2}, {val5}], final score: ", val1 + val2 + val5)
        print(f"Computer final hand: [{val3}, {val4}], final score: ", val4 + val3)
        p1 = val1 + val2 + val5
        p2 = val4 + val3
        result(p1, p2)
        again = input("Do you want to play again?? y or n: ").lower()
        if again == 'y':
            game()
        elif again == 'n':
            print("Thank you have a great day")
        else:
            print("Invalid input")
    elif con == 'n':
        print(f"Your final hand: [{val1}, {val2}], final score: ", val1 + val2)
        print(f"Computer final hand: [{val3}, {val4}], final score: ", val4 + val3)
        p1 = val1 + val2
        p2 = val3 + val4
        result(p1, p2)
        again = input("Do you want to play again?? y or n: ").lower()
        if again == 'y':
            game()
        elif again == 'n':
            print("Thank you have a great day")
        else:
            print("Invalid input")

    else:
        print("Invalid input")

confirm = input("Do you want to play BlackJack ? Y or N: ").lower()
if confirm == 'y':
    game()
elif confirm == 'n':
    print("Thank you have a great day")
else:
    print("Invalid Input")