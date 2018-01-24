#!/home/ahurst/env/digital_systems/bin/python
"""This program can help to simplify circuits
"""

import numpy as np


def create_2x2_arrays(num_arrays):
    """This creates a multi-dimensional array of n 2x2 arrays
    Arguments:
        num_var {[int]} -- [this is the number of desired arrays]
    Returns:
        [numpy array] -- [a zero filled n dimensional array with n 2x2 arrays]
    """

    temp_list = [2]

    for temp in range(0, num_arrays):
        temp_list.append(2)

    return np.zeros((temp_list))


if __name__ == "__main__":
    NUM_VAR = int(input("How many inputs do you have: "))
    k_map_array = create_2x2_arrays(NUM_VAR-1)

    user_input = input(
        "Enter 0 to fill a truth table or enter your circuit in the form x+y*z")
    if user_input == "0":
        it = np.nditer(k_map_array, op_flags=[
            'readwrite'], flags=['multi_index'])

        print("(", end='')
        for x in range(0, NUM_VAR):
            print(chr(65+x), end='')
            if x >= NUM_VAR-1:
                print(") | ")
            else:
                print(", ", end='')

        while not it.finished:
            print(str(it.multi_index) + " | ", end='')
            it[0] = input()
            it.iternext()
        print(k_map_array)
    else:
        print("coming shortly, sorry")
