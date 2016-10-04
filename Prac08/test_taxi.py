from Prac08.taxi import Taxi, UnreliableCar, SilverServiceTaxi

def main():
    Prius =  Taxi("Prius", 100)
    print(Prius)
    Prius.drive(40)
    Prius.current_fare_distance = 100
    print(Prius)

    dodge = UnreliableCar('dodge', 100)
    print(dodge)
    if dodge.drive(130):
        print('It worked')
    else:
        print("It failed")
    print(dodge)

    taxi = SilverServiceTaxi('taxi',200)
    taxi.drive(10)
    print(taxi)

main()