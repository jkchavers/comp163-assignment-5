'''
#Challenge 1
current_number = int(input("Enter starting number: "))
starting_num = current_number
sequence = "Sequence:"
step_count = 0

sequence += " " + str(starting_num)
while current_number > 1:
        
    if current_number % 2 == 0:
        current_number /= 2
        sequence += f" {current_number:.0f}"
    elif current_number % 2 != 0:
        current_number = current_number * 3 + 1
        sequence += f" {current_number:.0f}"
    
    step_count += 1
else:
    #print("Enter starting number:", starting_num)
    print("Sequence:", sequence)
    print("Steps:", step_count)

'''
#Challenge 2
'''
user_number = int(input("Enter a number: "))
step_count = 0
prime = True


for number in range(2,user_number - 1):
    if (user_number % number == 0):
        
        prime = False

        
if prime == True:
    print(user_number," is prime!")
elif prime == False:
    print(user_number,"is not prime")
    

        
    
'''
   
'''
#Challenge 3
current_number = int(input("Enter starting number: "))
step_count = 0
while current_number >= 1:
        
    if current_number % 2 == 0:
        current_number /= 2
    else:
        current_number = current_number * 3 + 1
    
    step_count += 1
'''
   
    
   