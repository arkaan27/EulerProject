# Problem 1:

# Problem statement

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples(y, x):
    """
    Puts all the multiples of y below x in a list and returns the list
    :param y: The multiple number
    :param x: The number till you count the multiples of y
    :return multiple_list: List of all the multiples of y below x
    """
    multiple_list = []
    for number in range(0, x):
        if number % y == 0:
            multiple_list.append(number)

    return multiple_list


if __name__ == '__main__':

    # Calculates the multiples of 3 & 5
    multiple_list_3 = multiples(3, 1000)
    multiple_list_5 = multiples(5, 1000)

    # Sums all the numbers present in the list
    total_sum = sum(multiple_list_3) + sum(multiple_list_5)

    # Prints the sum
    print(total_sum)
