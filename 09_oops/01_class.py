class CountFromBy:
    def __init__(self,v:int=0,i:int=1):
        self.val=v
        self.inc=i
    
    def increase(self):
        self.val+=self.inc

    def __repr__(self):
        return str(self.val)    

k=CountFromBy()
print(k)   
k.increase()
print(k) 
    
    

