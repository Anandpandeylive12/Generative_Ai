def chai_customers():
    print("Welcome! What chai would you like to have?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_customers()
next(stall)#start the generator
stall.send("Masala Chai")
stall.send("Ginger Chai")
stall.send("Elaichi Chai")
