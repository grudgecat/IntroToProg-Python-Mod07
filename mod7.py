# ---------------------------------------------------------------------------- #
# Title: Assignment 07 (Intro to Pickling and Exception Handling)
# Description: Working with Pickle and Shelf modules
# ChangeLog (Who,When,What):
# Sheri Elgin, 12.03.2021, Created new script
# ---------------------------------------------------------------------------- #

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
