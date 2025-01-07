class Employees:
    def __init__(self, name, last) -> None:
        self.name = name 
        self.last = last 
        
        
class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password
    # Need to modify the init class to add another property
    
        
class Chefs(Employees):

    def leave_request(self, days):
        return "May I take a leave for " + str(days)+ " days?"
    
# Once you have all the class, you start to creating the instancies

adrian= Supervisors("Adrian", "A.", "apple")


emily = Chefs("Emily", "E.")
juno = Chefs("Juno","J.")
    
print(emily.leave_request(3)) 
print(adrian.password)
print(emily.name +" " + emily.last)

print(issubclass(Chefs,Employees))
print(isinstance(emily,Supervisors))
        