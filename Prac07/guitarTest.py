from Prac07.guitar import Guitar

def main():
    guitars = []
    # while True:
    #     name = input("enter a name")
    #     if name == '':
    #         break
    #     else:
    #         year = int(input("enter what year it was made"))
    #         cost = int(input("enter the cost"))
    # guitars.append(Guitar(name,year,cost))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    counter = 0
    for row in guitars:
        print("Guitar",counter+1,":",guitars[1*counter])
        counter+=1

main()