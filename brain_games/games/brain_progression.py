import random


TASK = 'What number is missing in the progression?'


def generate_question():
    start = random.randint(0, 50)
    step = random.randint(1, 10)
    length = 10
    progression = [str(start + i * step) for i in range(length)]
    missing_index = random.randint(0, length - 1)
    correct_answer = progression[missing_index]
    progression[missing_index] = '..'
    question = progression
    return question, correct_answer
