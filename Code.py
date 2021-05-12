from datetime import datetime, time, date
import csv

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
    with open('/Users/kate/Desktop/Hustle/coding/CS101_Project/project/log.csv', 'w') as log:
        writer = csv.writer(log)
        writer.writerow([record_date, record_time, record.tag, record.mmol_level, record.mgdl_level])
        log.close()

def retrieve_record(date):
    retrieved = []
    with open('/Users/kate/Desktop/Hustle/coding/CS101_Project/project/log.csv', 'r') as log:
        reader = csv.reader(log, delimiter = ",")
        for line in reader:
            if line[0] == date:
                retrieved.append([line[2], line[3]])
        for record in retrieved:
            print(record[0] + "\t" + record[1])
    


#Screen
print("This is Yen's Blood Sugar Log. Please select your action.")
print("1. New Record    2. Retrieve Record")

#Input
action = input()
if action == 1:
    mgdl = float(input("Current Reading:"))
    new_record = Records(mgdl)
    write_record(new_record)
elif action == 2:
    x = str(input("Date in YYYYMMDD format:"))
    convert_date = datetime.strptime(x, '%Y%m%d')
    read_date = convert_date.strftime('%Y-%m-%d')
    retrieve_record(read_date)







