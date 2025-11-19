balance = 50000
#attempts = 0
#PIN = '2005'

def atm_machine():
    #balance = 50000
    attempts = 0
    PIN = '2005'

    #Balance and pin

    #PIN VERIFICATION
    while attempts < 3:
        user_pin = input("Enter your pin: ")
        if user_pin == PIN:
            print("Acess Granted")
            break
        else:
            attempts += 1
            print(f"Access Denied. You have {3 - attempts} attempts left\n")
    else:
        print("You have tried so many times. Access blocked!")
        return  # Exit the program if PIN is incorrect

    #ATM OPTIONS
    while True:
        print("\n === ATM MENU ===")
        print("1. Check Balance")
        print("2.Withdraw Money")
        print("3.Deposit Money")
        print("4. Exit")

        choice = input("Select an option(1-4):  ")

        #CHECK BALANCE
        if choice == "1":
            print(f"Your current balance is: ${balance}")

        #WITHDRAW
        elif choice == "2":
            amount = input("Enter amount to be withdrawn: ")
            balance -= amount
            print(f"Your current amount is:  ${balance}")

        #DEPOSIT MONEY
        elif choice == "3":
            amount = input(f"Enter amount to be deposited:  ")
            balance += amount
            print(f"Deposited ${amount}. New balance is: ${balance}")
        else:
            print("Invalid input. Please enter a positive number.")

        #EXIT
        elif choice == "4":
            print("Exiting.....Thank you for using the atm")
            break

    #invalid choice
    else:
        print("Invalid choice. Please select a valid option")

atm_machine()
