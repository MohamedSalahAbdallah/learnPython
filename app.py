########1##########
# print("first-lesson.py")
########2##########

# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")

########3##########

# # Store some information about a character.
# character_name = "john"
# character_age = 35

# # Print out a message that includes the character's name.
# print("there once was a man named " + character_name)

# # Print out the character's age.
# print("he was "+str(character_age)+" years old")

# # Change the character's name.
# character_name='mike'

# # Print out a message that shows the character's new name.
# print("he really liked the name "+character_name)

# # Print out a message that shows the character's age.
# print("but he didn't like being "+str(character_age))

########4##########


# # Print out the phrase
# phrase = "Python is fun"
# print(phrase)

# # Print out the phrase plus a little extra
# print(phrase + " yay")

# # Print out the phrase in all lowercase letters
# print(phrase.lower())

# # Print out the phrase in all uppercase letters
# print(phrase.upper())

# # Print out the phrase in titlecase: the first letter of each word
# # is capitalized, and the rest of the letters are in lowercase
# print(phrase.capitalize())

# # Print out the phrase with all instances of the substring "fun"
# # replaced with "awesome"
# print(phrase.replace("fun","awesome"))

# # Print out the length of the phrase
# print(len(phrase))

# # Print out the first letter of the phrase
# print(phrase[0])

# # Print out the index of the first occurrence of the letter "f" in
# # the phrase
# print(phrase.index("f"))

# # Print out the index of the first occurrence of the letter "f" in
# # the phrase. If the letter is not found, print out -1
# print(phrase.find("f"))

# # Print out the number of times the letter "f" appears in the phrase
# print(phrase.count("f"))


########5##########

# # Import all functions from the math module
# #
# # The math module is a built-in module that contains a variety of
# # mathematical functions. By importing all of them, we can use any
# # of the functions in our code without having to prefix them with
# # "math." (as in "math.sqrt" instead of just "sqrt").
# from math import *

# # Add two numbers and print the result
# print(2+3)

# # Subtract one number from another and print the result
# print(3-2)

# # Multiply two numbers and print the result
# print(3*2)

# # Divide one number by another and print the result
# print(3/2)

# # Raise one number to the power of another and print the result
# print(3**2)

# # Get the remainder of one number divided by another and print the result
# print(3%2)

# # Divide one number by another and round down to the nearest whole number.
# # Print the result.
# print(3//2)

# # Print the absolute value of a number
# # The absolute value of a number is the distance of that number from zero.
# # The absolute value of a negative number is positive.
# # For example, the absolute value of -888 is 888.
# print(abs(-888))

# # Print the rounded value of a number
# # The rounded value of a number is the number with the decimal part chopped off.
# # If the number is halfway between two whole numbers, it rounds up to the larger number.
# # For example, the rounded value of 3.7 is 4.
# print(round(3.7))

# # Print the result of raising one number to the power of another
# # The result of raising 3 to the power of 2 is 3 times 3, or 9.
# print(pow(3,2))
# # Get the maximum of two numbers and print the result
# # The maximum of two numbers is the larger of the two numbers.
# print(max(5, 12))

# # Get the minimum of two numbers and print the result
# # The minimum of two numbers is the smaller of the two numbers.
# print(min(5, 12))

# # Get the sum of multiple numbers and print the result
# # The sum of multiple numbers is the result of adding them all up.
# print(sum([5, 12]))

# # Get the floor of a number and print the result
# # The floor of a number is the largest whole number that is smaller than or equal to the number.
# # For example, the floor of 3.7 is 3.
# print(floor(3.7))

# # Get the ceiling of a number and print the result
# # The ceiling of a number is the smallest whole number that is larger than or equal to the number.
# # For example, the ceiling of 3.7 is 4.
# print(ceil(3.7))

# # Get the square root of a number and print the result
# # The square root of a number is the number that, when multiplied by itself, gives the number.
# # For example, the square root of 36 is 6, because 6 times 6 is 36.
# print(sqrt(36))


########6##########

# # Ask the user for their name and age
# name = input("What is your name? ")
# age = input("How old are you? ")

