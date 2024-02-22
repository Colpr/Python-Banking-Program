import subprocess

print("Welcome to The Bank of Mom")
#define the allowed account numbers
bank_account = {'1', '2'}
#login inputs
while True:

 login = input("Enter an account number:")
 if login in bank_account:
    break
else:
        print("Sorry, the account you requested is not in service")

#subprocess script and access to the accounts
if login == '1':
    subprocess.run(["python", "accounts/bank1.py"])

if login == '2':
    subprocess.run(["python", "accounts/bank2.py"])


