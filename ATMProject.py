print("WELCOME TO SBI ATM")
password=1234
Amount=50000
passkey=int(input("Enter the Passkey:"))
while True:
    if 10<passkey<99:
        Pin=int(input("Enter your pin:"))
        Process=int(input("1.Check Balance 2. With Draw 3.Deposit 4.Pin Change 5.Exit:"))
        if Pin==password:
            if Process==1:
                print("Your Balance Amount:","₹",Amount)
            elif Process==2:
                withdraw=int(input("Enter Withdraw Amount:"))
                if withdraw >50000:
                    print("Insufficient Amount")
                elif withdraw<=50000:
                    print("withdraw Amount:","₹",withdraw) 
                    print("Remain Balance:","₹",Amount-withdraw)
            elif Process==3:
                Deposit=int(input("Enter Deposit Amount:"))
                print("Deposit Amount:","₹",Deposit)
                print("Remain Balance:","₹",Amount+Deposit)
            elif Process==4:
                Pin=int(input("Enter the Older pin:"))
                New_pin=int(input("Enter Your New Pin:"))
                if Pin!=New_pin:
                    confirm_pin=int(input("Enter Your Confirm Pin:"))
                    print(New_pin,"Successfully Your Pin Changed")
                else:
                    print("Old Pin and New pin are equal ")
                    print("please enter valid Pin")
            elif Process==5:
                print("Thank You ")
                print("Please visit Again")
                break
        else:
                print("Incorrect Process")
                break
    else:
        print("Incorrect Passkey")
        break
        
        