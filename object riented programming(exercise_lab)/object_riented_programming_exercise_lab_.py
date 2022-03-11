class Car:
    """一次模拟汽车的简单尝试。"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
           long_name = f"{self.year} {self.make} {self.model}"
           return long_name.title()
    def read_odometer(self):
       print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
       if mileage >= self.odometer_reading:
           self.odometer_reading = mileage
       else:
           print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
       self.odometer_reading += miles
class Battery:
    """一次模拟电动汽车电瓶的简单尝试。"""
    def __init__(self,model,battery_size=75):
        """初始化电瓶的属性。"""
        self.battery_size = battery_size
        self.model=model
    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size==75 and self.model=='model s':
            range=260
        elif self.battery_size==100 and self.model=='model a':
            range=315
        print(f"this car can go about {range}")

class ElectricCar(Car):
        """电动汽车的独特之处。"""
        def __init__(self, make, model, year):
            """
            初始化父类的属性。
            再初始化电动汽车特有的属性。
            """
            super().__init__(make, model, year)
            self.battery = Battery(model)
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


















'''#灾难一样的例子，抽象过头+混用变量名，啧啧啧
class F1:
    def __init__(self):
        print('2',self)
        self.f3()
    def f3(self):
        self.age = 14
        self.name = 'wu'
        print('我是F1的')

class F2(F1):
    def __init__(self,classname):
        print('实例化F1')
        self.classname = classname
    def f1(self):
        self.classname()
        print('1',self)
    def f3(self):
        print('我是F2的！')
obj = F2(F1)
obj.f1()


'''