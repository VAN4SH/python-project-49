import random


TASK = "Answer 'yes' if given number is prime. Otherwise answer 'no'."


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_question():
    number = random.randint(0, 100)
    question = number
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
