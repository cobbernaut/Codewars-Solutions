def digitize(n):
    array = []
    for digit in str(n):
        array.append(int(digit))
    return(array[::-1])