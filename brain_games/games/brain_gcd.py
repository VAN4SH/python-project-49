import prompt
import random

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def brain_gcd():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    for _ in range(3):
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)

        print(f"Question: {num1} {num2}")
        user_answer = int(input("Your answer: "))
        correct_answer = gcd(num1, num2)

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
