def table_multi(table, start=1, end=10):

    tableCounter = start
    print("Table of {}: \n-----------".format(table))
    while tableCounter <= end:
        print(table * tableCounter)
        tableCounter += 1


table_multi(7, 5, 9)
