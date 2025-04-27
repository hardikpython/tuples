def product_of_tuple_values(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Test tuples
tuple1 = (4, 3, 2, 2, -1, 18)
tuple2 = (2, 4, 8, 8, 3, 2, 9)

# Output the results
print("Product of tuple1:", product_of_tuple_values(tuple1))
print("Product of tuple2:", product_of_tuple_values(tuple2))
