optional={'ginger','clove','nutmeg'}
spices={'cinnamon','clove','allspice','nutmeg','ginger'}

allspices=optional | spices
print(f'all spices :{allspices}')
common_spices=optional & spices      
print(f'common_spices: {common_spices}')