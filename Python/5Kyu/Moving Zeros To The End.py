def move_zeros(lst):
    for number in lst:
        if number == 0:
            lst.remove(number)
            lst.append(0)
        else:
            continue
            
    return lst