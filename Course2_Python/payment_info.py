class Payslips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name 
        self.payment = payment
        self.amount = amount
        
    def pay(self):
        self.payment = "yes"
            
    def status(self):
        if self.payment == "yes":
            return self.name + " is paid "+ str(self.amount)
        else:
            return self.name + " is not paid yet"

nathan = Payslips("Nathan", "no", 1100)
rogers = Payslips("Rogers", "yes", 2000)
val = Payslips("Val","no", 25663)

nathan.payment = "yes"


val.pay() # change to yes - é o que um botão pode vir a fazer, por exemplo
print(nathan.status(),"\n",rogers.status(), "\n", val.status())