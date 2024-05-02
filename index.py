import datetime

class ParkingLot:
    def __init__(self, location, capacity):
        self.location = location
        self.capacity = capacity
        self.reservations = []

    def check_availability(self, start_time, end_time):
        for reservation in self.reservations:
            if reservation.start_time < end_time and reservation.end_time > start_time:
                return False
        return True

    def add_reservation(self, reservation):
        if self.check_availability(reservation.start_time, reservation.end_time):
            self.reservations.append(reservation)
            return True
        return False

    def __str__(self):
        return f"ParkingLot({self.location}, Capacity: {self.capacity})"

class Reservation:
    def __init__(self, user, spot, start_time, end_time):
        self.user = user
        self.spot = spot
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return (f"Reservation for {self.user.name} at spot {self.spot} from "
                f"{self.start_time} to {self.end_time}")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def make_reservation(self, parking_lot, spot, start_time, end_time):
        reservation = Reservation(self, spot, start_time, end_time)
        if parking_lot.add_reservation(reservation):
            print(f"Reservation successful: {reservation}")
        else:
            print("Reservation failed: Time slot unavailable")

    def __str__(self):
        return f"User({self.name}, {self.email})"

class ParkingManager:
    def __init__(self):
        self.parking_lots = []

    def add_parking_lot(self, parking_lot):
        self.parking_lots.append(parking_lot)

    def find_available_lot(self, start_time, end_time):
        available_lots = [lot for lot in self.parking_lots if lot.check_availability(start_time, end_time)]
        return available_lots

# Example  of usage
parking_manager = ParkingManager()
lot1 = ParkingLot("Downtown Lot", 100)
parking_manager.add_parking_lot(lot1)

user1 = User("Michael Kearse", "michaelkearsedev@gmail.com")
start_time = datetime.datetime(2024, 5, 1, 8, 0)
end_time = datetime.datetime(2024, 5, 1, 18, 0)

# User makes a reservation
user1.make_reservation(lot1, 15, start_time, end_time)
