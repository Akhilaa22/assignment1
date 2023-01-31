balance = 1000
while True:
    print("1. Check balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        
        print("Your current balance is:", balance)
    elif choice == 2:
        
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Withdrawal successful. Current balance is:", balance)
    elif choice == 3:
        
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Deposit successful. Current balance is:", balance)
    elif choice == 4:
        
        print("Thank you for using our ATM. Have a nice day.")
        break
    else:
        
        print("Invalid choice. Please try again.")
