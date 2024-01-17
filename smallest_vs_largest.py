def smallest(numbers):
    return min(numbers)

def largest(numbers):
    return max(numbers)

# Example
numbers_list = [7, 10, 9, 11, 23, 8]
small_result = smallest(numbers_list)
large_result = largest(numbers_list)
print((small_result, large_result))
# this output should come out as (7, 23)