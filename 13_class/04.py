def message(str):

    #nested function
    def addWelcome():
        return "welcome to "
    
    return addWelcome()+str  

def site(site_name):
    return site_name

print(message(site("himaja")))      