import math

eps = float(input())  # Точность
step = int(input())  # Шаг печати
iterations = int(input())  # Количество итераций
current_summ = 0  # Исходная сумма бесконечного ряда
fin_iter = 0
table = ""
header1 = "№ итерации"
header2 = "t"
header3 = "s"

print("-" * 46)
print(f"|{header1:^14}|{header2:^14}|{header3:^14}|")
print("-" * 46)
for i in range(1, iterations + 1):
    current_element = (2 * i - 1) / (math.sqrt(2) ** i)
    current_summ += current_element
    if i % step == 1:
        table += f"|{i:^14.5g}|{current_element:^14.5g}|{current_summ:^14.5g}| \n"
    if current_element < eps:
        print(table[:-2])
        print("-" * 46)
        print(f"Сумма бесконечного ряда – {(current_summ-current_element):.5g}, вычислена за {i-1} итераций.")
        break
    elif i == iterations:
        print(table[:-2])
        print("-" * 46)
        print("За указанное число итераций необходимой точности достичь не удалось.")
