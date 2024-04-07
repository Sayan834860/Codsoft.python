import random
user_score=0
computer_score=0

while True:

    user=input("Enter your choice(rock,paper,scissors): ")
    possible=['rock','paper','scissors']
    computer=random.choice(possible)
    print(f"\nyou chose {user},computer chose {computer}.\n")

    if user == computer:
        print(f"Both are chose same {user},{computer}.it is tie!")

    elif user=='rock':
        if computer=='paper':
            print("you lose!")
            computer_score=computer_score+1
        else:
            print("you win!")
            user_score=user_score+1

    elif user=='paper':
        if computer=='scissors':
            print("you lose!")
            computer_score=computer_score+1
        else:
            print("you win!")
            user_score=user_score+1

    elif user=='scissors':
        if computer=='rock':
            print("you lose!")
            computer_score=computer_score+1
        else:
            print("you win!")
            user_score=user_score+1
    else:
        print("invalid string")

    play_again = input("You want to play anymore(yes/no/score):")
    while play_again not in'(yes/no/score)':
        play_again = input("You want to play anymore(yes/no/score):")
    if play_again == 'no':
        print("Ok! Thanks for playing")
        print(f"user_score={user_score},\ncomputer_score={computer_score}")
        break
    elif play_again == 'yes':
        print("ok! play now: ")
    elif play_again == 'score':
            print(f"user score={user_score},\ncomputer_score={computer_score}")

    else:
        print("please put the currect value..")