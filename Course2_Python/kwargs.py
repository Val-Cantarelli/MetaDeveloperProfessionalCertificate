def sum_of(**kwargs):
    sum = 0
    for k,v in kwargs.items():
        sum += v
    return sum 

# options = dict(coffe=2.10,cake=4.55)
options = dict(coffe=2.10,cake=4.55)
print(sum_of(**options))

def sum2_of(*args):
    sum = 0
    for v in args:
        sum += v
    return sum 
print(sum2_of(*[1,2,3,4,5,6]))
    