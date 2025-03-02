class Train:
    def __init__(self, name, seats, fare):
        self.name = name  
        self.seats = seats
        self.fare = fare  

    def get_status(self):
        print(f"Train Name: {self.name}")
        print(f"Available Seats: {self.seats}")
        print(f"Fare per Ticket: Rs {self.fare}")

    def book_ticket(self):
        if self.seats > 0:
            print("Ticket booked successfully!")
            self.seats -= 1  
        else:
            print("No seats available!")


train1 = Train("Pakistan Express", 330, 3200)

train1.get_status()
train1.book_ticket()
train1.get_status()
