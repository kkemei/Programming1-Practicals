name = input("Enter your name")
while len(name) <= 0:
    print("Invalid entry, please enter a name")
    name = input("Enter your name")

for char in range(0,len(name),2):
    print (char)
print("Your name is:",name)