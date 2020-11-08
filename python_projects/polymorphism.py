#Parent Class User
class User:
    name = "Mark"
    username = "Mark123"
    password = "1234abcd"
    
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_username = input("Enter your username: ")
        entry_password = input("Enter you password: ")
        if (entry_username == self.username and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else
            print("The password or email is incorrect.")
            
#Child Class Employee
class Employee(User):
    base_pay = 11.00
    department = "General"
    password = "1234abcd"
    
#This is the same method in the parent class "User".
#The difference is that, instead of using a username we are using an EmployeeID. 

    def getLoginInfo(self): entry_name = input("Enter your name: ")
    entry_eid = input("Enter your employee ID: ")
    entry_pasword = input("Enter your password: ")
    if (entry_password == self.password and entry_eid == self.eid):
        print("Welcome back, {}!".format(entry_name))
    else
        print("The employee ID or email is incorrect")
        
#The following code invokes the methods inside each class for User and Employee. 

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo() 
