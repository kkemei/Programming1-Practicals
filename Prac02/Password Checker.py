MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]\<>?{}|"


def main():
    print("Please enter a valid password")
    print("Your password must be between {} and {} characters, and contain:".format(MIN_LENGTH, MAX_LENGTH))
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:

        print("\tand 1 or more special characters: {}".format(SPECIAL_CHARACTERS))
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {} character password is valid: {}".format(str(len(password)),password))


def is_valid_password(password):
    if len(password) <MIN_LENGTH or len(password) >MAX_LENGTH:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower +=1
        elif char.isupper():
            count_upper +=1
        elif char.isdigit():
            count_digit +=1
        elif char in SPECIAL_CHARACTERS:
            count_special +=1
    print("lower: {}".format(count_lower))
    print("upper: {}".format(count_upper))
    print("digit: {}".format(count_digit))
    print("special: {}".format(count_special))
    if count_lower == 0 or count_upper == 0 or count_digit == 0 or (count_special == 0 and SPECIAL_CHARS_REQUIRED):
        return False
    return True

main()