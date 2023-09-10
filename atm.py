#User account info
balance = 12506.35
correct_pin = '6789'
attempts = 3
isPinCorrect = False

#ATM screen
def display_opening_screen():
    print('Welcome to the Bank. Insert your card.')
    print('                     ')
    print('Please enter your 4 digit PIN number')

#Enter PIN
def enterPin():
    global attempts
    while isPinCorrect == False:
        pin = input('enter your pin: ')

        if pin == correct_pin:
            isPinCorrect == True
            menu()
            break

        else:
            attempts -= 1
            print(f'Incorrect PIN. You have {attempts} attempts remaining.')
            if attempts == 0:
                print('You have no attempts remaining. Exiting...')
                exit()

#Main Menu
def menu():
    print('\n****ATM MENU****')
    print('[1] display account balance')
    print('[2] deposit money')
    print('[3] withdraw money')
    print('[0] exit ATM')
    print('****************')
    option = int(input('Enter your choice: '))

    if option == 1:
        display_balance()
        menu()

    elif option == 2:
        amount = float(input('Enter amount to deposit: '))
        deposit(amount)
        menu()

    elif option == 3:
        withdrawal_menu()
        menu()

    elif option == 0:
        print('Thank you for using the Bank')
        exit_atm()

    else:
        print('Invalid option')
        menu()


#Options from menu
def display_balance():
    print('Your current balance is:', balance)

def deposit(amount):
    global balance 
    balance += amount
    print('Deposit successful')

def withdrawal_menu():
    print('[1] $10')
    print('[2] $20')
    print('[3] $50')
    print('[4] $100')
    print('[7] other amount')
    withdrawal_menu_selection()

#Withdrawal menu options
def withdrawal_menu_selection():
    global balance
    withdrawal_option = int(input('Select an option: '))
    if withdrawal_option == 1:
        if 10 > balance:
            print('Insufficient funds')
        else:    
            print('You have selected $10. Please wait for your money.')
            balance -= 10

    elif withdrawal_option == 2:
        if 20 > balance:
            print('Insufficient funds')
        else:    
            print('You have selected $20. Please wait for your money.')
            balance -= 20

    elif withdrawal_option == 3:
        if 50 > balance:
            print('Insufficient funds')
        else:    
            print('You have selected $50. Please wait for your money.')
            balance -= 50

    elif withdrawal_option == 4:
        if 100 > balance:
            print('Insufficient funds')
        else:    
            print('You have selected $100. Please wait for your money.')
            balance -= 100

    elif withdrawal_option == 7:
        withdrawal_amount = int(input('Enter your amount'))
        if withdrawal_amount > balance:
            print('Insufficient funds')
        elif withdrawal_amount <= balance:    
            print('You have selected $%s. Please wait for your money.' % withdrawal_amount)
            balance -= withdrawal_amount 

def exit_atm():
    print("Thank you, Goodbye.")
    exit()

display_opening_screen()
enterPin()