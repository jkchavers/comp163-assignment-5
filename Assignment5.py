
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
    print("Enter starting number:", starting_num)
    print("Sequence:", sequence)
    print("Steps:", step_count)

#Challenge 2
'''
    current_number = int(input("Enter starting number: "))
    step_count = 0
    
    while current_number >= 1:
        
            if current_number % 2 == 0:
                current_number /= 2
            else:
                current_number = current_number * 3 + 1
    
            step_count += 1
    
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
   
    
   