#Submitted by Kanishk
#Assignment 5 - CPS 501 (Alternate Version)
import random
import os
from datetime import datetime

# Function to generate random numbers
def gen(digit):
    if digit == 1:
        return random.randint(1, 9), random.randint(1, 9)
    if digit ==2:   
        return random.randint(10, 99), random.randint(10, 99)
    else:    
        return random.randint(100, 999), random.randint(10, 999)
# Function for addition
def add(n1, n2):
    return str(n1+n2)

# Function for subtraction
def subtract(n1, n2):
    return str(n1-n2)

# Function for multiplication
def multiply(n1, n2):
    return str(n1*n2)

# Function for division
def divide(n1, n2):
    res = "{0:.2f}".format(n1/n2)
    return res

class Report():

    def __init__(self, username):
        self.stats = [[0,0], [0,0], [0,0], [0,0]]
        self.username = username
        self.report_asked = False


    def write_report(self, mode='newfile'):
        
        fname = self.username.split()[0]

        if mode == 'newfile':
            with open(f"{fname}_data.txt", 'w') as f:
                f.write(f"Timestamp: {str(datetime.now())} \n")
                # .strftime("%Y%m%d_%H-%M-%S"))}")
                f.write("Operation: Addition\n")
                f.write(f"Number of attempts: {self.stats[0][0]} \n")
                f.write(f"Correct Attempts: {self.stats[0][1]}\n")

                f.write("Operation: Subtraction\n")
                f.write(f"Number of attempts: {self.stats[1][0]} \n")
                f.write(f"Correct Attempts: {self.stats[1][1]}\n")

                f.write("Operation: Multiplication\n")
                f.write(f"Number of attempts: {self.stats[2][0]} \n")
                f.write(f"Correct Attempts: {self.stats[2][1]} \n")

                f.write("Operation: Division\n")
                f.write(f"Number of attempts: {self.stats[3][0]}\n")
                f.write(f"Correct Attempts: {self.stats[3][1]}\n")
                f.write("\n\n\n")


        elif mode == 'duplicate':
            with open(f"{fname}2_data.txt", 'w') as f:
                f.write(f"Timestamp: {str(datetime.now())} \n")
                # .strftime("%Y%m%d_%H-%M-%S"))}")
                f.write("Operation: Addition\n")
                f.write(f"Number of attempts: {self.stats[0][0]} \n")
                f.write(f"Correct Attempts: {self.stats[0][1]}\n")

                f.write("Operation: Subtraction\n")
                f.write(f"Number of attempts: {self.stats[1][0]} \n")
                f.write(f"Correct Attempts: {self.stats[1][1]}\n")

                f.write("Operation: Multiplication\n")
                f.write(f"Number of attempts: {self.stats[2][0]} \n")
                f.write(f"Correct Attempts: {self.stats[2][1]} \n")

                f.write("Operation: Division\n")
                f.write(f"Number of attempts: {self.stats[3][0]}\n")
                f.write(f"Correct Attempts: {self.stats[3][1]}\n")

                f.write("\n\n\n")

        elif mode == 'append':
            with open(f"{fname}_data.txt", 'a') as f:
                f.write(f"Timestamp: {str(datetime.now())} \n")
                # .strftime("%Y%m%d_%H-%M-%S"))}")
                f.write("Operation: Addition\n")
                f.write(f"Number of attempts: {self.stats[0][0]} \n")
                f.write(f"Correct Attempts: {self.stats[0][1]}\n")

                f.write("Operation: Subtraction\n")
                f.write(f"Number of attempts: {self.stats[1][0]} \n")
                f.write(f"Correct Attempts: {self.stats[1][1]}\n")

                f.write("Operation: Multiplication\n")
                f.write(f"Number of attempts: {self.stats[2][0]} \n")
                f.write(f"Correct Attempts: {self.stats[2][1]} \n")

                f.write("Operation: Division\n")
                f.write(f"Number of attempts: {self.stats[3][0]}\n")
                f.write(f"Correct Attempts: {self.stats[3][1]}\n")

                f.write("\n\n\n")


