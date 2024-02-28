"""Calculate the sum of numbers from 1 to n."""

# Interactive Approach
     # Straightforward implementation and easy to understand
     # May not be efficient for large valuers due to the loop interaction
     # Constant memory usage 

def calculate_sum():
    n = int(input("Choose n = "))
    for number in range(1, n): 
        n += number  # Add each number to the total
    print(f"The sum is: {n}")  


# Recursive Approach
    # can handle large values but at the same time consumes more memory
    # May encounter stack overflow for very large values
    # Adds clarity and reduces the time needed to write
    
def calculate_recursive_sum(n):
    if n == 1:  # Base case: if n is 1, return 1
        return 1
    else:
        return n + recursiveSum(n - 1)  # Return n plus the sum of integers from 1 to n-1 recursively
# uncomment the following
# n = int(input("Choose n = "))
# Call the recursive function and print the result
# print("The sum is:", recursiveSum(number))


# Mathematical Implementation
    # Most efficient solution in terms of time complexity, even in a large value
    # No memory overhead
    # Requires knowledge in math to understand the formula and whats been applied

def calculate_math_sum():
    n = int(input("Choose n = ")) # user input
    result = (n * (n + 1)) / 2 # mathematical formula
    print(result) 

# mathSum()
    

# Run code by removing "#"
