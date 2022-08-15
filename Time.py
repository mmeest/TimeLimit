import os
import time
from datetime import date
from os.path import exists

# Generate int value from current date
set_date = int(str(date.today().year) + str(date.today().month) + str(date.today().day))
# Daily time limit(180 = 180 minutes / 3 hours)
set_minutes = 180

# 'timer.txt' is a log file. If it does not exists it will be created
if(exists('timer.txt')):
    with open('timer.txt', 'r') as file:
        content = file.read()
    first_line = int(content.split('\n', 1)[0])
    file.close()
    if(first_line == set_date):
        set_minutes = int(content.split('\n', 1)[1])
    else:
        with open('timer.txt', 'w', encoding='utf-8') as file:
            file.writelines(str(set_date) + '\n' + str(set_minutes))
        file.close()
else:
    with open('timer.txt', 'w') as file:
        file.writelines(str(set_date) + '\n' + str(set_minutes))

# After every minute time counter will update
while True:
    time.sleep(60)
    # print(set_minutes)
    set_minutes -= 1
    with open('timer.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    data[1] = str(set_minutes)
    with open('timer.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)
    file.close()
    if(set_minutes <= 0):
        os.system('shutdown /s /t 1')   
