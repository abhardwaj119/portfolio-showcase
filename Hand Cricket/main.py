import random

MAX = 6


def win_toss(user_choice):
    while True:
        user_move = int(input("\nYour move: "))

        if user_move < 1 or user_move > MAX:
            print(f"Please choose a number from 1 to {MAX}")
        else:
            print(f"You chose {user_move}")
            break

    comp_move = random.randint(1, MAX)
    print(f"The computer chose {comp_move}")

    if (user_move + comp_move) % 2 == 0:
        result = "Even"
    else:
        result = "Odd"

    if result == user_choice:
        return True
    else:
        return False


def inning(batting):
    runs = 0

    while True:
        while True:
            user_move = int(input("\nYour move: "))

            if user_move < 1 or user_move > MAX:
                print(f"Please choose a number from 1 to {MAX}")
            else:
                print(f"You chose {user_move}")
                break

        comp_move = random.randint(1, MAX)
        print(f"The computer chose {comp_move}")

        if user_move == comp_move:
            print("This inning is over..")
            print(f"\nTotal runs right now: {runs}")
            return runs
        else:
            if batting:
                runs += user_move
            else:
                runs += comp_move
            print(f"Total runs right now: {runs}")


def win_check(bat_score, ball_score):
    if ball_score >= bat_score:
        return "Baller"
    else:
        return "Batsman"


def main():
    print("Welcome to HAND CRICKET!!!\n")
    print("Let's start with a toss..")

    while True:
        user_ch = input("Odd or Even: ").capitalize()
        if user_ch in ["Odd", "Even"]:
            break
        print("Invalid option..")

    if win_toss(user_ch):
        print("You won the toss!!")

        while True:
            play_ch = input("Balling or Batting: ").capitalize()

            if play_ch == "Balling" or play_ch == "Batting":
                print(f"You chose {play_ch}")
                break
            else:
                print("Please choose either Balling or Batting.")

    else:
        print("The computer won the toss..")

        comp_ch = random.choice(["Balling", "Batting"])
        print(f"The computer chose {comp_ch}")

        if comp_ch == "Batting":
            play_ch = "Balling"
        else:
            play_ch = "Batting"

    if play_ch == "Balling":
        target = inning(False)
        final = inning(True)

        print(f"\nYou made {final} runs.")
        print(f"The computer made {target} runs.")

        if win_check(target, final) == "Baller":
            print("You won!!")
        else:
            print("You lost!")

    else:
        target = inning(True)
        final = inning(False)

        print(f"\nYou made {target} runs.")
        print(f"The computer made {final} runs.")

        if win_check(target, final) == "Batsman":
            print("You won!!")
        else:
            print("You lost!")


main()
