class Customer:
    """Class customer will collect and validate customer details which will be provided at the end of purchasing proccess"""
    
    def __init__(self,name,surname,phone,email,house_num,street,city):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.house_num = house_num
        self.street = street
        self.city = city
        
def get_customer_data():
    surname = input('Please type in your surname: ').capitalize()
    phone = int(input('Please type in your phone number: '))
    email = input('Please type in your email: ')
    print('')
    print('And the last one, address in correct way House number, Street name, City')
    print('')
    house_num = int(input('House number: '))
    street = input('Street name: ').capitalize()
    city = input('City: ').capitalize()
        
    customer = Customer(surname, phone,email, house_num,street, city)
        
    return customer
        
    
