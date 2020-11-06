class Resident:
    name = 'Unknown Name'
    email = 'co@co.com'
    password = 'Pass321!'
    Apartment = '101' 

class Employee(Resident):
    rent_discount = '1000.00'
    work_location = '10'
    
class Corporate(Resident):
    representative = 'Bob'
    company_address = '123 n 123 s'
