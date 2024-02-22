import json


class BankAccount:

    def __init__(self, initial_balance=0):

        self.balance = initial_balance


    def withdraw(self, amount):

        if amount > self.balance:

            raise ValueError("Insufficient funds")

        self.balance -= amount


    def deposit(self, amount):

        if amount < 0:

            raise ValueError("Deposit amount must be positive")

        self.balance += amount


    def display_balance(self):

        return self.balance



def save_balance(balance):

    with open("balance2.json", "w") as f:

        json.dump(balance, f)



def load_balance():

    try:

        with open("balance2.json", "r") as f:

            balance = json.load(f)

    except FileNotFoundError:

        balance = 0

    return balance



def main():

    balance = load_balance()

    account = BankAccount(balance)

    print("You are accessing the bank account of the user REG")

    print("Initial balance:", account.display_balance())


    while True:

        print("\nChoose an option:")

        print("1. Deposit")

        print("2. Withdraw")

        print("3. Display balance")

        print("4. Exit")


        choice = input("Enter the number of your choice: ")


        if choice == "1":

            amount = float(input("Enter the amount to deposit: "))

            account.deposit(amount)

            print("Deposit successful. New balance:", account.display_balance())

        elif choice == "2":

            amount = float(input("Enter the amount to withdraw: "))

            account.withdraw(amount)

            print("Withdrawal successful. New balance:", account.display_balance())

        elif choice == "3":

            print("Current balance:", account.display_balance())

        elif choice == "4":

            print("Exiting...")

            save_balance(account.balance)

            break

        else:

            print("Invalid choice. Please try again.")



if __name__ == "__main__":

    main()