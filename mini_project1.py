balance = 50000
attempts = 0
PIN = '2005'

def user_input():
    global attempts
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


def user_choice(): 
    global balance
    choice = int(input("Select an option(1-5): "))
    if choice not in range(1, 6):
            print("Invalid choice. Please select a valid option")
            return

        #CHECK BALANCE
    if choice == 1:
            print(f"Your current balance is: ${balance}")

        #WITHDRAW
    elif choice == 2:
            amount = int(input("Enter amount to be withdrawn: "))
            balance -= amount
            print(f"Your current amount is:  ${balance}")

        #DEPOSIT MONEY
    elif choice == 3:
            amount = int(input(f"Enter amount to be deposited:  "))
            if amount <= 0:
                print("Invalid input. Please enter a positive number.")
            else:
                balance += amount
                print(f"Deposited ${amount}. New balance is: ${balance}")
        
        #Transfer Money
    elif choice == 4:
            Receipient = input(f"Enter receipient's number: ")
            try:
                amount = int(input("Enter amount to transfer: "))
                if amount > balance:
                    print("Insufficient Balance. Amount is more than exisiting balance")
                if amount <= 0:
                    print("Invalid input. Please enter a positive number.")
                else:
                    balance -= amount
                    print(f"Transferred ${amount} to account {Receipient}. New balance is: ${balance}")
            except ValueError:
                    print("Invalid input. Please enter a number.")


#EXIT
    elif choice == 5:
            print("Exiting.....Thank you for using the atm")
            return

def atm_machine():
    #Balance and pin
    

    user_input()
#ATM OPTIONS
    while True:
        print("\n === ATM MENU ===")
        print("1. Check Balance")
        print("2.Withdraw Money")
        print("3.Deposit Money")
        print("4.Transfer Money")
        print("5. Exit")
        
        try:
            user_choice()
        except ValueError:
             print("Invalid option. Enter a positive number")




       

           

atm_machine()   