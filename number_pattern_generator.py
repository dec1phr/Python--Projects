def number_pattern(n):
    if ((isinstance(n,int)) != 1):
        return "Argument must be an integer value."
    if (n < 1):
        return "Argument must be an integer greater than 0."
    numbers = ""
    for number in range(1, n+1):
        numbers += str(number) + " "
    
    return numbers.strip()

print(number_pattern(4))
