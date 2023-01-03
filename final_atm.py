import os

# ATM System
'''
    Sanchay Vashist
    03596402720
    5C12
'''
# Constants
MIN_BALANCE = 500

# Data of customer
customer_data = {
    123456: {"Name":"Sanchay Vashist","PIN":1133,"Account_balance":40000 },
    234567: {"Name":"Aryan Arora","PIN":2344,"Account_balance":3324 },
    345678: {"Name":"Karthik Gulati","PIN":6644,"Account_balance":43555 },
    456789: {"Name":"Swaraj Chaudhary","PIN":3424,"Account_balance":56733 },
    567890: {"Name":"Pranav Jha","PIN":5434,"Account_balance":4340 }
}

# Data of admin
admin_data={
    786345:1543,
    543523:4533
}

class ATM:
    # Cash in ATM
    def __init__(self, balance=25000):
        self.balance = balance

    #Function to withdraw cash
    def withdraw(self, card_number, amount):
        if card_number in customer_data:
            customer = customer_data[card_number]
            if customer["Account_balance"] >= amount + MIN_BALANCE and self.balance >= amount and amount>0:
                self.balance -= amount
                customer["Account_balance"] -= amount
                print(' Withdrawal successful. Your current balance is: {}'.format(customer["Account_balance"]))
            elif customer["Account_balance"] < amount:
                print("Insufficient balance")
            elif amount < 0:
                print("Invalid amount")
            elif self.balance < amount:
                print("ATM does not have sufficient cash")
        else:
            print("Invalid card number")

    # Funciton to deposit cash
    def deposit(self, card_number, amount):
        if card_number in customer_data:
            customer = customer_data[card_number]
            if amount >= 0:
                self.balance += amount
                customer["Account_balance"] += amount
                print(' Deposit successful. Your current balance is: {}'.format(customer["Account_balance"]))
            else:
                print("Invalid amount")
        else:
            print("Invalid card number")
    
    # Function to transfer funds
    def transfer(self, card_number, recipient_card_number, amount):
        if card_number in customer_data and recipient_card_number in customer_data:
            sender = customer_data[card_number]
            recipient = customer_data[recipient_card_number]
            if sender["Account_balance"] >= amount + MIN_BALANCE:
                sender["Account_balance"] -= amount
                recipient["Account_balance"] += amount
                print(' Transfer successful. Your current balance is: {}'.format(sender["Account_balance"]))
            elif amount < 0:
                print("Invalid amount")
            else:
                print("Transaction failed")
        else:
            print("Invalid card number")
    
    #Function to change PIN
    def change_pin(self, card_number, new_pin):
        if card_number in customer_data:
            customer = customer_data[card_number]
            if new_pin > 999 and new_pin < 10000:
                customer["PIN"] = new_pin
                print("PIN changed successfully")
            else:
                print("Invalid PIN")
        else:
            print("Invalid card number")
    
    #Function to diplay details
    def show_details(self, card_number):
        if card_number in customer_data:
            customer = customer_data[card_number]
            print("Name: {}".format(customer["Name"]))
            print("Account Balance: {}".format(customer["Account_balance"]))
        else:
            print("Invalid card number")

#Function to verify customer
def verify_customer(card_number, pin):
    if card_number in customer_data:
        if customer_data[card_number]["PIN"] == pin:
            return True
    return False

#Funciton to verify Admin
def verify_admin(card_number, pin):               
    if card_number in admin_data:
        if admin_data[card_number]==pin:
            return True
    return False
    
# Function to give user to time to see output
def pause():
    input("Press Enter to continue...")

# Menu after customer verfied
def customer_menu(atm, card_number):
    while True:
        os.system("clear")
        print("Welcome to the customer menu")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Transfer")
        print("4. Change PIN")
        print("5. Show details")
        print("0. Log out")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = int(input("Enter amount: "))
            atm.withdraw(card_number, amount)
        elif choice == "2":
            amount = int(input("Enter amount: "))
            atm.deposit(card_number, amount)
        elif choice == "3":
            recipient_card_number = int(input("Enter recipient card number: "))
            amount = int(input("Enter amount: "))
            atm.transfer(card_number, recipient_card_number, amount)
        elif choice == "4":
            new_pin = int(input("Enter new PIN: "))
            atm.change_pin(card_number, new_pin)
        elif choice == "5":
            atm.show_details(card_number)
        elif choice == "0":
            break
        pause()

# Menu after admin verfied
def admin_menu(atm):
    while True:
        os.system("clear")
        print("Welcome to the admin menu")
        print("1. Show ATM balance")
        print("0. Log out")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("ATM balance: {}".format(atm.balance))
        elif choice == "0":
            break
        pause()

# Execution start
if __name__ == "__main__":
    atm = ATM()
    while True:
        os.system("clear")
        print("Welcome to the ATM")
        print("1. Customer")
        print("2. Admin")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            card_number = int(input("Enter card number: "))
            pin = int(input("Enter PIN: "))
            if verify_customer(card_number, pin):
                customer_menu(atm, card_number)
            else:
                print("Invalid card number or PIN")
                pause()
        elif choice == "2":
            card_number = int(input("Enter card number: "))
            pin = int(input("Enter PIN: "))
            if verify_admin(card_number, pin):
                admin_menu(atm)
            else:
                print("Invalid card number or PIN")
                pause()
        elif choice == "0":
            break
