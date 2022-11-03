import time
from sys import exit
import pyinputplus as pyip
import pyfiglet

def hello():
    '''
    Welcoming function confirmig accessing and asking for name to personalize welcome message. 
    '''
    logo = pyfiglet.figlet_format("SAT & CCTV")
    print(logo)
    print('\nWelcome! Before you enter can I ask you for your name? \n')
    time.sleep(1)
    answer = pyip.inputYesNo('Press [Y] to continue, [N] to leave: ')
    if answer == 'yes':
        name = pyip.inputStr('\nWhats your name: ').capitalize()
        print('')
        print(f'Hello {name} and welcome in our SAT TV and CCTV order system')
        print('')
    elif answer == 'no':
        print('\nSorry you pressed No which is closing system. You can come back if you wish and start again.\n')
        exit()
    
        
def show_stock(stock,price):
    '''
    Function showing amount of avaible stock/price units
    '''
   
    time.sleep(1)
    print('\nTo make it easy we are selling our products in sets which are including all cabling and needed connections.')
    time.sleep(1)
    print('\nSAT TV set operate only 1 TV and set of CCTV including 4 cameras.\nOur current prices and avabilty will be shown below\n')
    print('Do you want to continue to display avaible stock and prices?')
    answer = pyip.inputYesNo('Press [Y] to continue or [N] to leave: ')
    if answer == 'yes':
        print('\nAvaible stock:')
        for x,y in stock.items():
            
            print(f'\n{x} = -->{y}<-- units')
        
        print('\nCurrent prices:\n')    
        
        for z,c in price.items():
            
            print(f'{z} = -->${c}<-- each')
    elif answer == 'no':
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
    '''
    This function is taking number of ordered items and checking is there enough in stock to sell needed amount to customer.
    '''
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
    '''
    Calculating current order with possibilty to change it befor go to next step.
    '''
    
    total = (int(order[0]) * price['cctv_set_price']) + (int(order[1]) * price['sat_price'])
    time.sleep(2)
    print(f'\nYour current total is ${total} if you want to change your order please type [Y] for Yes or [N] for No and proceed to complete order.\n')
    
    if total == 0:
        print('\nI see you choose 0 sets\nYou need to start again if you change your mind.')
        time.sleep(2)
        exit()

    return total, order

class Customer:
    '''
    Each customer is created by using Class
    '''
    def __init__(self,name,surname,phone,email,house_num,street,city):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.house_num = house_num
        self.street = street
        self.city = city
        
def get_customer_data():
    '''
    Collecting customer data entered by inputs and return them as customer object also basic validation done by use pyinputplus library
    '''
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
    
    '''Order summary, subtract stock and complete program'''
    
    time.sleep(2)
    print(f'\nYour order is accepted and it will be shipped to you in up to 2 days on address:\n {customer.house_num} {customer.street} {customer.city}\n ')
    print('Thank you for visisting and buing in our shop!\n')
    
    stock['cctv_sets'] = stock['cctv_sets'] - int(order[0])
    stock['sat_sets'] = stock['sat_sets']  - int(order[1])
    
    
def main():
    '''
    Main function to keep flow of the program and start functions in correct order. Stock and Price values also keeps in it.
    '''
    stock ={
            'cctv_sets' : 100,
            'sat_sets' : 300, 
        } 
    price = {
            'cctv_set_price' : 100,
            'sat_price' : 120
    }
    
    hello()
    show_stock(stock, price)
    order = orders(stock)
    calc_order(order, price)
    
    while True:
        answer = pyip.inputYesNo('[Y] to change [N] to complete order: ')
        if answer == 'yes':
            order = orders(stock)
            calc_order(order, price)
        elif answer == 'no':    
            customer = get_customer_data()
            break
    complete_order(customer, stock, order)
    
main()


        
    
