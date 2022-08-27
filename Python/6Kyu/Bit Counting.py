def count_bits(n):
    binary = bin(n)
    binary = binary[2:]
    ones = 0
    for num in binary:
        if num == "1":
            ones +=1
    return ones
