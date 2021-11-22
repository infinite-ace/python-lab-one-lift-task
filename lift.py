import time
from termcolor import colored

class Lift:
    emergency_number = ""
    model = ""
    # Zero floor represents our ground floor
    current_level = 0
    max_floors = 5

    def __init__(self, model, current_level, emergency_number):
        self.model = model
        self.current_level = current_level
        self.emergency_number = emergency_number

    def travel(self, destination_level):
        if destination_level > self.current_level:

            print("Going up. Floors to travel: ",  abs(destination_level - self.current_level))

            time.sleep(abs(destination_level - self.current_level))

            print(colored('Arrived', 'green'))

        elif destination_level < self.current_level:

            print("Going down. Floors to travel: ",  abs(destination_level - self.current_level))

            time.sleep(abs(destination_level - self.current_level))

            print(colored('Arrived', 'green'))

        self.current_level = destination_level

        print(colored('Caution! The door is opening and closing for 2 seconds.', 'yellow'))

        time.sleep(2)
