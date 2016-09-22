from Prac08.taxi import Taxi, UnreliableCar

def main():
    Prius =  Taxi("Prius", 100)
    print(Prius)
    Prius.drive(40)
    Prius.current_fare_distance = 100
    print(Prius)

    dodge = UnreliableCar('dodge', 100)
    print(dodge)
    if dodge.drive(distance=130):
        print('It worked')
    else:
        print("It failed")
    print(dodge)

main()