class Car (object):
    def __init__(self,model,color,company,speedlimit):
        self.color=color
        self.model=model
        self.company=company
        self.speedlimit=speedlimit
    def start(self):
        print("started")
    def stop(self):
        print("stop")
    def accelerate(self):
        print("The car is moving")
    def changeGear(self,gear_type):
        print("Gear changed")            
audi=Car("A8L","Black","Audi","250")
print(audi.color)
audi.start()