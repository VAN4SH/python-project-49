import random
import operator


TASK = 'What is the result of the expression?'


def generate_question():
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    operation = random.choice(list(operations.keys()))
    question = (number1, operation, number2)
    correct_answer = operations[operation](number1, number2)
    return question, str(correct_answer)


