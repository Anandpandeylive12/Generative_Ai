flavours = ['Ginger','out of Stock', 'Lemon','Discontinued ','tulsi']
for flavour in flavours:
    if flavour == 'out of Stock':
        print(flavour + " is not available right now.")
        continue
    if flavour == 'Discontinued ':
        print(flavour + " has been discontinued.")
        break
    print("Enjoy your " + flavour + " tea!")