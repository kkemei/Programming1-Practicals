numItems = int(input("Enter number of items to be shipped"))
x = 1
print(numItems,x)
while x <= numItems:
    x += 1
    price = []
    for i in range(x <= numItems):
        price = input("please enter price of item")
        price.append(i)

print(numItems, price)

