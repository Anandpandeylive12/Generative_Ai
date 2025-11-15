users=[
    {'id':1,'total':100,'Coupon':'F40'},
    {'id':2,'total':50,'Coupon':'F10'},
    {'id':3,'total':75,'Coupon':'P10'},
    {'id':4,'total':200,'Coupon':'F50'},
]
discounts={
    'P20':(0.2,0),
    'P10':(0.1,50),
    'F50':(0.05,20),
}

for user in users:
    percent,fixed = discounts.get(user['Coupon'],(0,0))
    discount = user['total'] * percent + fixed  
    print(f"User {user['id']} gets a discount of {discount}.")