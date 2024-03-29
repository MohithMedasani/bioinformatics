"""
exercise_02
2/1/2018
"""


def first_elements(my_list, n):

    x=my_list[:n]

    """"
    returns the first n elements in a list.
    EX: first_element([0, 1, 2, 3], 2) should return [0, 1]
    :param my_list: a non-empty list
    :param n: an integer greater than 0
    :return: a list of length n
    """

    return x

result=first_elements([0,1,2,3,3],4)
print(result)

def first_element(my_list, n):

    t =my_list[n:]

    """
    returns the last n elements in a list.
    EX: last_element([0, 1, 2, 3], 2) should return [2, 3]
    :param my_list: a non-empty list
    :param n: an integer greater than 0
    :return: a list of length n
    """

    return t

result2=first_element([0,1,2,3,4],3)

print(result2)


def n_elements(my_list, start, n):
    """
    returns n elements in a list, starting at the position "start".
    EX: n_elements([0, 1, 2, 3, 4, 5], 2, 3) should return [2, 3, 4]
    :param my_list: a non-empty list
    :param start: a non-negative integer
    :param n: an integer greater than 0
    :return: a list of length n
    """
    n=start+n
    return(my_list[start:n])

print(n_elements([0,1,2,3,4,5],2,3))

def count_letters(s):
    dict = {}
    for n in s :
        keys = dict.keys()
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    """
    returns a dictionary containing each letter in s as a key and
    the number of times each letter has occurred as the value
    :param s: a string
    :return: a dictionary
    """
    return dict
print(count_letters('balayya'))



def protein_wight(protein):

    """
    Given a string of amino acids coding for a protein, return the total mass of the protein
    :param protiein: a string containing only G, A, L, M, F, W, K, Q, E, S, P, V, I, C, Y, H, R, N, D, and T
    :return: a float
    """
    AMINO_ACID_WEIGHTS = {'A': 71.04, 'C': 103.01, 'D': 115.03, 'E': 129.04, 'F': 147.07,
                          'G': 57.02, 'H': 137.06, 'I': 113.08, 'K': 128.09, 'L': 113.08,
                          'M': 131.04, 'N': 114.04, 'P': 97.05, 'Q': 128.06, 'R': 156.10,
                          'S': 87.03, 'T': 101.05, 'V': 99.07, 'W': 186.08, 'Y': 163.06}

    n = 0

    for x in protein:
        n = n + AMINO_ACID_WEIGHTS[x]

    return n

print(protein_wight('GALMF'))

