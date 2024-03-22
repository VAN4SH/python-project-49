from brain_games.cli import welcome_user
import random


def is_even(number):
    return number % 2 == 0

def main():
    print("Welcome to the Brain Games!")
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1,20)
        print("Question:", number)
        answer = input("Your answer: ")

        if (answer == "yes" and is_even(number)) or (answer == "no" and not is_even(number)):
            print("Correct!")
            correct_answers += 1
        else:
            if is_even(number):
                correct_answer = "no"
            else:
                correct_answer = "yes"
            print(" '{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, correct_answer))
            print("Let's try again, {}!".format(name))
            return
    print("Congratulations, {}!".format(name))

if __name__ == "__main__":
    main()
