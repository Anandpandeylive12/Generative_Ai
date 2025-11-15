def update_order():
    chai_type = 'Elaichi'
    def Kitchen():
        nonlocal chai_type
        chai_type = 'Kashmiri'
    Kitchen()
    print(f'Order updated to: {chai_type} tea.')

update_order()