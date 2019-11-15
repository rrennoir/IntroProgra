def table_multi(table, start=1, end=10):

    i = start
    print("Table of {}: \n-----------".format(table))
    while i <= end:

        print(table * i)
        i += 1


table_multi(7, 5, 9)
