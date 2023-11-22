# function with a constant time complexity - O(1)
def give_square(val):
    return val * val

num_to_square = give_square(5)
print(num_to_square)
print()

# function with logarithmic time complexity - O(logn)

# TODO: Binary Search algorithm

# function with linear time complexity - O(n)
def print_items(val):
    for i in range(val):
        print(i)
      
print_items(5)  
print()

# function with a linearithmic time complexity - O(nlogn)

# TODO: sorting algorithms

# function with quadratic time complexity - O(n^2) [Nesting of loops!]
def print_combinations(val):
    for i in range(val):
        for j in range(val):
            print(i, j)

print_combinations(5)
print()

# function with cubic time complexity - O(n^3) [Nesting of loops! x3] 
# !Never Use! # 
def print_combinations_2(val):
    for i in range(val):
        for j in range(val):
            for k in range(val):
                print(i, j, k)

print_combinations_2(5)
print()

# function with exponential time complexity - O(2^n)
def fibonacci_recursive(val):
    if val <= 1:
        return val
    return fibonacci_recursive(val - 1) + fibonacci_recursive(val - 2)

print(fibonacci_recursive(10))
print()