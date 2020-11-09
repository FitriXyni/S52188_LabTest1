#ai

def multiply_by_two(x):
    return x * 2


def print_arguments(function):
    print("Arguments are: ", function, " and will return ", multiply_by_two(function))
    return multiply_by_two(function)


augmented_multiply_by_two = int(input("Enter your numbers"))
print_arguments(augmented_multiply_by_two)

#a2

def add_numbers(a, b):
    return a + b

def print_arguments(augmented_add_numbers_a,augmented_add_numbers_b):
    print("Arguments are: ", augmented_add_numbers_a,augmented_add_numbers_b, " and will return ", add_numbers(augmented_add_numbers_a,augmented_add_numbers_b))
    return add_numbers(augmented_add_numbers_a,augmented_add_numbers_b)


augmented_add_numbers_a= int(input("Enter your numbers"))
augmented_add_numbers_b= int(input("Enter your numbers"))
print_arguments(augmented_add_numbers_a,augmented_add_numbers_b)

#b

def multiply_by_three(x):
    return x * 3


def print_arguments(function):
    print("Arguments are: ", function, " and will return ", 2 * (multiply_by_three(function)))
    return 2 * (multiply_by_three(function))


augmented_ultiply_by_three = int(input("Enter your numbers"))
print_arguments(augmented_ultiply_by_three)

#c

def add_numbers(a, b):
    return a + b

def print_arguments(augmented_add_numbers_a,augmented_add_numbers_b):
    print("Arguments are: ", augmented_add_numbers_a,augmented_add_numbers_b, " and will return ", 2 * (add_numbers(augmented_add_numbers_a,augmented_add_numbers_b)))
    return 2 * (add_numbers(augmented_add_numbers_a,augmented_add_numbers_b))


augmented_add_numbers_a= int(input("Enter your numbers"))
augmented_add_numbers_b= int(input("Enter your numbers"))
print_arguments(augmented_add_numbers_a,augmented_add_numbers_b)
