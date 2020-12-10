# Normal function
'''
def double(x):
    return x*2
print(double(2))
'''
# Lambda Function
'''
square = lambda x:2*x

print(square(20))

'''
'''
addition = lambda x,y:x+y

print(addition(2,3))

mx = lambda x,y:x if x>y else y

print(mx(20,3))
'''
# Map Function in python
'''
n = [1,2,3,4,5]
print(list(map(lambda x:x**2,n)))

'''
'''
n = [1,2,3,4,5]
print([x**2 for x in n])
'''
# filter in python
'''
lst =[1,2,3,4,5,6,7,8]
def even(num):
    if num%2==0:
        return True

print(list(filter(even,lst)))
'''
'''
lst =[1,2,3,4,5,6,7,8]

print(list(filter(lambda x:x%2==0,lst)))
'''
# reduce the number into single number
n =[5,4,3,2,1]
print(reduce(lambda x,y:x*y,n))
















