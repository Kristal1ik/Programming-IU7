ls = [10, 1, 0, 2, 7, 10, 3, 5, 6, 3, 1, 2, 9, 8, -1, -2]
n, i = len(ls), 0

while True:
   flag = 0
   for j in range(i, n - 1 - i): # пузырёк
      if ls[j] > ls[j + 1]:
          ls[j], ls[j + 1] = ls[j + 1], ls[j]
          flag = 1
   if flag == 0: # массив упорядочен
      break
   i += 1
   flag = 0
   for j in range(n - 1 - i, i - 1, -1): # шарик
      if ls[j - 1] > ls[j]:
          ls[j], ls[j - 1] = ls[j - 1], ls[j]
          flag = 1
   if flag == 0: #массив упорядочен
      break

print(*ls)