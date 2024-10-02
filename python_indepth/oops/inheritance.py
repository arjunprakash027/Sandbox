#single inheritance
class parent(): #initialize parent class
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def ischild(self):
        print (False)


class child(parent): #initialize child class
    def display(self):
        print(f"Name: {self.name} \nAge: {self.age}")

    def ischild(self):
        print(True)


arjun = child("Arjun", 25) #child class uses the construxtor of parent class
arjun.display()
arjun.ischild()

rames = parent("Rames", 50)
rames.ischild()

#multiple inheritance

class base1():
    def __init__(self,name1):
        self.str1 = name1
class base2():
    def __init__(self,name2):
        self.str2 = name2

class derived(base1,base2):
    def __init__(self,name1,name2):
        base1.__init__(self,name1)
        base2.__init__(self,name2)
        print(self.str1,self.str2)

obj = derived("arjun","rameh")

#multilevel inheritance

class apartment():
    def __init__(self,apartment_name):
        self.apartment_name = apartment_name
    

class street(apartment):
    def __init__(self,apartment_name,street_name):
        apartment.__init__(self,apartment_name)
        self.street_name = street_name
    

class city(street):
    def __init__(self,apartment_name,street_name,city_name):
        street.__init__(self,apartment_name,street_name)
        self.city_name = city_name
    
    def display(self):
        print(f"Apartment: {self.apartment_name} \nStreet: {self.street_name} \nCity: {self.city_name}")

adress = city("A1","B1","C1")
adress.display()

#private variable that cannot be inherited by class

class parent():
    def __init__(self):
        self.name = "arjun"
        self.__age = 21

class childz(parent):
    def __init__(self):
        self.degree = "B.Tech"
        parent.__init__(self)
    
    def display(self):
        print(self.name)
        print(self.__age) #this will throw an error
        print(self.degree)

obj = childz()
obj.display()