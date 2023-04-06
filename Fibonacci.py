def fibonacci(n):  
    a = 0
    b = 1
    
    while b <= n:
        
        if b == n:
            return True
          
        a = b 
        b = a + b
    
    return False

num = int(input("Digite um número: "))

if fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci!")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci!")