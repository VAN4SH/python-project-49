import random


TASK = 'What number is missing in the progression?'


def progression_handler(progression):
    indexes = len(progression) - 1
    index = random.randint(0, indexes)
    correct_answer = progression[index]
    progression[index] = '..'
    return correct_answer, progression


def generate_question():
    length = random.randint(5, 10)
    start = random.randint(0, 50)
    step = random.randint(1, 10)
    stop = length * step + start

    li = []

    for i in range(start, stop, step):
        li.append(str(i))

    expression = progression_handler(li)
    return expression


def ask_question(expression):
    correct_answer, progression = expression
    progression = ' '.join(progression)
    print(f'Question: {progression}')


def solve(expression):
    correct_answer, progression = expression
    return correct_answer
