marks = input("marks:")  # Get input from the user

# Convert the input to an integer, and add error handling
try:
    marks = int(marks)  # Try to convert the input to an integer
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    exit()  # Exit the program if the input is not a valid integer

# Check the marks and print the corresponding grade
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("D")