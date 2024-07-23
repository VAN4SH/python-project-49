import prompt

DEFAULT_ROUNDS = 3


def welcome_user():
    print("Welcome to the Brain games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def ask_question(question):
    if isinstance(question, tuple):
        if len(question) == 2:  # For games like brain-gcd
            number1, number2 = question
            print(f"Question: {number1} {number2}")
        elif len(question) == 3:  # For games like brain-calc
            number1, operation, number2 = question
            print(f"Question: {number1} {operation} {number2}")
    elif isinstance(question, list):
        progression = " ".join(question)
        print(f"Question: {progression}")
    else:
        print(f"Question: {question}")


def play(game):
    name = welcome_user()
    print(game.TASK)
    game_rounds = DEFAULT_ROUNDS

    while game_rounds:
        question, correct_answer = game.generate_question()
        ask_question(question)
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            game_rounds -= 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
