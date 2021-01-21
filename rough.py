class Car:
    wheels=0  #Class variable
    # wheels : int  #Class variable (optional)
    def __init__(self,color,brand):
        self.color=color          #Instance Variables
        self.brand=brand
        # print("Class variable",self.wheels)

ob1=Car('red','bmw')
ob2=Car('blue','alto')

# Car.wheels=5
print(ob1.wheels)
print(ob1.color)
print(ob1.brand)

print(ob2.wheels)
print(ob2.color)
print(ob2.brand)
print(ob1,type(ob1))