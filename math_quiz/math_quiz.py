import random


def generate_random_integer(min_Val, max_Val):
    """
    Generate a random integer between min_Val and max_Val.

    Args:
        min_Val (int):  min Val for the random integer.
        max_Val (int):  max Val for the random integer.

    Returns:
        int: A random integer between min_Val and max_Val.
    """
    try:
        # Check if min_Val and max_Val are integers
        if not isinstance(min_Val, int) or not isinstance(max_Val, int):
            raise ValueError("min_Val and max_Val must be integers.")
        
        # If they are integers, generate random integers
        return random.randint(min_Val, max_Val)
    
    except ValueError as e:
        # If they are not integers, catch the exception and assign some default random values
        print(f"Error: {e}")
        print("Assigning default random values.")
        return random.randint(1, 5)



def generate_random_operator():
    """
    Generates a random operator: '+', '-', or '*'.

    Returns:
        str: A random selected operator.
    """

    return random.choice(['+', '-', '*'])


def add_sub_mul(number1, number2, operator):
    """
    Performs the Add or Sub operation based on the given operator.

    Args:
        number1 (int): The first operand.
        number2 (int): The second operand.
        operator (str): ('+', '-', or '*').

    Returns:
        tuple: A tuple containing the problem string and the correct answer.
    """

    problem = f"{number1} {operator} {number2}"
    if operator == '-': result = number1 - number2
    elif operator == '+': result = number1 + number2
    else: result = number1 * number2
    return problem, result

def math_quiz():
    points = 0
    Num_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(Num_questions):
        n1 = generate_random_integer(1, 10); n2 = generate_random_integer(1, 5.5); o = generate_random_operator()



        PROBLEM, ANSWER = add_sub_mul(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            points += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {points}/{Num_questions}")

if __name__ == "__main__":
    math_quiz()
