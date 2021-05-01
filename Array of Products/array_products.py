def arrayOfProducts(array):
    # Write your code here.

    left_products = [1 for _ in range(len(array))]
    for i in range(1, len(array)):
        left_products[i] = left_products[i-1] * array[i-1]

    right_products = [1 for _ in range(len(array))]
    for i in reversed(range(0, len(array)-1)):
        right_products[i] = right_products[i+1] * array[i+1]

    products = [1 for _ in range(len(array))]
    for i in range(len(array)):
        products[i] = left_products[i] * right_products[i]

    print(left_products)
    print(right_products)
    return products


print(arrayOfProducts([5, 1, 4, 2]))
