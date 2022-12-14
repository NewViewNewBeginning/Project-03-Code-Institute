import time
from datetime import datetime
from sys import exit
import gspread
import pyfiglet
import pyinputplus as pyip
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("CCTV_SAT")


def get_units():

    """
    Taking avaible units from google sheet.
    """

    stock = SHEET.worksheet("stock")
    cctv_sets = int(stock.acell("A2").value)
    sat_sets = int(stock.acell("B2").value)

    if (cctv_sets or sat_sets) < 25:
        print("We had delivery and all stock back to full capacity")
        cctv_sets = 1000
        sat_sets = 1000
    return [cctv_sets, sat_sets]


def get_prices():
    """
    Taking prices from google sheet for cctv and sat tv
    """
    price = SHEET.worksheet("price")
    cctv_price = price.acell("A2").value
    sat_price = price.acell("B2").value
    return [cctv_price, sat_price]


def hello():
    """
    Welcoming function confirmig accessing and printing text.
    """
    print("\n\n---------->>>>   WELCOME TO  <<<<----------\n\n")
    logo = pyfiglet.figlet_format("SAT & CCTV")
    print(logo)
    print("\n\n---------->>>>  ORDERING SYSTEM  <<<<----------\n\n")
    time.sleep(1)

    print("\nJust confirm access to system\n")
    answer = pyip.inputYesNo("Press [Y] to continue, [N] to leave:\n ")
    if answer == "yes":
        print("\nHello and welcome in our SAT TV and CCTV order system.\n")
    elif answer == "no":
        print("\nHope to see you again.\n")
        exit()


def show_stock(stock, price):
    """
    Function showing amount of avaible stock/price units
    """
    time.sleep(1)
    print(
        "\nTo make it easy we are selling our products in sets "
        "which are including \nall cabling and needed connections."
    )
    time.sleep(1)
    print(
        "\nSAT TV set operate only 1 TV and set of CCTV including 4 cameras."
        "\nOur current prices and avabilty will be shown below.\n"
    )
    print("Do you want to continue to display avaible stock and prices?")
    answer = pyip.inputYesNo("Press [Y] to continue or [N] to leave:\n ")
    if answer == "yes":
        print("\nAvaible stock:\n")
        print(f"CCTV SETS = {stock[0]} units which cost \U0001F4B5 "
              f"${price[0]} each")
        print(
            f"SAT-TV SETS = {stock[1]} units  which cost \U0001F4B5 "
            f"${price[1]} each"
        )
    elif answer == "no":
        print("Thanks for visiting us! Hope to see you again.")
        exit()
    time.sleep(3)
    print("\nNow tell me what you need?\n")


def orders(stock):
    """
    This function is taking number of ordered items and
    checking is there enough in stock to sell needed amount to customer.
    """
    while True:
        time.sleep((1))
        print("\nPlease type number of needed sets.\n")

        cctv_avaible = int(stock[0])

        while True:
            order_cctv = pyip.inputInt("How many CCTV would you like: \n")
            if order_cctv > cctv_avaible:
                print(f"We have only {cctv_avaible} left")
            else:
                break
        sat_avaible = int(stock[1])
        while True:
            order_sattv = pyip.inputInt("How many Sat Tv would you like: \n")
            if order_sattv > sat_avaible:
                print(f"We have only {sat_avaible} left")
            else:
                break
        if order_sattv == 0 and order_cctv == 0:
            print("\nI see you choose 0 sets!\nYou need to start again.")
            continue
        else:
            break

    return [order_cctv, order_sattv]


def calc_order(order, price):
    """
    Calculating current order with possibilty
    to change it before go to next step.
    """

    total = (int(order[0]) * int(price[0])) + (int(order[1]) * int(price[1]))
    time.sleep(2)
    print(
        f"\nYou choose \U0001F4F9 { order[0]} cctv sets and \U0001F4FA "
        f"{order[1]} sat-tv sets"
    )
    print(
        f"\nYour current total is \U0001F6D2 ${total} if you want to"
        f" proceed your order.\nPlease type [Y] for "
        f"Yes or [N] for No change order.\n"
    )

    return [total, order]


