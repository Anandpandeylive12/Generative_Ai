value = 13


if (remainder := value % 5):
    print(f"{value} is not Divisible be the number 5 and the remainder is {remainder}")


# this walrus  operator (:=) allows you to assign values to variables as part of an expression.


awailable_sizes = ['small', 'medium', 'large', 'extra large']

if (size := 'medium') in awailable_sizes:
    print(f"The size {size} is available.")