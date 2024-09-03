class Person():
    def give_name (self,name, lastname):
        self.name = name
        self.lastname = lastname
romi = Person()
romi.give_name("romina","godoy")
print (romi.name, romi.lastname)