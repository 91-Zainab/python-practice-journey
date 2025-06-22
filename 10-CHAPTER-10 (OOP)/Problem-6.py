#Can you change the self-parameter inside a class to something else (say "harry"). Try changing self to "slf" or "harry" and see the effects.

from random import randint
class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(harry, fro, to):
        print(f"The ticket is booked in train no: {harry.trainNo} from {fro} to {to}")

    def status(self):
        print(f"train {self.trainNo} is running on time.")

    def fare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t = Train(6543)
t.book("karachi","lahore")
t.status()
t.fare("Karachi","Lahore")

# Our output will remain intact, but our code readability will suffer.