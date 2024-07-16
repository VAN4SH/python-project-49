import prompt
import random


def is_even(number):
    return number % 2 == 0


def brain_even():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 20)
        print("Question:", number)
        answer = input("Your answer: ")

        if (answer == "yes" and is_even(number)) or (answer == "no" and not is_even(number)):
            print("Correct!")
            correct_answers += 1
        else:
            if is_even(number):
                correct_answer = "yes"
            else:
                correct_answer = "no"
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, correct_answer))
            print("Let's try again, {}!".format(name))
            return
    print("Congratulations, {}!".format(name))
