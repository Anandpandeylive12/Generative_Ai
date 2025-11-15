def serve_chai():
    chai_type = 'Masala'  #Local Scope
    print(f'inside function: Serving a cup of {chai_type} tea.')

chai_type = 'Ginger'  #Global Scope
serve_chai()
print(f'outside function: Serving a cup of {chai_type} tea.')



def chai_counter():
    chai_order='Lemon'
    def print_order():
        chai_order='Tulsi'#inside the nested function only the scope of the this chai_order variable
        print(f'Inner:',chai_order)
    print_order()    
    print('outer:',chai_order)    

chai_counter()   
chai_order='Ginger'#global scope    
chai_counter()
print("global:", chai_order) 