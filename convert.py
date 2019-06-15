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

data = {}
data['tutors'] = {}

file = open(home + "/imports/tutors/araza_rahul.md", "r")

contents = file.readlines()

next_id = generate()
data['tutors'][next_id] = {}

name = contents[0][2:len(contents) - 2]


print(next_id)

print(contents)

print(json.dumps(data, indent = 2))