one =[]
two = []
three = []
def change(x):
    if x == "one":
        a = one
    elif x == "two":
        a = two
    elif x == "three":
        a = three
    return a

n = int(input("Enter the no. of tiles: "))
print("Enter the tiles from bottom to top: ")
for i in range(n):
    a = input()
    one.append(a)
check = one
print(check)
while True:
    print("Elements in one: ", one)
    print("Elements in two: ", two)
    print("ELements in three: ", three)
    if check == three:
        print("You won.")
        break
    b = input("Enter the name of the list from which you want to take out the tile: ")
    c = input("Enter the name of the list to which you want to send the tile: ")
    d = change(b)
    e = change(c)
    f = d.pop()
    g = e.append(f)
