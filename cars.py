class Car :
    def __init__(self, model, years, color, company, speedLimit) :
        self.model = model
        self.years = years
        self.color = color
        self.company = company
        self.speedLimit = speedLimit

    def start(self):
        print("The car has been started")
    
    def stop(self):
        print("The car has stopped")

    def accelarate(self, speed):
        print("The car has accelarated by", speed)

    def changeGear(self, gear):
        print("The Car Gear changed to", gear)


Car1 = Car("X10", 2, "red", "BMW", 150)
Car1.accelarate(100)