def add_without_arithmetic_operators(a, b):
    while b != 0:
       
        carry = a & b
        
        
        a = a ^ b
        
        
        b = carry << 1
    
    return a


result = add_without_arithmetic_operators(15, 25)
print(result)  
