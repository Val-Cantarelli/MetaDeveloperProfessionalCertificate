# global scope
my_global= 10

def fn1():
    local_v = 5
    print('Acess to global',my_global)
    
fn1()

