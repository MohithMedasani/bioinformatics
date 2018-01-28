"""
Exercise 1
Place this script inside a new folder in your github repository called "Exercises".
This will be the directory for all of your in-class exercises this semester.

By the end of class on Thursday 1/25, students should have:
    - Created a private github repo for this class
    - Added their information to this sheet:
        https://docs.google.com/spreadsheets/d/1EKNYOqTnxelmBT4jqotRbUer5eVvWYM9RloN5doScyo/edit?usp=sharing
    - Added my github account (kylelevi) as a collaborator for their private repository
    - Completed these definitions and pushed this script to a folder called "Exercises" in their repo

"""


def hello():
    print("Hello world")
    """
    Print "Hello World"
    :return: None
    """
    return


hello()


def percent_decimal(i):
    if i > 1:
        i = i/100
        print(i)
    else:
        i = i * 100
        print(i)

    """
    Converts a percentage to a decimal or a decimal to a percentage depending on the input i
    :param i: a float between 0 and 100
    :return: a float between 0 and 100
    """

    return

percent_decimal(0.1)


def exponent(integer, power):
    var = integer
    power = power - 1
    for i in range(power):
        integer = integer * var
    print(integer)
    """
    Using a loop (no imports!), raise the integer given to the power provided. (integer^power)
    :param integer: a positive, non zero, integer
    :param power: a positive, non zero, integer
    :return: an integer
    """
    return (integer, power)


exponent(2, 5)


def complement(dna):
    temp_string = ''
    for s in dna:
        if s == 'C':
            temp_string += 'G'
        elif s == "A":
            temp_string += 'T'
        elif s == "T":
            temp_string += 'A'
        elif s == "G":
            temp_string += 'C'
        else:
            temp_string += s

    return temp_string

    """
    Returns the complement strand of DNA to the input.  C <--> G,  A <--> T
    :param dna: String containing only C, T, A, and G
    :return: String containing only C, T, A, and G
    """

print(complement('CTAG'))