import random
val = [
    {
        "name": "Arun",
        "age" : 24
    },
    {
        "name": "Belle",
        "age": 25
    },
    {
        "name": "Honey",
        "age": 69
    },
    {
        "name": "Bhuji",
        "age": 96
    },
    {
        "name": "Baby",
        "age": 6
    }
]
count = 0
a = 0
flag1 = True
for a in range(0,4):
    try:
        if flag1 == True:
            ans = random.choice(val)
        ans1 = random.choice(val)
        flag = True
        if ans == ans1:
            while flag:
                ans1 = random.choice(val)
                if ans == ans1:
                    flag = True
                else:
                    flag = False
        print(f"Compare A: {ans["name"]}")
        print("----------VS-----------------")
        print(f"Compare B: {ans1["name"]}")
        ans2 = input("Who is older ? A or B : ").lower()
        if ans2 == 'a'and ans["age"] > ans1["age"]:
            count += 1
            print(f"You are correct, current score is {count}")
            flag1 = False
        elif ans2 == 'b' and ans1["age"] > ans["age"]:
            count += 1
            print(f"You are correct, current score is {count}")
            flag1 = False
        else:
            print(f"You lost, Your are score is {count}")
            break
    except IndexError:
        print("Game over")
        break