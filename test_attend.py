import csv
import datetime
import time
import pandas as pd
from boltons import iterutils

filename = 'Attendance.log'
with open(filename) as file:
    content = file.read().splitlines()
    print(content)
    attendance1 = set(content)
    print('attendance1 set: ', attendance1)

attendance2 = list(attendance1)

print('attendance2 list: ', attendance2)
main_attendance = list(list(attendance2))
new_attendance = main_attendance.strip('" ')

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')

with open('MainAttendance_' + date + '.csv', 'a+', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_NONE, escapechar='\\')
    csv_writer.writerow(['Name', 'Value'])
    csv_writer.writerow([main_attendance])

print(main_attendance)
#
# fields = ['Name', 'Branch', 'year']
#
# rows = [
#     ['John', 'kutus', '4'],
#     ['mark', 'embu', '3'],
#     ['jaems', 'naks', '1'],
# ]
#
#
# with open('namee.csv', 'w') as f:
#     csv_writer = csv.writer(f)
#     csv_writer.writerow(fields)
#     csv_writer.writerows(rows)
#     print(rows)

old_string= '"python"'

new_string=old_string.strip('"')