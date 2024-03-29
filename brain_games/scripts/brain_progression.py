import random
import prompt

def generate_progression():
    start = random.randint(1, 10)
    diff = random.randint(1, 10)
    length = random.randint(5, 10)
    progression = [start + i * diff for i in range(length)]
    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    return progression, str(correct_answer)

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    for _ in range(3):  # Количество вопросов
        progression, correct_answer = generate_progression()
        print("What number is missing in the progression?")
        print("Question:", ' '.join(map(str, progression)))
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print("Let's try again, {name}!")
            break
    else:
        print("Congratulations, {name}!")


if __name__ == "__main__":
    main()
