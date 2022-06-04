with open('estructura_datos/diccionarios/temps.dat') as f:
    for line in f:
        max_temp, min_temp = line.strip().split()
        print(max_temp, min_temp)

