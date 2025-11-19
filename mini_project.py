PIN = '2005'
balance = 50000  # global variable to maintain state

def pin_verification():
    attempts = 0
    while attempts < 3:
        user_pin = input("Enter your PIN: ")
        if user_pin == PIN:
            print("Access Granted\n")
            return True
        else:
            attempts += 1
            print(f"Access Denied. You have {3 - attempts} attempts left\n")
    print("You have tried too many times. Access blocked!")
    return False

def show_menu():
    print("\n=== ATM MENU ===")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Transfer Money")
    print("5. Exit")

def check_balance():
    print(f"Your current balance is: ${balance}")

def withdraw_amount():
    global balance
    try:
        amount = int(input("Enter amount to be withdrawn: "))
        if amount <= 0:
            print("Invalid input. Enter a positive number.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"Withdrawal successful. New balance: ${balance}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def deposit_money():
    global balance
    try:
        amount = int(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid input. Enter a positive number.")
        else:
            balance += amount
            print(f"Deposited ${amount}. New balance: ${balance}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def transfer_money():
    global balance
    recipient = input("Enter recipient's account number: ")
    try:
        amount = int(input("Enter amount to transfer: "))
        if amount <= 0:
            print("Invalid input. Enter a positive number.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"Transferred ${amount} to account {recipient}. New balance: ${balance}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def exit_atm():
    print("Exiting.....Thank you for using the ATM")

def atm_machine():
    if not pin_verification():
        return

    while True:
        show_menu()
        try:
            choice = int(input("Select an option (1-5): "))
        except ValueError:
            print("Invalid input. Choose a number from 1-5.")
            continue

        if choice == 1:
            check_balance()
        elif choice == 2:
            withdraw_amount()
        elif choice == 3:
            deposit_money()
        elif choice == 4:
            transfer_money()
        elif choice == 5:
            exit_atm()
            break
        else:
            print("Invalid choice. Please select a valid option.")

atm_machine()
