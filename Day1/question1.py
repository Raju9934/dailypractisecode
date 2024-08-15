def add_without_arithmatic_operator(a,b):
    while b!=0:
        carry=a&b
        a=a^b
        b=carry<<1
        

    return a

result=add_without_arithmatic_operator(12,18)
print(result)

  
