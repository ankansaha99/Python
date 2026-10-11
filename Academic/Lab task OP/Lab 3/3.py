def my_f(fname,lname):
    print(fname+ " "+lname)

my_f("X","Walker")


def kid(*kids):
    print( kids[2])

kid("x","c","v")


def f(c1,c2,c3):
    print(c3+" "+c2)
f(c1="Emil", c2="Tolis",c3="Haturu")


def mf(**kid):
    print(kid["lname"])

mf(fname="Tobias",lname="Resnes")


def my_fun(cntry="Norway"):
    print("I am From "+ cntry)

my_fun("Usbekistan")
my_fun("Honululu")
my_fun()
my_fun("Mongolia")


def fun(food):
    for x in food:
        print(x)
foods=["Apple","Samsung","Pixel"]

fun(foods)




def xlast(x):
    return 5*x

print(xlast(4))
print(xlast(5))
print(xlast(6))
print(xlast(7))