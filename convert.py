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

# Create the database
data = {}
data['tutors'] = {}

file = open(home + "/imports/tutors/araza_rahul.md", "r")
contents = file.readlines()

next_id = generate()
data['tutors'][next_id] = {}

name = contents[0][2:len(contents[0]) - 1]
print('Now processing: ' + name)
data['tutors'][next_id]['name'] = name

style_index = contents.index('## Teaching Style\n') + 2
style = contents[style_index]
data['tutors'][next_id]['bio'] = {}
data['tutors'][next_id]['bio']['style'] = style

description_index = contents.index('## Experience\n') - 2
description = contents[description_index]
data['tutors'][next_id]['bio']['description'] = description[0:len(description) - 2]

experience_index = contents.index('## Experience\n') + 2
experience = contents[experience_index]
data['tutors'][next_id]['bio']['experience'] = experience[0:len(experience) - 2]

split_name = name.split(' ')
data['tutors'][next_id]['lastname'] = split_name[1]

drive_index = contents[11].find("Drives?") + 16
does_drive = contents[11][drive_index:drive_index + 3]
drives = does_drive == "Yes"
data['tutors'][next_id]['info'] = {}
data['tutors'][next_id]['info']['drives'] = drives

print(json.dumps(data, indent = 2))