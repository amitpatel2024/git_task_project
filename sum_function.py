def return_sum(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result


def return_product(num1, num2):
    return num1 * num2


print(return_sum(10))
print(return_sum(10, 20))
print(return_sum(10, 20, 30, 40, 50))

print(return_product(10, 20))
print(return_product(35, 45))
