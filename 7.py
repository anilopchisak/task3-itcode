index = -1

# проверка - введенное число положительное
while (index < 0):
    index = int(input("Введите положительное число: "))
    if (index < 0):
        print("\nВведенное вами число отрицательное")

# Числа Фибоначчи
# 1 2 3 4 5 6 7 8   9   10  11  12  13  14
# 0 1 1 2 3 5 8 13 21   34  55  89  144 233
count = 0
list = []
for i in range(index):
    if (len(list) < 2):
        list.append(i)
    else:
        list.append(list[i-1] + list[i-2])

print(list[-1])