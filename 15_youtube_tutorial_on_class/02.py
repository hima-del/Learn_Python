class Employee:
    raise_amt=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + "." + last + "@email.com"

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

dev_1=Employee('John','Doe',50000)
dev_2=Employee('Sara','Joseph',70000)

print(dev_1.email)
print(dev_2.email)
