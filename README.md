# IntroToProg-Python-Mod07
## Review of pickling and Unpickling files, and Exception Handling

 Data serialization allows converting complex data structures into a linear form that has improved storage to disk and potentially faster transmission over a network. Serialized data is not human readable so you need a way to reverse the process to restore the file to human readable form. In a nutshell, pickling refers to serializing data while unpickling refers to deserializing data, both using Python's "Pickle module."

 The Pickle module uses the picke.dump() method to write pickled data to a file, and the pickle.load() method to reverse the process and restore the data to its original format. Both methods take the file name and the data to transform as an argument.

 In order to use the Pickle module, it must be imported. 

 An example script, using simple lists and these methods follows:

```
# Intro to pickling/unpickling files

#import the pickle module
import pickle

#file to read/write to
filmCollection = 'filmcollection.txt'

#data = 3 lists to pickle/unpickle
genre = ["comedy", "scifi", "horror", "drama", "documentary"]
country = ["USA", "Germany", "France", "Italy", "Japan", "China"]
filmFormat = ["VCR", "DVD", "BluRay", "Streaming"]

#print before pickling
print("*** LISTS BEFORE PICKLING ***")
print(genre)
print(country)
print(filmFormat)

#open file to store lists as pickeld file
f = open(filmCollection, "wb")

#pickle each list to file
pickle.dump(genre, f)
pickle.dump(country, f)
pickle.dump(filmFormat, f)

#close open file stream
f.close()

#verify list is in serialized format - check

# unpickle the lists

#open file
f = open(filmCollection, "rb")

#unpicke each list, restore to original variable/format
genre = pickle.load(f)
country = pickle.load(f)
filmFormat = pickle.load(f)

#verify it worked
print("*** LISTS AFTER UNPICKLING ***")
print(genre)
print(country)
print(filmFormat)

#close file stream
f.close()
```

---

## Using Exception class to improve error handling
Python has a built-in class that provides information when errors occur. Any time an error occurs, Python creates a new Exception object with information about the error.

Using the try-except block formatting allows the programmer to capture this information, and modify it as needed.

Providing an except clause with a message allows you to overwrite unfriendly/confusing Python messages with more human friendly messages. As an example, the code below shows what the user will see if they attempt to divide by zero. Using the 'print' opiton in the except block allows the programmer to present their own version of the error message. Additionally, by adding the exception type, in this case 'ZeroDivisionError', you can capture only this error type and connect it to your custom error message.

Sample code demonstrates how the try-except function works:

```
# Using try
try:
    quotient = 5/0
    print(quotient)
except:
    print("You cannot divide by zero. Not being a math god, I don't make the rules, but you can't do this. \n")


# Now, without try
#quotient = 5/0  #MUST COMMENT THIS OUT TO GET CODE TO CONTINUE RUNNING OR IT STOPS WHEN ERROR IS ENCOUNTERED!!!
print('If you repeat the line without the TRY block, the program stops here. Proven, then commented it out to move on. \n')


#Using the exception class to modify error messages to be more readable, including original Python error to demonstrate the difference
try:    
    quotient = 5/0
except ZeroDivisionError as e:
    print("You cannot use zero in the denominator. Please replace the bottom number with a non-zero number and try again.")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
```

***OUTPUT IS:***
```
You cannot divide by zero. Not being a math god, I don't make the rules, but you can't do this.

If you repeat the line without the TRY block, the program stops here. Proven, then commented it out to move on.

You cannot use zero in the denominator. Please replace the bottom number with a non-zero number and try again.
Built-In Python error info:
division by zero
Second argument to a division or modulo operation was zero.
<class 'ZeroDivisionError'>
```

---

Another example of modifying error output for a specific exception type is capturing the 'KeyError' exception type. This is an error that is thrown when a bad key is provided to a dictionary type. This error type, and its associated Python error, and custom error is shown the example below:

```
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
```

***OUTPUT IS:***
```
John
Object has no key, please check data and verify key-data pair.
Built-In Python error info:
'namefail'
Mapping key not found.
<class 'KeyError'>
(venv)
```