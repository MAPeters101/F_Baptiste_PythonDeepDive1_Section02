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
