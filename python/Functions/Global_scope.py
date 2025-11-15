chai_type = 'Plain'
def front_desk():
    def Kitchen():
        global chai_type    
        chai_type = 'Masala'
    Kitchen()    
    print(f'Front Desk: Serving a cup of {chai_type} tea.')

front_desk()
print(f'Global Scope: Serving a cup of {chai_type} tea.')