

print("~~~~ Mini Calculator ~~~~")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division")

choice = int(input("Enter your choice number from 1-4: "))

if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 / num2)
    
print("Invalid input values")