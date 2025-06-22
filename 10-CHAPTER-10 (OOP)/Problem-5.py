#write a class train which has methods to book a ticket get status (no of seats) and get fare information of train running under Pak railways.
from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"The ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def status(self):
        print(f"train {self.trainNo} is running on time.")

    def fare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t = Train(6543)
t.book("karachi","lahore")
t.status()
t.fare("Karachi","Lahore")