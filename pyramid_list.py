"""function to print a pyramid using lists"""
def pyramid_list(n):
    myList = []
    for i in range(1, n+1):
        myList.append("*"*i)
    print("\n".join(myList))

    n = 4
    pyramid_list(n)