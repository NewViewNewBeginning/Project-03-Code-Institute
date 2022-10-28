
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
        print(f'Hello {name} and welcome in our SAT TV and CCTV order system')
        print('')
    else:
        print('\nSorry you pressed N or other key which close our system. You can come back if you wish and start again.\n')
        exit() 
        
def show_stock():
    '''
    That function show and contain amount of avaible stock units
    '''
    stock ={
            'cctv_sets' : 100,
            'sat_sets' : 300, 
        } 
    price = {
            'cctv_set_price' : 100,
            'sat_price' : 120
        }
 
    time.sleep(1)
    print('\nTo make it easy we are selling our products in sets which are including all cabling and connections.')
    time.sleep(1)
    print('\nSAT TV set operate only 1 TV and set of CCTV including 4 cameras.\nOur current prices and avabilty will be shown below\n')
    print('Do you want to continue?')
    answer = input('Press Y to continue or N to leave: ')
    if answer.lower() == 'y':
        print('\nAvaible stock:')
        for x,y in stock.items():
            print(f'\n{x} = {y} units')
        
        print('\nCurrent prices:\n')    
        
        for z,c in price.items():
            print(f'{z} = ${c} each')
    else:
        print('Thanks for visiting us!') 
        exit()        
        
    return stock, price

def orders():
    '''This function is taking number of ordered items'''
    
    print('Please type number of needed sets.')
    
    cctv = int(input('How many CCTV would you like: '))
    
    sattv = int(input('How many Sat Tv would you like: '))
    
    return [cctv , sattv]


        
        
        
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
    stock, price = show_stock()
    orders(stock)
    
   
    
    # customer = Customer.get_customer_data()
    
    # data_veryfication(customer)

main()
        
    
