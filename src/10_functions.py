# Write a function is_even that will return true if the passed-in number is even.

def even(number):
    if number % 2 == 0:
        return True
    else:
        return False


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

if even(num) == True:
    print("Even!")
else:
    print("Odd")

