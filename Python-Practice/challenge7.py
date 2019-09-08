#Write Python code which accepts name of a product and in turn returns their respective prices.
#Make sure to use dictionaries to store products and their respective prices.
#The dictionary should include at least 5 elements.
products = {"Chair":40, "Sofa": 500, "Table": 90, "Monitor": 100 , "Carpet": 200}
newproduct = input('Enter product name')
if(newproduct in products):
    print(products.get(newproduct))
else:
    print('Product Not Found')
