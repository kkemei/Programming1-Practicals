numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


# Q1) It will occur when the numerator is lower than the denominatior
# Q2) This will occur when the denominator is 0
# Q3) Yes, by creating a error checker


