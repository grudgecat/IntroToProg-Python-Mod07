#mod7-exceptions.py

# Using try
try:
    quotient = 5/0
    print(quotient)
except:
    print("You cannot divide by zero. Not being a math god, I don't make the rules, but you can't do this. \n")


# Now, without try
#quotient = 5/0
print('If you repeat the line without the TRY block, the program stops here. Proven, then commented it out to move on. \n')

#Using the exception class to modify error messages to be more readable, including original Python error to demonstrate the difference
try:    
    quotient = 5/0
except ZeroDivisionError as e:
    print("You cannot use zero in the denominator. Please replace the bottom number with a non-zero number and try again.")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')


#Using the exception class to modify error messages to be more readable
try:    
    dictionaryObject = {"id":7, "name":"John"}
    dictionaryObj2 = {"id":3, "name":"Joe"}
    print(dictionaryObject["name"])
    print(dictionaryObj2["namefail"])
except KeyError as e:
    print("Object has no key, please check data and verify key-data pair.")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')

    



