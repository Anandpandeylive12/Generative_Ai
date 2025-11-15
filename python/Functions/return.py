def idle_chaiwala():
    return "The chaiwala is idle."


print(idle_chaiwala())

def chai_status(cups_left):
    if cups_left == 0:
        return "Chaiwala is out of chai." 
    return "Chai is ready"


print(chai_status(0))
print(chai_status(5))
