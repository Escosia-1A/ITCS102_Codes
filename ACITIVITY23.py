# mamaya ka

# JEepney simulator (Interactive)
route = ["Terminal","Perez park", "Pacific mall"]
passengers = []
Seats = 8 
fare = 14 
total = 0 

while True:
    print()
    print("Sakay: ", passengers)
    print(len(passengers), "of", Seats, "seats")
    print("2 Sakay 4 Priority seat 2 Para po!")
    print("4 Baba sa pinto 4 Baba sa harap")
    print("6 seat check 7 balikan 8 exit")
    choice = input("Choice: ")

    if choice == "1":
        if len(passengers) == Seats:
            print("Puno na!")
        else:
            name = input("Name: ")
            passengers.append(name)
            total = total + fare
            print(name, "already seated")

    elif choice == "2":
            if len(passengers) == Seats:
                print("Puno na!")
            else:
                name = input("Name: ")
                passengers.insert(0, name)
                total = total + fare
                print(name, "took the priority seat.")

    elif choice == "3":
            name = input("Who is getting off? ")
            if name in passengers:
                passengers.pop(name)
                print(name, "just got off the Jeep")
            else:
                print("name, is not on the Jeep.")

    elif choice == "4":
            if len(passengers) == 0:
                print("The jeep is empty.")
            else:
                front = passengers.pop(0)
                print(front, "got off at the front.")

    elif choice == "5":
                if len(passengers) == 0:
                    print("The jeep is empty.")
                else:
                    front = passengers.pop(0)
                    print(front, "got off at the front.")

    elif choice == "6":
            for i in range(len(passengers)):
                 print("seat", i + 1, passengers[1])

    elif choice == "7":
            route.reverse()
            print("Route: ", route)

    elif choice == "8":
            print("Total fare today: ", total)
            break
    else:
            print("Invalid Choice.")


    
    



