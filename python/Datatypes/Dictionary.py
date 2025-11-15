chai_order = dict(type='masala',size= 'Large',sugar=2)
print (f'Chai Order Details:\nType: {chai_order["type"]}\nSize: {chai_order["size"]}\nSugar Level: {chai_order["sugar"]} tsp')

chai_recipe = {}
#adding the value in that dictionary
chai_recipe['milk'] = '150 ml'
chai_recipe['tea_leaves'] = '2 tsp'
chai_recipe['water'] = '200 ml'

print(f'Chai Recipe Ingredients: {chai_recipe}')

del chai_recipe['tea_leaves']
print(f'Updated Chai Recipe Ingredients: {chai_recipe}')
print (f'is sugar in the recipe? {"sugar" in chai_order}')