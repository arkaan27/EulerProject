# Problem 1:

# Problem statement

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def compute(y, z, x):
    """
    Checks for all the multiples of y and z below x and sums the multiples
    :param y: The multiple number
    :param z: The second multiple number
    :param x: The number till you count the multiples of y and z
    :return answer: The sum of multiples of y and z below x
    """
    answer = 0
    for number in range(0, x):
        if number % y == 0 or number % z == 0:
            answer += number

    return answer


if __name__ == '__main__':
    print(compute(3, 5, 1000))

    ## answer is 233168
