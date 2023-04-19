num = -1

# проверка - введенное число положительное
while (num < 0):
    num = float(input("Введите положительное число: "))
    if (num < 0):
        print("\nВведенное вами число отрицательное")

if (num % 2 == 0 or num % 3 == 0) and num != 2 and num != 3:
    print("\nСоставное")
else:
    print("\nПростое")