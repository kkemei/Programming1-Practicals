# lowerB = 33
# upperB = 127
# value = input("enter a character:")
# print("The ASCII code for",value,"is",ord(value))
# valueNum = int(input("Enter a number between",lowerB,"and",upperB,":"))
# while valueNum >upperB or valueNum<lowerB:
#     print("Invalid Number, Try again.")
#     valueNum = int(input("Enter a number between",lowerB,"and",upperB,":"))
# print("The character for",valueNum,"is",chr(valueNum))

# lowerB = 33
# upperB = 127
# value = input("enter a character:")
# ordValue = ord(value)
# print("The ASCII code for {} is {}".format(value,ordValue))
# valueNum = int(input("Enter a number between {} and {} :".format(lowerB,upperB)))
# while valueNum >upperB or valueNum<lowerB:
#     print("Invalid Number, Try again.")
#     valueNum = int(input("Enter a number between {} and {} :".format(lowerB, upperB)))
# chrValue = chr(valueNum)
# print("The character for {} is {}".format(valueNum,chrValue))

def main():
    lowerB = 33
    upperB = 127
    value = input("enter a character:")
    ordValue = ord(value)
    print("The ASCII code for {} is {}".format(value,ordValue))
    valueNum = int(input("Enter a number between {} and {} :".format(lowerB, upperB)))
    while get_number(lowerB,upperB,valueNum):
        print("Invalid Number, Try again.")
        valueNum = int(input("Enter a number between {} and {} :".format(lowerB, upperB)))
    chrValue = chr(valueNum)
    print("The character for {} is {}".format(valueNum,chrValue))

def get_number(lowerB,upperB,valueNum):
    # try:
    #     valueNum
    # except ValueError:
    #     print("Numbers must be valid numbers!")
    #     return False
    if valueNum > upperB or lowerB > valueNum:
        return True


main()

# lower = 10
# upper = 100
# print("Enter a number ({}-{}):".format(lower,upper))
# for i in range(10, 120, 11):
#  print("{} {}".format(i, chr(i)))
