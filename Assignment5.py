#Challenge 1
print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
starting_num = current_number
sequence = ""
step_count = 0

sequence += " " + str(starting_num)#Sets the starting number in the sequence as a string value
while current_number > 1:#stops when current_number is equal to 1
        
    if current_number % 2 == 0:#if current_number is even 
        current_number /= 2 #divide current_number by 2
        sequence += f" {current_number:.0f}"#Appends the new current_number to the sequence string
    elif current_number % 2 != 0:#if current_number is odd 
        current_number = current_number * 3 + 1 #Multiply current_number by 3 and add 1
        sequence += f" {current_number:.0f}"#Appends the new current_number to the sequence string
    
    step_count += 1#increments steps by 1
else:
    #print("Enter starting number:", starting_num)
    print(f"Sequence:{sequence}")
    print("Steps:",step_count)


#Challenge 2
print()
print("=== Challenge 2: Prime Number Checker ===")
user_number = int(input("Enter a number: "))
step_count = 0
prime = True


for number in range(2,user_number - 1):#returns all numbers between 2 and the user number minus 1
    if (user_number % number == 0):#tests user number against a divisor returned from the range funtion in the for loop
        
        prime = False #sets prime to False if a remainder is found. Thus proving the number is not prime

        
if prime == True: #prime boolean is always set to true unless changed in the for loop as a result of having a divisor.
    print(f"Testing divisors from 2 to {user_number - 1}...")
    print(f"{user_number} is prime!")
elif prime == False:
    print(f"Testing divisors from 2 to {user_number - 1}... {user_number} is not prime (divisible by 3)")

#Challenge 3
print()
print("=== Challenge 3: Multiplication Table ===")
baseNums = [1,2,3,4,5,6,7,8,9,10]

rowString = ""

print("Multiplication Table")

for headerNum in range(0,10):#Header row formatting
    print(f"{baseNums[headerNum]:3}",end="")
    
print()

for row in range(0,10):

    print(f"{baseNums[row]:2}",end="")#prints the row with the starting value

    for column in range(0,10):

        print(f"{baseNums[row] * baseNums[column]:4}",end="")#This calculates and returns a product from left to right. Then return to outer for loop until the last iteration
    
    print()

   
    
   