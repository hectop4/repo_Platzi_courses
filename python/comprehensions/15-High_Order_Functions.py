#HOF 

def increment(number):
    return number + 1

increment_v2=lambda number: number + 1

def high_order_function(func, number):
    result = func(number)
    return number+result

reslut = high_order_function(increment, 2)
print(reslut)

result=high_order_function(increment_v2, 2)
print(result)

result_v2=high_order_function(lambda number: number + 1, 2)
print(result_v2)