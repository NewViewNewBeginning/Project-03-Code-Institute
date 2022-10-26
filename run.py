import time
from sys import exit

def hello():
    '''
    Welcoming function which will show at begining and ask for name to get access
    '''
    print('Welcome! Before you enter can I ask you for your name? ')
    time.sleep(1)
    answer = input('Press Y to continue, N to leave: ')
    if answer.lower() == 'y':
        name = input('Whats your name: ').capitalize()
        print('')
        print(f'Hello {name} and welcome in our SAT Tv and CCTV order system')
        print('')
    else:
        print('\nSorry you pressed N or other key which close our system. You can come back if you wish and start again.\n')
        exit()  



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
    time.sleep(1)
    print('\nNow please provide your details to complete order.')
    print('')
    print("Follow informations are needed:\n-Name \n-Surname \n-Phone number \n-E-mail \n-Address \n")
    
    name = input('Please type in your name: ').capitalize()
    surname = input('Please type in your surname: ').capitalize()
    phone = int(input('Please type in your phone number: '))
    email = input('Please type in your email: ')
    print('')
    print('And the last one, address in correct way House number, Street name, City')
    print('')
    house_num = int(input('House number: '))
    street = input('Street name: ').capitalize()
    city = input('City: ').capitalize()
    
        
    customer = Customer(name, surname, phone,email, house_num,street, city)
        
    return customer

def data_veryfication(customer):
    pass


def main():
    
    # hello()
    
    
    customer = get_customer_data()
    
    data_veryfication(customer)

main()
        
    
