def d():
    animal = "elephant"
    def e():
        nonlocal animal
        animal = "giraffe"
        print("Inside the nested function: " + animal)
    
    print("Before calling the function: " + animal)
    e()
    print("After the nested function: " + animal)
    
animal = "Camel"
d()
print("Global variable: " + animal)