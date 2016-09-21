def main():
    numbers = []
    for i in range(0, 5):
        num_value = int(input("Enter a number? "))
        numbers.append(num_value)

    print("the first number is {}".format(numbers[0]))
    print("the last number is {}".format(numbers[4]))
    print("the smallest number is {}".format(min(numbers)))
    print("the largest number is {}".format(max(numbers)))
    print("the average number is {}".format(sum(numbers)/len(numbers)))

main()
