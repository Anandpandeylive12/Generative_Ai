try:
    value = 10
    result = 10 / value
except ValueError:
    print("Input wasn't an integer.")
except ZeroDivisionError:
    print("Can't divide by zero.")
except (TypeError, OverflowError) as e:  # grouping
    print("Other numeric problem:", e)
else:
    print("Result:", result)
finally:
    print("Done.")
