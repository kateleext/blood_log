from datetime import datetime

class Records:
    evaluation = "None"
    log = {}
    def __init__(self, mgdl_level, timestamp = datetime.now()):
        self.mmol_level = mgdl_level*0.0555
        self.mgdl_level = mgdl_level
        self.timestamp = timestamp
        Records.log[timestamp] = self
        if self.mmol_level >= 4 and self.mmol_level < 10:
            self.evaluation = "Perfect!"
        elif mmol_level < 4:
            self.evaluation = "Blood sugar is low. Eat some candies!"
        elif mmol_level >= 10:
            self.evaluation = "Blood sugar is high! Time for insulin?"
        print("Record for {} logged. mmol/L: {}".format(timestamp, self.mmol_level))
        print(self.evaluation)




print("This is Yen's Blood Sugar Log. Please enter your current reading.")

mgdl_level = input()
new_record = Records(mgdl_level)
print(Records.log)


