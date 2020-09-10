def is_valid(isbn):
    # Pre Process - remove hyphens, remove non-X alpha, convert X to 10, 
    # convert strings to integers in a list.
    num_list = []
    for i in isbn:
        if i == '-':
            pass
        elif i.isalpha() and i != "X":
            return False
        elif i == "X":
            num_list.append(10)
        else: 
            num_list.append(int(i))

    #Check if "10" exists anywhere except -1 and that there are only 10 numbers
    if 10 in num_list[:-2] or len(num_list) != 10:
        return False

    # Validate Checksum
    total = 0
    for i in range(10):
        total += num_list[i] * (10-i)
    return total % 11 == 0
