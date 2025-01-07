def d():
    animal = "elephant"
    def e():
        nonlocal animal
        animal = "giraffe"
        print("Dentro do for aninhando: "+ animal)
    
    print("Antes de chamar a função: " + animal)
    e()
    print("Depois do for aninhado: " + animal)
    
animal = "Camel"
d()
print("Variavel global " + animal)