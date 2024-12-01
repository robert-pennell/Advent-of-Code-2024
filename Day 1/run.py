# Read in file and separate each column into its own list
with open("input.txt", "r") as file: # Open file for reading
    lines = file.readlines() # Read each line
    firstColumn = [] # First column
    secondColumn = [] # Second column
    for line in lines: # For every line in file
        cols = line.strip().split() # Strip whitespace and split columns
        firstColumn.append(cols[0]) # Organize into firstColumn
        secondColumn.append(cols[1]) # Organize into secondColumn

# Sort both columns from lowest to highest
firstSorted = sorted(firstColumn)
secondSorted = sorted(secondColumn)

sum = 0 # Sum for Part 1

# Iterate through the lowest of each column
for firstNum, secondNum in zip(firstSorted, secondSorted):
    sum += abs(int(firstNum) - int(secondNum)) # Add together the differences
    
print(f"Part 1 = {sum}") # Print Part 1 answer
    
# Part 2
sum2 = 0 # Sum for Part 2

# Iterate through each number in the first column to find
# how many instances are in the second column
for firstNum in firstSorted: # For every number in first column
    iterate = 0 # Number of iterations
    for secondNum in secondSorted: # For every number in second column
        if firstNum == secondNum: # If the numbers are equal
            iterate += 1 # Add iteration
    sum2 += int(firstNum) * iterate # Multiply first number by iterations

print(f"Part 2 = {sum2}") # Print Part 2 answer
        
          
