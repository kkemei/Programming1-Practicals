from Prac08.taxi import Taxi, UnreliableCar, SilverServiceTaxi


def main():
    # Prius =  Taxi("Prius", 100)
    # print(Prius)
    # Prius.drive(40)
    # Prius.current_fare_distance = 100
    # print(Prius)
    #
    # dodge = UnreliableCar('dodge', 100)
    # print(dodge)
    # if dodge.drive(130):
    #     print('It worked')
    # else:
    #     print("It failed")
    # print(dodge)
    #
    # taxi = SilverServiceTaxi('taxi',200,4)
    # taxi.drive(10)
    # print(taxi)
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0

    menu_choice = get_menu()

    while menu_choice != "q":
        if menu_choice == "c":
            taxi_choice = run_taxi_choice(taxis)
            print("Bill to date: ${:.2f}".format(bill))
            menu_choice = get_menu()
        elif menu_choice == "d":
            bill = run_drive(bill, taxi_choice)
            menu_choice = get_menu()
    print("Total trip cost: ${:.2f}".format(bill))
    print("Taxis are now:")
    counter = 0
    for taxi in taxis:
        print(counter, "-", taxis[counter])
        counter += 1


def get_menu():
    menuOptions = ['q', 'c', 'd']
    print("Let's drive!")
    menu_choice = input("q)uit, c)hoose taxi, d)rive")
    while menu_choice not in menuOptions:
        print("incorrect answer try again")
        menu_choice = input("q)uit, c)hoose taxi, d)rive")
    return menu_choice


def run_taxi_choice(taxis):
    counter = 0
    print("Taxis available: ")
    for taxi in taxis:
        print(counter, "-", taxis[counter])
        counter += 1
    choose_taxi = int(input("Choose taxi:"))
    taxi_choice = taxis[choose_taxi]
    return taxi_choice


def run_drive(bill, taxi_choice):
    distance = int(input("Drive how far? "))
    taxi_choice.drive(distance)
    fare = taxi_choice.get_fare()
    bill += fare
    print(
        "Your {} trip cost you ${:.2f}".format(taxi_choice.name, fare))
    print("Bill to date: ${:.2f}".format(bill))
    return bill


main()
