import csv

with open('yeet_out.csv', mode = 'w') as output:
    to_output = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    to_output.writerow(['sun_hours_start', 'sun_hours_end', 'mon_hours_start', 'mon_hours_end', 'tues_hours_start', 'tues_hours_end', 'wed_hours_start', 'wed_hours_end', 'thurs_hours_start', 'thurs_hours_end', 'fri_hours_start', 'fri_hours_end', 'sat_hours_start', 'sat_hours_end'])
    with open('yeet.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = False
        for row in csv_reader:
            nextRow = ['' for x in range(14)]
            if not headers:
                headers = True
            else:
                now = 0
                for day in row:
                    if len(day) is 0:
                        print('0')
                    else:
                        nextRow[now * 2] = row[now][0:5]
                        nextRow[now * 2 + 1] = row[now][6:11]
                    now = now + 1
            to_output.writerow(nextRow)