# # Print out a message that greets the user and tells them their age
# # The message is constructed by concatenating the following strings:
# # 1. "Hello "
# # 2. The user's name
# # 3. " You are "
# # 4. The user's age
# # 5. " years old."
# print("Hello " + name + "! You are " + age + " years old.")


########7##########

# # Prompt the user to enter a number and convert the input from a string to a float.
# # This allows the user to enter decimal numbers and not just whole numbers.
# num1 = float(input("Enter a number: "))

# # Prompt the user to enter a mathematical operator (+, -, *, or /).
# # This is used to determine the operation to perform on the two numbers.
# sign = input("Enter an operator: ")

# # Prompt the user to enter another number and convert the input from a string to a float.
# # This is the second number that will be used in the operation with the first number.
# num2 = float(input("Enter another number: "))

# # This is a "match statement" that checks the value of the variable sign.
# # It is a more concise way of writing a series of if/elif statements.
# match sign:
#     # If the value of sign is "+", add num1 and num2 and print the result.
#     case "+":
#         print(num1 + num2)
#     # If the value of sign is "-", subtract num2 from num1 and print the result.
#     case "-":
#         print(num1 - num2)
#     # If the value of sign is "*", multiply num1 and num2 and print the result.
#     case "*":
#         print(num1 * num2)
#     # If the value of sign is "/", divide num1 by num2 and print the result.
#     # If num2 is 0, print "Cannot divide by zero".
#     case "/":
#         if num2 == 0:
#             print("Cannot divide by zero")
#         else:
#             print(num1 / num2)
        

########8##########

# color= input("Enter a color: ")
# plural_noun = input('Enter a plural noun: ')
# celebrity = input('Enter a celebrity: ')

# print('roses are ' + color)
# print( plural_noun + ' are blue')
# print('I love ' + celebrity)


########9##########
# # A list of my lucky numbers
# lucky_number = [5,7,8,1,6,8,4]

# # A list of my friends' names
# friends=['bob','joe','sally','mike','oscar']

# # Print out the list of friends
# print(friends)

# # Print out the first friend in the list
# print(friends[0])
# # Print out the second friend in the list
# print(friends[1])
# # Print out the third friend in the list
# print(friends[2])

# # Print out the last friend in the list
# print(friends[-1])
# # Print out the second-to-last friend in the list
# print(friends[-2])
# # Print out the third-to-last friend in the list
# print(friends[-3])

# # Print out all the friends from the second one onward
# print(friends[1:])
# # Print out the second, third, and fourth friends in the list
# print(friends[1:4])

# # Combine the lists of friends and lucky numbers
# friends.extend(lucky_number)
# # Print out the combined list
# print(friends)

# # Add a new friend named "jackson" to the list
# friends.append('jackson')
# # Print out the updated list
# print(friends)

# # Insert a new friend named "jackson" at the second position in the list
# friends.insert(1,'jackson')
# # Print out the updated list
# print(friends)

# # Remove the first occurrence of "jackson" from the list
# friends.remove('jackson')
# # Print out the updated list
# print(friends)

# # Remove the last element from the list
# friends.pop()
# # Print out the updated list
# print(friends)

# # Remove the element at the second position from the list
# friends.pop(1)
# # Print out the updated list
# print(friends)

# # Clear the list of friends
# friends.clear()
# # Print out the cleared list
# print(friends)

# # Find the index of the first occurrence of "bob" in the list
# print(friends.index('bob'))

# # Count the number of occurrences of "bob" in the list
# print(friends.count('bob'))

# # Sort the list of friends
# friends.sort()
# # Print out the sorted list
# print(friends)

# # Reverse the order of the list of friends
# friends.reverse()
# # Print out the reversed list
# print(friends)

# # Make a copy of the list of friends
# friends2 = friends.copy()
# # Print out the copy
# print(friends2)


########10##########

# coordinates = (1,2)
# print(coordinates)
# print(coordinates[0])
# print(coordinates[1])

########11##########

def say_hi(name):
    print("Hi "+name)
    
    
say_hi(input("Enter a name: "))