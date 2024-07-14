name=input("Enter Your Name :")
print(f"Hello {name}")

message="""
How may I help You!

please Select any of the option

type 1 >>> CHECK BALANCE
type 2 >>> DEPOSIT
type 3 >>> WITHDRAW 
"""
print(message)

task=int(input("Please select any of the option : "))

if task==1 :
    print("Your balance is 5000")
    print("Thank u for visiting!!!")

elif task ==2 :
    deposit_amount=int(input("Enter the deposit amount : "))
    print(f"your deeposited amount is {deposit_amount} ")   
    total_amount=deposit_amount+5000
    print(f"your total amount is {total_amount}")
    print("Thank u for visiting!!!")

elif task ==3 :
    withdrawn_amount=int(input("Enter the withdraw amount : "))
    if(withdrawn_amount>5000):
        print("Sorry!!! yoy can't withdrawn more than 5000")
        print("Thank u for visiting!!!")
    else :
        print(f"your withdrawn_amount is {withdrawn_amount} ")   
        remaining_amount= 5000 - withdrawn_amount
        print("Now your remaining amount is :",remaining_amount)
        print("Thank u for visiting!!!")

else :
    print("You are not select any valid task, Please Select any valid task!")
    print("thank u for visiting")        



        


