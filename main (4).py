def linear_search_product(product_list, target_product):
    indices = []
    for i in range(len(product_list)):
        if product_list[i] == target_product:
            indices.append(i)
    return indices

# Example usage
products = ["apple", "banana", "apple", "orange", "grape", "apple"]
target_product = "apple"

result = linear_search_product(products, target_product)

if result:
    print(f"The product '{target_product}' is found at indices: {result}")
else:
    print(f"The product '{target_product}' is not found in the list.")