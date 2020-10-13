def is_isogram(string):
    string = [i for i in string.lower().replace('-','').replace(' ','')]
    for i in string:
        lst_count = string.count(i)
        if lst_count > 1:
            return False
    return True