class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)    
x=person("john","doe")
x.printname()        

class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.gradutaionyear=year

y=student("mike","olsen",2016)  
y.printname()      