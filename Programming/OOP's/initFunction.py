class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return ( f"{self.name,self.age}")
class student(person):
    pass
p1=person("Joydeep",20)
print(p1)
