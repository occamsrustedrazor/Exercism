import numpy as np

def square_of_sum(number):
    return np.square(sum(create_num_array(number)))
    # Without NumPy:
    # return sum(create_num_array(number)) ** 2

def sum_of_squares(number):
    return sum(np.square(create_num_array(number)))
    # Without NumPy:
    # return sum([i ** 2 for i in create_num_array(number)])

def difference_of_squares(number):
    return (square_of_sum(number) - sum_of_squares(number))

def create_num_array(number):
    return [i+1 for i in range(number)]