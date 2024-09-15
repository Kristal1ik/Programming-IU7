n, k = map(int, input().split())
unallowed = input().split()


def check(number):
    number_str = str(number)
    for i in range(k):
        if unallowed[i] in number_str:
            return False
    return True


while not(check(n)):
    n += 1
print(n)
