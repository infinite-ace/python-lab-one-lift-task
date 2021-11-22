class Lift:
    emergency_number = ""
    model = ""
    # Zero floor represents our ground floor
    current_level = 0
    max_floors = 6

    def __init__(self, model, current_level, emergency_number):
        self.model = model
        self.current_level = current_level
        self.emergency_number = emergency_number

    def travel(self, destination_level):
        if destination_level > self.current_level:
            print("Going up")
        elif destination_level < self.current_level:
            print("Going down")

        self.current_level = destination_level
