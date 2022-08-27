def no_odds(values):
    even = []
    for value in values:
        if value %2 == 0:
            even.append(value)
    return even