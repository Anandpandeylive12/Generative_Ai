def chai_flavor(flavor='masala'):
    """Return the flavor of chai."""
    chai='ginger'
    return flavor

print(chai_flavor.__doc__)   #dundur doc
print(chai_flavor.__name__)   #dundur Name


def generate_bill(chai=0,samosa=0):
    """
    Calculate the total billfor chai and samosa

    :param Chai: Number of chai cups (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    : return:(total amount , thank you message as a string)
    """
    total = chai*10 + samosa*15
    return total, 'Thank you for visiting org.com'