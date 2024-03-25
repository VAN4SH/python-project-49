import prompt
import random

def generate_question():
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    correct_answer = str(eval(question))
    return question, correct_answer

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    correct_answers_count = 0
    attempts = 3

    while correct_answers_count < attempts:
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if correct_answers_count == attempts:
        print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()
