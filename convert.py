# Converts v1 to v2 in Python

# Imports
import json
import random
import string
import os
from shutil import copyfile

# Home Directory
home = "D:/Repos/database-io"
profiles = "/imports/tutors/"
images = "/imports/headshots/"

# Generate a random ID to assign to tutors
def generate(length = 20):
    options = string.ascii_letters + string.digits
    return ''.join(random.choice(options) for i in range(length))

# Create the database
data = {}
data['tutors'] = {}

for filename in os.listdir(home + profiles):
    # Open the tutor v1 file and read it
    file = open(home + profiles + filename, "r")
    contents = file.readlines()
    named_file = filename[0:len(filename) - 2]
    print(named_file)

    # Generate a tutor v2 ID
    next_id = generate()
    copyfile(home + images + named_file + "jpg", "exports/images/" + next_id + "jpg")
    data['tutors'][next_id] = {}

    # Get the name
    name = contents[0][2:len(contents[0]) - 1]
    print('Now processing: ' + name)
    data['tutors'][next_id]['name'] = name

    # Get the teaching style
    style_index = contents.index('## Teaching Style\n') + 2
    style = contents[style_index]
    data['tutors'][next_id]['bio'] = {}
    data['tutors'][next_id]['bio']['style'] = style

    # Get the description
    description_index = contents.index('## Experience\n') - 2
    description = contents[description_index]
    data['tutors'][next_id]['bio']['description'] = description[0:len(description) - 2]

    # Get the experience
    experience_index = contents.index('## Experience\n') + 2
    experience = contents[experience_index]
    data['tutors'][next_id]['bio']['experience'] = experience[0:len(experience) - 2]

    # Get the last name
    split_name = name.split(' ')
    data['tutors'][next_id]['lastname'] = split_name[1]

    # Gets their driving ability
    drive_index = contents[11].find("Drives?") + 16
    does_drive = contents[11][drive_index:drive_index + 3]
    drives = does_drive == "Yes"
    data['tutors'][next_id]['info'] = {}
    data['tutors'][next_id]['info']['drives'] = drives

    # Do something about price

    # Gets whether they're willing to negotiate the price
    negotiable = contents[9].find('Negotiable') != -1
    data['tutors'][next_id]['info']['negotiable'] = negotiable

    # Do something about availability

    # Gets their subjects
    start_index = 8
    end_index = experience_index - 6
    end_subject = contents[start_index].find(" |") - 1
    subjects = []
    for x in range(start_index, end_index):
        if (contents[x][0:3] == "|  "):
            break
        subjects.append(contents[x][2:end_subject].strip())
    data['tutors'][next_id]['info']['subjectnames'] = subjects

    # Gets their first name
    data['tutors'][next_id]['firstname'] = split_name[0]

    # Adds their ID
    data['tutors'][next_id]['id'] = next_id

    # Adds their city (except not)
    data['tutors'][next_id]['location'] = {}
    data['tutors'][next_id]['location']['city'] = 'Thousand Oaks'

    # Adds their school
    location_index = contents[8].find("Location") + 16
    location = contents[8][location_index:len(contents[8]) - 2].strip()
    data['tutors'][next_id]['location']['school'] = location

print(json.dumps(data, indent = 2))

with open('exports/firebase.json', 'w+') as outfile:
    json.dump(data, outfile)