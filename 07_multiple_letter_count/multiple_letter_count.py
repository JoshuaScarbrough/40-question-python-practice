def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # for num in range(0, len(phrase)):
    #     print(phrase[num])

    # 

    # Making an empty dictionary 
    counter = {}

    # Iterates through the phrase by each letter
    for ltr in phrase:
        print(ltr)
        # counter[p] = counter.get(p,)
        counter[ltr] = counter.get(ltr, 0) + 1

    return counter

