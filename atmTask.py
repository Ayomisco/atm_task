#importing date and time from python modules
import datetime
import time


print("Welcome to Ayomide Bank")
print("======================================")
print("======================================")
time.sleep(2)

print("Please insert your card")
print("======================================")
print("======================================")
time.sleep(3)

name = input("What is your name? \n")
##################
allowedUsers = ['Ayo', 'Seyi', 'Gift']
allowedPassword = ['ayo123', 'seyi123', 'gift123']
userBalance = [23000, 32000, 12500]
trials = 3
naira = u"\u20A6"   ###########Naira code
##################

if(name in allowedUsers):
    #check if password martches with the users id
    while trials != 0:
        password = input('Please enter your password \n')
        time.sleep(3)
        print("======================================")
        print("======================================")
        userId = allowedUsers.index(name)
        if password != allowedPassword[userId]:
            trials -= 1
            print("Wrong password, You have", trials, "more trials Left")
        else:
            #Feedback after successful login begin
            print("Welcome %s" % name)
            print("======================================")
            #Date and Time
            now = datetime.datetime.now()
            print(now.strftime("%y-%m-%d %H:%M:%S"))
            time.sleep(3)
            #Feedback after login close

            print("======================================")
            print("======================================")

            selectedOption = int(input("Choose your transaction: \n"
                                    "1. Withdrawal \n" 
                                    "2. Cash Deposit \n" 
                                    "3. Complaint \n"
                                    "===================================== \n"))
            
            time.sleep(2)
            print("======================================")
            print("======================================")

            ## Customer Widrawal Start here ###
            if(selectedOption == 1):
                userWithdraw = int(input("Enter The Amount You would Like to withdraw: \n"))
                time.sleep(2)
                print("======================================")
                print("======================================")

                if(userBalance[userId] > userWithdraw):
                    total = userBalance[userId] - userWithdraw
                    print("Please take your cash")
                    time.sleep(2)
                    print("======================================")
                    print("======================================")
                    print("your new balance is: \n", naira,total)
                else:
                    print("insufficient balance")
            ## Customer Withdrawal Ends here ###
            
            ## Customer Deposit Start here ###
            elif(selectedOption == 2):
                cashDeposit = int(input("How much would you like to deposit? \n"))
                time.sleep(2)
                print("======================================")
                print("======================================")
                total = userBalance[userId] + cashDeposit                
                print("your account balance is: /n %s" % naira, total)
            ## Customer Deposit Ends here ###

            ## Customer Complaint Start here ###
            elif(selectedOption == 3):
                CustomerReport = input("What issue will you like to report? \n")
                time.sleep(2)
                print("======================================")
                print("======================================")
                print("Thank you for contacting us")
            ## Customer Complaint Ends here ###
            else:
                print('No transaction selected')

        ### Exit and Continue ###
        time.sleep(2)
        print("======================================")
        print("======================================")
        UserExit = input("Would you like to perform another transaction? Y/N: \n")
        time.sleep(2)
        print("======================================")
        print("======================================")
        if UserExit == "N":
            print("Thank You for using Ayomide bank")
            break
        else: 
            continue


           

        
       