n = int(input())

for i in range(n):
    me, him = input().split()
    if me == "R":
        if him == "R":
            print("D")
        elif him == "P":
            print("L")
        else:
            print("W")
    elif me == "P":
        if him == "P":
            print("D")
        elif him == "S":
            print("L")
        else:
            print("W")
    elif me == "S":
        if him == "S":
            print("D")
        elif him == "R":
            print("L")
        else:
            print("W")

