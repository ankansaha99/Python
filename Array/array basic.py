arr = ["A","R","R","A","Y"]

for i in arr:
    print(i)

size = int(input("Enter Array Size : "))

arr2=[]

for i in range(size):
    value= int(input(f"Enter number at index [{i}] : "))
    arr2.append(value)

    
for j in arr2:
    print(j)