class Customer:
    """
    Each customer is created by using Class
    """

    def __init__(self, name, surname, phone, email, house_num, street, city):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.house_num = house_num
        self.street = street
        self.city = city

    def show_data(self):
        return f"{self.name}, {self.surname}, {self.phone}, {self.email}, \
            {self.house_num}, {self.street}, {self.city}"


def get_customer_data():
    """
    Collecting customer data entered by inputs and return them as customer
    object also basic validation done by use pyinputplus library
    """
    time.sleep(1)
    print("\nNow please provide your details to complete order.")
    print("")
    print(
        "Follow informations are needed:\n-Name \n-Surname \n-Phone number "
        "\n-E-mail \n-Address \n"
    )

    while True:
        name = pyip.inputStr("Please type in your name: \n").capitalize()
        surname = pyip.inputStr("Please type in your surname: \n").capitalize()
        if not name.isalpha() or not surname.isalpha():
            print("\U0001F534 Enter only letters")
            continue
        else:
            break

    print("\nPlease use correct number for Irish mobile 08xxxxxxxx with 10"
          " digits\n")
    while True:
        phone = input("\U0001F4DE Please type in your mobile phone number: \n")

        if not phone.isdigit():
            print("\U0001F534 Only digits please.\n")
        elif len(phone) != 10:
            print("\U0001F534 The phone number you provided is not 10 digital")
        elif not phone.startswith("08"):
            print("\U0001F534 Your number is not starting with 08......")
            print("\U0001F534 Please keep correct format")
        else:
            print("\U0001F7E2 Correct number.\n")
            break
    email = pyip.inputEmail("\U0001F4E7 Please type in your e-mail: \n")
    print("")
    print(
        "And the last one, address in correct way House number,"
        " Street name, City \U0001F30D")
    print("")
    house_num = pyip.inputNum("\U0001F3E1 House number: \n")
    while True:
        street = pyip.inputStr("\U0001F3E1 Street name: \n").capitalize()
        if street != "" and all(chr.isalpha()
                                or chr.isspace() for chr in street):
            break
        else:
            print("Only letters are accepted.")
    while True:
        city = pyip.inputStr("\U0001F3E1 City: \n").capitalize()
        if city != "" and all(chr.isalpha() or chr.isspace() for chr in city):
            break
        else:
            print("Only letters are accepted.")

    customer = Customer(name, surname, phone, email, house_num, street, city)
    data = customer.show_data()
    return customer, [data]


def update_stock(stock, order):
    """
    Updating Stock sheet after order is finished
    """
    to_update_stock = SHEET.worksheet("stock")
    update_cctv = int(stock[0]) - int(order[0])
    update_sat = int(stock[1]) - int(order[1])

    to_update_stock.update("A2", update_cctv)
    to_update_stock.update("B2", update_sat)


def complete_order(customer, data, total):
    """
    Order summary, send customer data to google sheet with order info
    """
    print(
        f"\nThank You for your details {customer.name} {customer.surname}"
        f" \U0001F91D!"
    )
    time.sleep(2)

    print(
        f"\nYour order is accepted and it will be shipped \U0001F69A to"
        f" you in up to 2 days \non address:\n{customer.house_num}"
        f" {customer.street} {customer.city}\n "
    )
    print("Thank you for visisting and buying in our shop! "
          "\U0001F642 \U0001F642\n")
    data = data[0]
    paid = total[0]
    ordered_cctv = total[1][0]
    ordered_tv = total[1][1]
    order_time = str(datetime.now())
    new_order = SHEET.worksheet("orders")

    new_order.append_row([data, ordered_cctv, ordered_tv, paid, order_time])


def main():
    """
    Main function to keep flow of the program and start
    functions in correct order.
    """

    print(
        "\n \U0001F449  Please note that for the purpose of this project your"
        " name, number etc.\n will be added to an external sheet so feel free "
        "to add fictional\ndetails if you prefer. No data will be shared with"
        "anyone but me. \U0001F448"
    )
    time.sleep(5)

    stock = get_units()
    price = get_prices()

    hello()
    show_stock(stock, price)
    order = orders(stock)
    total = calc_order(order, price)

    while True:
        answer = pyip.inputYesNo("[Y] to complete [N] to change order: \n")
        if answer == "no":
            order = orders(stock)
            calc_order(order, price)
        elif answer == "yes":
            customer, data = get_customer_data()
            break

    complete_order(customer, data, total)
    update_stock(stock, order)


main()
