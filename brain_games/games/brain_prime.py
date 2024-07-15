import prompt
from random import randint


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def brain_prime():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(3):
        num = randint(1, 100)
        print(f"Question: {num}")
        user_answer = input("Your answer: ")

        if (user_answer == "yes" and is_prime(num)) or (user_answer == "no" and not is_prime(num)):
            print("Correct!")
        else:
            if is_prime(num):
                correct_answer = "yes"
            else:
                correct_answer = "no"
            print(f'"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
