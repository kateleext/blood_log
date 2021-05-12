from datetime import datetime, time, date, timedelta
import csv
import time as sleep

class Records:
    evaluation = "None"

    breakfast_start = time(6,0,0)
    lunch_start = time(11,0,0)
    dinner_start = time(18,0,0)
    night_start = time(23,0,0)

    def __init__(self, mgdl_level, timestamp = datetime.now()):
        self.mmol_level = mgdl_level*0.0555
        self.mgdl_level = mgdl_level
        self.timestamp = timestamp

        #Evaluation
        if self.mmol_level >= 4 and self.mmol_level < 10:
            self.evaluation = "Perfect! Keep it up!"
        elif self.mmol_level < 4:
            self.evaluation = "Blood sugar is low. Eat some candies!"
        elif self.mmol_level >= 10:
            self.evaluation = "Blood sugar is high! Time for insulin?"
        
        #Tag
        if Records.breakfast_start <= timestamp.time() < Records.lunch_start:
            self.tag = "breakfast"
        elif Records.lunch_start <= timestamp.time() < Records.dinner_start:
            self.tag = "lunch"
        elif Records.dinner_start <= timestamp.time() < Records.night_start:
            self.tag = "dinner"
        else:
            self.tag = "night"
        
        #Print
        print(timestamp.date())
        print("Record for {} logged.".format(self.tag))
        print("mmol/L: {}".format(self.mmol_level))
        print(self.evaluation)

#Functionalities
def write_record(record):
    record_date = record.timestamp.date()
    record_time = record.timestamp.time()
    with open('/Users/kate/Desktop/Hustle/coding/cs101/project/log.csv', 'a') as log:
        writer = csv.writer(log)
        writer.writerow([record_date, record_time, record.tag, record.mmol_level, record.mgdl_level])
        log.close()

def retrieve_record(date):
    retrieved = []
    with open('/Users/kate/Desktop/Hustle/coding/cs101/project/log.csv', 'r') as log:
        reader = csv.reader(log, delimiter = ",")
        for line in reader:
            if line[0] == date:
                retrieved.append([line[2], line[3]])
        for record in retrieved:
            print(record[0] + "\t" + record[1])
        log.close()

def two_week_average():
    retrieved = []
    with open('/Users/kate/Desktop/Hustle/coding/cs101/project/log.csv', 'r') as log:
        reader = csv.reader(log, delimiter = ",")
        for line in reader:
            if datetime.strptime(line[0],"%Y-%m-%d") - datetime.now() <= timedelta(days=14):
                retrieved.append([line[2], line[3]])
        count = 0
    total = 0
    for record in retrieved:
        total += float(record[1])
        count += 1
        log.close()
    print("Your 2-week average: " + str(round(total/count, 2)) + " mmol/L")
        
    
#Menu
def script():
    
    print("Please select your action.")
    action = int(input("1. New Record    2. Retrieve Record  3. 2-week Average \n"))
    
    if action == 1:
        mgdl = float(input("Current Reading:  "))
        new_record = Records(mgdl)
        write_record(new_record)
    elif action == 2:
        x = str(input("Date in YYYYMMDD format:  "))
        convert_date = datetime.strptime(x, '%Y%m%d')
        read_date = convert_date.strftime('%Y-%m-%d')
        retrieve_record(read_date)
    elif action == 3:
        two_week_average()
    else:
        print('Invalid input.')
        sleep.sleep(1)
        script()

    sleep.sleep(1)

    next_action = int(input('1. Return to menu    2. Close program \n'))
    rerun(next_action)

#To return to screen
def rerun(action):
    if action == 1:
        script()
    elif action == 2:
        exit()
    else:
        print('Invalid input.')
        new_action = int(input('1. Return to menu    2. Close program \n'))
        rerun(new_action)

#Actual Program Run
print("This is Yen's Blood Sugar Log.")
script()


