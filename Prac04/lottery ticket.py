import random

quick_pics = int(input("How many quick pics?"))
# for num in range(0,quick_pics):

while quick_pics > 0:
    quick_pics -= 1

    list = []
    num1 = [(random.randint(1, 45))]
    list.append(num1[0])
    num2 = [(random.randint(1, 45))]
    if num2 == num1:
        num2 = [(random.randint(1, 45))]
    list.append(num2[0])
    num3 = [(random.randint(1, 45))]
    if num3 == num2:
        num3 = [(random.randint(1, 45))]
    list.append(num3[0])
    num4 = [(random.randint(1, 45))]
    if num4 == num3:
        num4 = [(random.randint(1, 45))]
    list.append(num4[0])
    num5 = [(random.randint(1, 45))]
    if num5 == num4:
        num5 = [(random.randint(1, 45))]
    list.append(num5[0])
    num6 = [(random.randint(1, 45))]
    if num6 == num5:
        num6 = [(random.randint(1, 45))]
    list.append(num6[0])
    list.sort()
    print(list, end=' \n')