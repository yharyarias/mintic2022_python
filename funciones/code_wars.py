def grow(arr):
    cont = 1
    
    for i in arr:
        print(i)
        cont *= i
        print(cont)
    return cont


print(grow([1, 2, 3]))