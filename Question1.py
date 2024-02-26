# Interactive Approach
    # Straightforward implementation and easy to understand
    # May not be efficient for large valuers due to the loop interaction
    # Constant memory usage

def sum():
    number = int(input("Choose n = "))
    for x in range(1, number):  # Loop through numbers from 1 to number
        number += x  # Add each number to the total
    print(f"The sum is: {number}")  


# Recursive Approach
    # can handle large values but at the same time consumes more memory
    # May encounter stack overflow for very large values
    # Adds clarity and reduces the time needed to write
    
def recursiveSum(n):
    if n == 1:  # Base case: if n is 1, return 1
        return 1
    else:
        return n + recursiveSum(n - 1)  # Return n plus the sum of integers from 1 to n-1 recursively

# number = int(input("Choose n = "))
# Call the recursive function and print the result
# print("The sum is:", recursiveSum(number))


# Mathematical Implementation
    # Most efficient solution in terms of time complexity, even in a large value
    # No memory overhead
    # Requires knowledge in math to understand the formula and whats been applied

def mathSum():
    n = int(input("Choose n = ")) # user input
    result = (n * (n + 1)) / 2 # mathematical formula
    print(result) # print result

# mathSum()
    

# Run code by removing "#"
