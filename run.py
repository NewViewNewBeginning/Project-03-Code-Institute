import time
from sys import exit
import pyinputplus as pyip


def hello():
    '''
    Welcoming function confirmig accessing and asking for name to personalize welcome msg 
    '''
    print('\nWelcome! Before you enter can I ask you for your name? \n')
    time.sleep(1)
    answer = pyip.inputYesNo('Press [Y] to continue, [N] to leave: ')
    if answer == 'y':
        name = pyip.inputStr('\nWhats your name: ').capitalize()
        print('')
        print(f'Hello {name} and welcome in our SAT TV and CCTV order system')
        print('')
    elif answer == 'n':
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
    print('\nTo make it easy we are selling our products in sets which are including all cabling and needed connections.')
    time.sleep(1)
    print('\nSAT TV set operate only 1 TV and set of CCTV including 4 cameras.\nOur current prices and avabilty will be shown below\n')
    print('Do you want to continue to display avaible stock and prices?')
    answer = pyip.inputYesNo('Press [Y] to continue or [N] to leave: ')
    if answer.lower() == 'y':
        print('\nAvaible stock:')
        for x,y in stock.items():
            
            print(f'\n{x} = -->{y}<-- units')
        
        print('\nCurrent prices:\n')    
        
        for z,c in price.items():
            
            print(f'{z} = -->${c}<-- each')
    elif answer.lower() == 'n':
        print('Thanks for visiting us! Hope to see you again.') 
        exit()
    

        
    time.sleep(2)    
    print('\nWould you like to continue?\n')
    
    answer = pyip.inputYesNo('Give [Y] to continue [N] to leave? ')  
    
    if answer == 'yes':
        time.sleep(1)
        print("Thank you and let's go to order section")
    else:
        print('Thank you, hope to see you again!')
        exit()
              
        
    return stock, price

def orders(stock):
    '''This function is taking number of ordered items and checking is there enough to sell'''
    print('\nPlease type number of needed sets.\n')

    cctv_avaible = stock['cctv_sets']
    
    
    
    while True:
        cctv = pyip.inputInt('How many CCTV would you like: ')
        if cctv > cctv_avaible:
            print(f'We have only {cctv_avaible} left')
        else:
            break
    sat_avaible = stock['sat_sets']     
    while True:
        sattv = pyip.inputInt('How many Sat Tv would you like: ')
        if sattv > sat_avaible:
                print(f'We have only {cctv_avaible} left')
        else:
            break
        
    return [cctv , sattv]

def calc_order(order, price):
    total = (int(order[0]) * price['cctv_set_price']) + (int(order[1]) * price['sat_price'])
    time.sleep(2)
    print(f'\nYour current total is ${total} if you want to change your order please type [Y] for Yes or [N] for No and proceed to complete order.\n')
    
    if total == 0:
        print('\nI see you choose 0 sets\nYou need to start again if you change your mind.')
        time.sleep(2)
        exit()

    return total, order


  
class Customer:
    
    def __init__(self,name,surname,phone,email,house_num,street,city):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.house_num = house_num
        self.street = street
        self.city = city
        
def get_customer_data():
    '''Collecting customer data entered by inputs and return them as customer object'''
    time.sleep(1)
    print('\nNow please provide your details to complete order.')
    print('')
    print("Follow informations are needed:\n-Name \n-Surname \n-Phone number \n-E-mail \n-Address \n")
    
    while True:
        name = pyip.inputStr('Please type in your name: ').capitalize()
        surname = pyip.inputStr('Please type in your surname: ').capitalize()
        if not name.isalpha() or not surname.isalpha():
            print('Enter only letters')
            continue
        else:
            break        
    
    while True:
        print('\nPlease use correct number for Irish mobile 08xxxxxxxx with 10 digits\n')
        phone = input('Please type in your mobile phone number: \n')
        
        if len(phone) == 10 and phone[0] == '0' and phone[1] == '8' and phone.isdigit():
            print('Correct number\n')
            break
        else:
            print('Please provide valid number, only numbers! ')
            continue
            
    
    email = pyip.inputEmail('Please type in your email: ')
    print('')
    print('And the last one, address in correct way House number, Street name, City')
    print('')
    house_num = pyip.inputNum('House number: ')
    street = pyip.inputStr('Street name: ').capitalize()
    city = pyip.inputStr('City: ').capitalize()
    
    print('\nThank You for your details!')
            
    customer = Customer(name, surname, phone,email, house_num,street, city) 
    return customer


def complete_order(customer, stock, order):
    '''Order summary, subtract stock '''
    time.sleep(2)
    print(f'\nYour order is accepted and it will be shipped to you in up to 2 days on address:\n {customer.house_num} {customer.street} {customer.city}\n ')
    print('Thank you for visisting and buing in our shop!\n')
    
    stock['cctv_sets'] = stock['cctv_sets'] - int(order[0])
    stock['sat_sets'] = stock['sat_sets']  - int(order[1])
    
    
def main():
    hello()
    stock, price = show_stock()
    order = orders(stock)
    calc_order(order, price)
    
    while True:
        answer = pyip.inputYesNo('[Y] to change [N] to complete order: ')
        if answer == 'y':
            order = orders(stock)
            calc_order(order, price)
        else:    
            customer = get_customer_data()
            break
    complete_order(customer, stock, order)

main()


        
    
