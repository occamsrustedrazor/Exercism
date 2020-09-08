def is_armstrong_number(number):
    # Create list of individual digits
    individuals = [int(i) for i in str(number)]
    result = 0

    # Get each digit exponent result and sum them
    for i in range(len(individuals)):
        result += individuals[i] ** len(individuals)
    
    # Compare
    if number == result:
        return True
    else:
        return False