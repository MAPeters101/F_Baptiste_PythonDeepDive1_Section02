a = [1, 2, 3]
a = [1, 2,
     3, 4, 5]
print(a)
#a = [1 #item,
#    2 ]
a = [1, #item
    2]
a = [1 #item
    ,2]

a = (1 #comment
    ,2 #comment
    ,3)
print(a)
# a = {'key1': 1 #value for key 1
#     ,'key2': 2 #value for key2 }
# print(a)
a = {'key1': 1 #value for key 1
    ,'key2': 2 #value for key2
    }
print(a)
print('-'*80)

def my_func(a, #comment
            b, #comment
            c):
    print(a, b, c)

my_func(10, 20, 30)
my_func(10,
        20,
        30)

my_func(10, #comment
        20, #comment
        30 #comment
        )
print('-'*80)

a = 10
b = 20
c = 30
if a > 5 and b > 10 and c > 20:
    print('yes')

if a > 5 \
    and b > 10 \
        and c > 20:
    print('yes')
print('-'*80)

a = '''this is a string'''
print(a)

a = '''this 
is a string'''
print(a)

a = '''this 
    is a string
        that is created over multiple lines'''
print(a)

a = '''some items:
        1. item 1
        2. item 2'''
print(a)
print('-'*80)

def my_func():
    a = '''a multi-line string
    that is indented in the second line'''
    return a
print(my_func())
print()

def my_func():
    a = '''a multi-line string
that is indented in the second line'''
    return a
print(my_func())




