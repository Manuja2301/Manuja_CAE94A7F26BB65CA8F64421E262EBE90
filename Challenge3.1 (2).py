def linear_search_product(product_list, target_product):
    indices = []
    
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    
    return indices

# Example usage:
products = ["Rose", "Jasmine", "Rose", "Sunflower ", "white Rose", "Rose"]
target = "Rose"
result = linear_search_product(products, target)
print( result)