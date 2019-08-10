import os
import csv
from shutil import copyfile

csv_file = csv.reader(open('Tutors.csv', 'r', encoding='utf8'), delimiter=',')
for row in csv_file:
    for file in os.listdir('oof_out'):
        if file.lower().find(row[1].lower()) > 0:
            print(row[1], row[2], 'success')
            try:
                os.mkdir('exports/' + row[0])
            except:
                print('oops')
            copyfile('oof_out/' + file, 'exports/' + row[0] + '/' + 'profile.jpg')
        else:
            print('ccant find guys')