def get_name():
    global name
    name = input("Enter your name")
    return name


def print_loop(name,step):
    for i in range(0, len(name), step):
        print(name[i])
    print("Your name is:", name)


def main():
    name = get_name()
    while len(name) <= 0:
        print("Invalid entry, please enter a name")
        name = input("Enter your name")

    print_loop(name,3)


main()
