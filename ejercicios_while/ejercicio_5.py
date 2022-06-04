p = 5
sum = 0
count = 0

while p > 0:
    count += 1
    f = int(input("Enter the number "))
    sum += f
    p -= 1
  
average = sum/count
print("Average of given Numbers:",average)