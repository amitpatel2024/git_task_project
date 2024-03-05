def return_sum(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result


print(return_sum(10))
print(return_sum(10, 20))
print(return_sum(10, 20, 30, 40, 50))
