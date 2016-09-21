def get_number(lowerB,upperB,valueNum):
    if valueNum > upperB or lowerB > valueNum:
        return True
    # try:
    #     valueNum
    # except ValueError:
    #     print("Numbers must be valid numbers!")
    #     return False


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

main()
