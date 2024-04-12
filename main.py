def pattern1(num_of_numbers):
    """
    1
    2 2
    3 3 3
    4 4 4 4
    """
    for i in range(1,num_of_numbers + 1):
        for j in range(i):
            print(i, end = " ")
        print("\n")




pattern1(4)
