def classify(number):
    factors = []
    if (number + 1) < 2:
        raise ValueError("Not a natural number!")
    for i in range(1,number):
        if number % i == 0:
            factors.append(i)
    if sum(factors) == number:
        return "perfect"
    elif sum(factors) > number:
        return "abundant"
    else:
        return "deficient"