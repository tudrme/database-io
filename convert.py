# Converts v1 to v2 in Python

# Imports
import json
import random
import string

# Home Directory
home = "D:/Repos/database-io"

# Generate a random ID to assign to tutors
def generate(length = 20):
    options = string.ascii_letters + string.digits
    return ''.join(random.choice(options) for i in range(length))

tutors = {}

file = open(home + "/imports/tutors/araza_rahul.md", "r")

contents = file.readlines()

name = contents[0][2:len(contents) - 2]

print(name)

print(contents)