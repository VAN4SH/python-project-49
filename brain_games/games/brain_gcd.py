import random
import math


TASK = "Find the greatest common divisor of given numbers."


def generate_question():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    question = (number1, number2)
    correct_answer = math.gcd(number1, number2)
    return question, str(correct_answer)
