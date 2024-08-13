import Rectangle
import Circle
import Triangle

print("\tMENU")

#Loop to run program
while True:
    try:
        print("\n1. Area of a circle")
        print("2. Circumference of a circle")
        print("3. Area of a rectangle")
        print("4. Perimeter of a rectangle")
        print("5. Area of a triangle")
        print("6. Perimeter of triangle")
        print("7. Quit")
        print("-------------------------")

        option = int(input("Enter you choice: "))

        #Conditions of choice entered

        if option == 1:
            #AREA OF CIRCLE
            radius = float(input("Enter circle's radius: "))
            print(f"The circle's area is {Circle.area(radius)}")
                  
        elif option == 2:
            #CIRCUMFERENCE OF CIRCLE
            radius = float(input("Enter circle's radius: "))
            print(f"The circle's circumferemce is {Circle.circumference(radius)}")
                  
        elif option == 3:
            #AREA OF RECTANGLE
            length = float(input("Enter rectangle's length: "))
            width = float(input("Enter rectangle's width: "))
            print(f"The rectangle's area is {Rectangle.area(length, width)}")
                  
        elif option == 4:
            #PERIMETER OF RECTANGLE
            length = float(input("Enter rectangle's length: "))
            width = float(input("Enter rectangle's width: "))
            print(f"The rectangle's perimeter is {Rectangle.perimeter(length, width)}")

        elif option == 5:
            #AREA OF TRIANGLE
            base = float(input("Enter triangle's base: "))
            height = float(input("Enter triangle's height: "))
            print(f"The triangle's area is {Triangle.area(base, height)}")

        elif option == 6:
            #PERIMETER OF TRIANGLE
            base = float(input("Enter triangle's base: "))
            length1 = float(input("Enter triangle's first length: "))
            length2 = float(input("Enter triangle's second length: "))
            print(f"The triangle's perimeter is {Triangle.perimeter(length1, length2, base)}")
                            
        elif option == 7:
            #QUITS PROGRAM
            print("--Exiting the program--")
            break
        
        else:
            #IN CASE WRONG VALUE IS ENTERED
            print('Invalid option. Please enter number of choice listed. ')

    except ValueError:
        print('Invalid option. Please enter number of choice listed. ')
