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
        print(timestamp.date())
        print("Record for {} logged.".format(self.tag))
        print("mmol/L: {}".format(self.mmol_level))
        print(self.evaluation)

print("This is Yen's Blood Sugar Log.")
print("Please enter your current reading.")

def write_record(record):
    record_date = record.timestamp.date()
    record_time = record.timestamp.time()
    with open('/Users/kate/Desktop/Hustle/coding/CS101_Project/project/log.csv', 'w') as log:
        writer = csv.writer(log)
        writer.writerow([record_date, record_time, record.tag, record.mmol_level, record.mgdl_level])
        log.close()

mgdl_level = float(input())
new_record = Records(mgdl_level)
write_record(new_record)


