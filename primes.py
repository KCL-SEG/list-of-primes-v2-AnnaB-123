"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):

    #checks if input is positive
    if(number_of_primes <= 0):
        raise ValueError ("Input should be positive")

    list = []
    count = 2
    div = 2

    while (len(list) < number_of_primes):

        if (count % div == 0):
            #checks if itself
            if (count == div):
                list.append(count)
            count += 1
            div = 2
        else:
            div += 1
    return list
