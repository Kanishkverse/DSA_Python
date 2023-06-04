# Taking input of users name
name = input("Please enter your name: ")

# Actual Loop of menu.
while True:
    # Presenting Menu
    print("1 - Convert US Dollar to British Pound")
    print("2 - Convert British Pound to US Dollar")
    print("3 - Exit")

    # Asking for choice
    choice = int(input("Please enter your choice (1/2/3): "))

    # Exiting if choice is option 3
    if choice == 3:
        print("Thank you", name, "!")
        break
    else:
        if choice == 1:
            # Asking for amount in USD and printing the converted GBP
            amount = float(input("Enter the amount to be converted: "))
            print(str(amount), " USD is equivalent to ", str(amount*0.87),  " GBP.")
        
        if choice == 2: 
            # Asking for amount in GBP and priniting the converted USD
            amount = float(input("Enter the amount to be converted: "))
            print(str(amount), " GBP is equivalent to ", str(amount*1.15), " USD.")

        # Asking if user wants to continue
        loop = input("Do you want to convert again? (Yes/No): ")
        if loop == "Yes" or loop == "yes" or loop == "Y" or loop == "y":
            continue
        else:
            # If not then exiting
            print("Thank you", name, "!")
            print("Assignment Submitted by Kanishk")
            break



