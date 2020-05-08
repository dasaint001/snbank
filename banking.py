import random


def login():
    print("Please enter your details to log in")
    x = True
    if x is True:
        staff_username = str(input("Username: "))
        staff_password = str(input("Password: "))

        for line in open("staff.txt", "r").readlines():
            pieces = line.split(":")
            username = pieces[0]
            password = pieces[1]

            if staff_username == username and staff_password == password:
                print("Hello", username)
                x = False
                break
        else:
            print("login unsuccessful...Please try again")


def staff_login():
    while True:
        try:
            print("""
            1 Create new bank account
            2 Check Account Details
            3 Logout""")
            staff_choice = int(input("Press 1 to create new bank account\n"
                                     "Press 2 to check account detail\n"
                                     "Press 3 to logout\n" ">>> "))
            if staff_choice == 1:
                print("Fill the Form Below: ")
                acct_name = input("Account Name: ")
                opn_bal = input("Opening Balance: ")
                acct_type = input("Account Type: ")
                acct_mail = input("Account Email: ")
                acct_num = str(random.randint(1000000000, 1999999999))
                print(f"Account number is {acct_num}")
                file = open("customer.txt", "a")
                file.write(acct_name)
                file.write(":")
                file.write(opn_bal)
                file.write(":")
                file.write(acct_type)
                file.write(":")
                file.write(acct_mail)
                file.write(":")
                file.write(acct_num)
                file.write("\n")
                file.close()
                print("Bank Account created successfully... ")
            if staff_choice == 2:
                while True:
                    try:
                        print("Enter Account Number: ")
                        account_num = input(">>>> ")
                        file = open("customer.txt", "r")
                        for line in file.readlines():
                            pieces = line.split(":")
                            acct_name = pieces[0]
                            opn_bal = pieces[1]
                            acct_type = pieces[2]
                            acct_mail = pieces[3]
                            acct_num = pieces[4]
                            if account_num == acct_num:
                                print(f"Account Name is {acct_name}")
                                print(f"Opening Balance is {opn_bal}")
                                print(f"Account Type is {acct_type}")
                                print(f"Account Email is {acct_mail}")
                                file.close()
                                break
                        else:
                            print("Invalid Account Number")
                        break
                    except ValueError:
                        print("Account Number must be Integers: ")
                    except IndexError:
                        print()
            if staff_choice == 3:
                break
        except ValueError:
            print("Invalid")


def staff_option():
    while True:
        try:
            print("1 Staff Login\n""2 Close App\n")
            choice = (input("Press 'L' to login or 'C' to close app\n" ">>>> "))
            if choice == "L":
                login()
                staff_login()
            else:
                if choice == "C":
                    break
                if choice == "L" or "C":
                    print("Invalid Command. Please try again..")

        except ValueError:
            print("Invalid Input")


staff_option()
