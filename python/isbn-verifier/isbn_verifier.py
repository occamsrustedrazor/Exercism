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

    #Check if "X" existed anywhere except -1 and that there are only 10 digits
    if 10 in num_list[:-2] or len(num_list) != 10:
        return False

    # Validate Checksum
    if (num_list[0] * 10 + num_list[1] * 9 + num_list[2] * 8 + 
        num_list[3] * 7 +  num_list[4] * 6 + num_list[5] * 5 + 
        num_list[6] * 4 +  num_list[7] * 3 + num_list[8] * 2 + 
        num_list[9] * 1) % 11 == 0:
        return True
    else:
        return False