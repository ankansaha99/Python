f1=0
f2=1
fn=0

num=int(input("Enter Number of term : "))
print("Series ",f1," ",f2, end=" ")

for i in range(2,num):
    fn=f1+f2
    print(fn," ")
    f1=f2
    f2=fn

print()