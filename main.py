# Tyler Gregory
# Coding Challenge 3

# Part 1
def discount10(price):
    return price * .9

def discountReg(price):
    return discount10(price) * .95

# Part 2
x = 5
print((lambda x: x*(x+5)**2)(x))

# Part 3
prices = [9.99, 15.99, 24.99, 49.99, 59.99]
discounted = list(map(discount10, prices))

# Part 4
class Computer:
    def __init__(self, os, price):
        self.os = os
        self.price = price

    def getspecs(self):
        return self.os, self.price

    def displayspecs(self):
        print("OS: ", self.os, " Price: ", self.price)

class Laptop(Computer):
    def __init__(self, os, price, battery):
        super().__init__(os, price)
        self.battery = battery

    def displayspecs(self):
        print("OS: ", self.os, " Price: ", self.price, " Battery: ", self.battery)

    def getbattery(self):
        return self.battery

class Desktop(Computer):
    def __init__(self, os, price, monitor):
        super().__init__(os, price)
        self.monitor = monitor

    def displayspecs(self):
        print("OS: ", self.os, " Price: ", self.price, " Monitor: ", self.monitor)

    def getmonitor(self):
        return self.monitor

# Part 5
class Add:
    def __init__(self, num):
        self.num = num

    def __mul__(self, other):
        return self.num + other.num

print(Add(5) * Add(5))