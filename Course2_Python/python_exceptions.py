def divide_by(a,b):
    return  a/b

# Se o divisor for zero, irá retornar um erro. 
# Então, devemos tratar os casos de exceção apropriadamente 

try:
    ans = divide_by(40,0)
except ZeroDivisionError as e:
    print(e, "we cannot divide by zero")
    #print(e.__class__)
except Exception as e:
    print("Something went wrong")