if __name__ == "__main__":
    
    username = input("Please Enter Your Name: ")

    report = Report(username=username)

    print(f"Welcome, {report.username}!")
    
    #Taking number of times user wants to do the operations

    numtime = int(input("So, How many times you will practice this option"))
    
    while numtime>0:
        numtime -= 1
        # Presenting choices
        print("List of Operations:")
        print("1-Addition")
        print("2-Subtraction")
        print("3-Multiplication")
        print("4-Division")
        print("5-Write a Report")
        print("6-View Report")
        print("7-Exit")

       
        # Taking opinion
        options = int(input(f"hey, {username}!, Please enter your choice from above(1/2/3/4/5/6/7): "))
        

        # Exiting on 7th choice
        if options == 7:
            if not report.report_asked:
                exit_choice = input("No report was maintaied, are you sure to quit?(y/n)") 
                if exit_choice =='n':
                    continue
            
            print("Thank you!")
            break

        # Writing to text files
        if options == 5:
            fname = username.split()[0]

            # Checking file existence
            if os.path.isfile(f"{fname}_data.txt"):
                print('Report already exists. Choose an option')
                print('a: Create a new file')
                print('b: Append to the same file')

                choice = input('Enter your choice(a/b): ') 
                # Creating new file
                if choice == 'a':
                    report.write_report(mode='duplicate')

                    
                else:

                    # Appending to existing file
                    report.write_report(mode='append')


                   
            else:
                # Creating new file
                report.write_report(mode='newfile')

                

            report.report_asked = True

            # adding one as creating report doesnt come under operation count
            numtime += 1
            continue             

        # Printing the report
        if options == 6:
            fname = username.split()[0]
            if os.path.isfile(f"{fname}_data.txt"):
                with open(f"{fname}_data.txt", 'r') as f:
                    print(f.read())

            else:
                print("No report was maitained.")

            # adding one as showing report doesnt come under operation count
            numtime+=1
            continue

        # Taking digits choice
        dig = int(input("Choose the number of digits(1/2): "))
        
        # Generating the digits
        n1, n2 = -1, -1
        if dig == 1:
            n1, n2 = gen(1)
        else:
            n1, n2 = gen(dig)

        # Reforming randomly generating digits
        if n2 > n1:
            n1, n2 = n2, n1

        # Presenting the numbers
        print(f"The numbers are: {n1} and {n2}")

        # Seeking the result
        res = input("Please enter the result of the operation: ")

        # Performing the operations according to choices
        correct = -1
        if options == 1:
            correct = add(n1, n2)
            report.stats[0][0]+=1
            if res == correct:
                report.stats[0][1] += 1

        elif options == 2:
            correct = subtract(n1, n2)
            report.stats[1][0]+=1
            if res == correct:
                report.stats[1][1] += 1

        elif options == 3:
            correct = multiply(n1, n2)
            report.stats[2][0]+=1
            if res== correct:
             report.stats[2][1] += 1

        elif options == 4:
            correct = divide(n1, n2)
            report.stats[3][0]+=1
            if res== correct:
             report.stats[3][1] += 1

        # Reinforcers List
        pos_rein = ['Excellent', 'Very Good', 'Well Done', 'Awesome', 'Good Job', 'Correct'] 
        sup_rein = ['Try Again', 'OOPS', 'Not Quite', 'Look at it again', 'Sorry']       
    
        # For correct result
        if res == correct:

            print(random.choice(pos_rein))
            input("Press Enter key to continue")
            continue

        # For incorrect result
        else:
            print(random.choice(sup_rein))
            
            # Asking again
            res2 = input("Re-enter the result of the operation: ")
            if res2 == correct:
                print(random.choice(pos_rein))
            else:
                print(f"The correct answer is {correct}!")
            input("Press Enter key to continue")
            continue

