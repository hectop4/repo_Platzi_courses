def sum_with_range(min,max):
    sum=0
    print("Sumando desde ",min," hasta ",max)
    for x in range(min,max+1):
        sum+=x
    return sum

result=sum_with_range(20,30)
result_V2=sum_with_range(result,result+10)
sum_with_range(0,100)

print("La suma es ",result)
print("La suma es ",result_V2)

