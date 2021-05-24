import time

class Driver():
    pass

class Gatekeeper():
    def __init__(self):
        self.parkingLot = ParkingLot(5,5,2)

    def checkIn(self, vehcile):
        if self.parkingLot.isFull(vehcile):
            print("Lot if full")
            return None
        else:
            return self.parkingLot.issueTicket(vehcile)

    def checkOut(self, ticket):
        price = ticket.price()
        self.charge(price)
        self.parkingLot.releaseSpot(ticket.spot)
        print("Thanks, Gate is open!")




    def charge(self, price):
        print("Charged $" , price)

class Vehicle():
    def __init__(self, size):
        self.size = size

class Car(Vehicle):
    def __init__(self, length, width):
        Vehicle.__init__(self, length * width)

class Van(Vehicle):
    def __init__(self, length, width):
        Vehicle.__init__(self, length * width)

class Bus(Vehicle):
    def __init__(self, length, width):
        Vehicle.__init__(self, length * width)


class ParkingSpot():
    def __init__(self, id, size, price):
        self.id = id
        self.size = size
        self.price = price

    def getPrice(self):
        return self.price

class SmallSpot(ParkingSpot):
    def getPrice(self):
        return ParkingSpot.getPrice(self)

class MediumSpot(ParkingSpot):
    def getPrice(self):
        return ParkingSpot.getPrice(self)

class LargeSpot(ParkingSpot):
    def getPrice(self):
        return ParkingSpot.getPrice(self)

class Ticket():
    def __init__(self, vehicle, spot):
        self.vehicle = vehicle
        self.spot = spot
        self.checkIn = time.time()
        self.id = str(spot.id) + str(self.checkIn)

    def price(self):
        mins = (time.time() - self.checkIn) / 60
        return self.spot.getPrice() * mins

    def print(self):
        pass


class ParkingLot():
    def __init__(self, small, medium, large):
        self.MAX_SMALL = small
        self.MAX_MEDIUM = medium
        self.MAX_LARGE = large

        self.small_lot = [SmallSpot(i, 3, 10) for i in range(self.MAX_SMALL)]
        self.medium_lot = [MediumSpot(i, 6, 15) for i in range(self.MAX_MEDIUM)]
        self.large_lot = [LargeSpot(i, 10, 20) for i in range(self.MAX_LARGE)]

    def getEligibleSpot(self, vehicle):
        if vehicle.size <= 3:
            return

    def isFull(self, vehicle):
        if vehicle.size <= 3:
            return len(self.small_lot) == 0
        elif vehicle.size <= 6:
            return len(self.medium_lot) == 0
        elif vehicle.size > 6:
            return len(self.large_lot) == 0
        else:
            return False

    def issueTicket(self, vehicle):
        spot = self.getSpot(vehicle)
        return self.createTicket(vehicle, spot)

    def getSpot(self, vehicle):
        if vehicle.size <= 3:
            return self.small_lot.pop(0)
        elif vehicle.size <= 6:
            return self.medium_lot.pop(0)
        elif vehicle.size > 6:
            return self.large_lot.pop(0)
        else:
            return None

    def createTicket(self, vehicle, spot):
        return Ticket(vehicle, spot)

    def releaseSpot(self, spot):
        if isinstance(spot, SmallSpot):
            self.small_lot.append(spot)
        elif isinstance(spot, MediumSpot):
            self.medium_lot.append(spot)
        elif isinstance(spot, LargeSpot):
            self.large_lot.append(spot)


if __name__ == '__main__':
    gateKeeper = Gatekeeper()
    car = Car(2, 4)
    ticket1 = gateKeeper.checkIn(car)
    print(ticket1.id)
    car2 = Car(2, 4)
    ticket2 = gateKeeper.checkIn(car2)
    print(ticket2.id)
    car3 = Car(2, 4)
    ticket3 = gateKeeper.checkIn(car3)
    print(ticket3.id if ticket3 else None)
    time.sleep(30)
    gateKeeper.checkOut(ticket1)
    gateKeeper.checkOut(ticket2)

    ticket3 = gateKeeper.checkIn(car3)
    print(ticket3.id if ticket3 else None)
    time.sleep(30)
    gateKeeper.checkOut(ticket3)


