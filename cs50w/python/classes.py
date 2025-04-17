import random

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passengers(self, name):
        if not self.open_seats():
            return False
        else:
            self.passengers.append(name)
            return True

    def open_seats(self):
        return self.capacity - len(self.passengers)
    
    def show_passengers(self):
        print(f"Current passengers in flight( Capacity: {len(self.passengers)}/{self.capacity})")
        for index, passenger in enumerate(self.passengers):
            print(f"Passenger_{index + 1}: {passenger}")

flight = Flight(capacity=5)

people = ["Harry", "Ron", "Daniel", "Bismark", "Moses", "Sly", "Michael"]
random.shuffle(people)
for person in people:
    success = flight.add_passengers(person)
    if success:
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")

print("")
flight.show_passengers()