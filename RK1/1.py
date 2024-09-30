eps = float((input()))
x = int(input())
summ = 0
prev_num = 0
current_num = 0
n = 0

while abs(prev_num - current_num) > eps or n == 0:
    prev_num = current_num
    factorial = 2 * n + 1
    for i in range(2, n+1):
        factorial *= i
    current_num = ((-1) ** (n - 1)) * ((x * (2 * n + 1)) / factorial)
    summ += current_num
    n += 1
print(summ)
