textFileO = open("name.txt", "w")
name = input("enter your name")
textFileO.write(name)
textFileO.close()

textFileI = open("name.txt", "r")
name = textFileI.read().strip()
print("Your name is", name)
textFileI.close()

numbersFileI = open("numbers.txt", "r")
number1 = int(numbersFileI.readline())
number2 = int(numbersFileI.readline())
print(number1+number2)
numbersFileI.close()

numbersFileI = open("numbers.txt", "r")
total = 0
for line in numbersFileI:
 number = int(line)
 total += number
print(total)
numbersFileI.close()