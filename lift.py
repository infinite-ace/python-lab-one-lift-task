import time
from termcolor import colored


class Lift:
    emergency_number = ""
    model = ""
    # Zero floor represents our ground floor
    current_level = 0
    max_floors = 5
    is_traveling = False
    open_door_duration = 3

    def __init__(self, model, current_level, emergency_number):
        self.model = model
        self.current_level = current_level
        self.emergency_number = emergency_number

    def travel(self, destination_level):
        self.is_traveling = True

        abs_floors = abs(destination_level - self.current_level)

        if destination_level > self.current_level:

            print(colored(f"Going up. Floors to travel: {abs_floors}", 'magenta'))

            time.sleep(abs_floors)

            print(colored('Arrived', 'green'))

        elif destination_level < self.current_level:

            print(colored(f"Going down. Floors to travel: {abs_floors}", 'magenta'))

            time.sleep(abs_floors)

            print(colored('Arrived', 'green'))

        self.current_level = destination_level

        print(colored(f'Caution! The door is opening and closing for {self.open_door_duration} seconds.', 'yellow'))

        time.sleep(self.open_door_duration)

        self.is_traveling = False

    def return_to_ground_floor(self):
        if not self.is_traveling:
            print(colored('Going to ground floor', 'cyan'))
            self.travel(0)
