from Prac07.guitar import Guitar

def main():

    # while True:
    #     name = input("enter a name")
    #     if name == '':
    #         break
    #     else:
    #         year = int(input("enter what year it was made"))
    #         cost = int(input("enter the cost"))
    # guitars.append(Guitar(name,year,cost))

    Gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    Line = Guitar("Line 6 JTV-59", 2010, 1512.9)
    guitars = [Gibson, Line]


    counter = 0
    for i, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(Vintage)"
        # print("Guitar", counter + 1, ":", guitars[counter])
        # counter += 1
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1,guitar.name, guitar.year, guitar.cost, vintage_string))
        i += 1

main()