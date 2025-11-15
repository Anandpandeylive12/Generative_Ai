# impure funtion::An impure function is one that:

# May give different outputs for the same inputs (because it depends on external state or random values).

# Has side effects, such as:

# Modifying global variables

# Printing or logging output

# Writing/reading files

# Changing mutable arguments (like lists or dicts)
x = 10

def add_to_global(y):
    global x
    x = x + y  # modifies global variable
    return x




# pure functions:::A pure function is one that:

# Always produces the same output for the same input.

# Does not cause any side effects (i.e., does not modify global variables, write to files, print output, etc.).
def add(a, b):
    return a + b



# Lamda function
# a lambda function is a small, anonymous (nameless) function — often used for short, simple operations.
add = lambda a, b: a + b
print(add(3, 5))   


