def print_name(full_name):
    print(f'Hello, {full_name}')

# name = input('Enter your name: ')

# print_name(name)

def print_names(name1, name2):
    print(f'Hello, {name1} and {name2}')

print_names("Kaylee", "Ben")

def abc(*args):
    print('hello')
    print(args[0])
   # for name in args:
    #    print(name)

abc()
# abc('a')
# abc('a', 'b','c', 'd', 'e')

#def addition (*args):
 #   print(sum(args))

# addition(1,2,3,4,5,6)

# my_list[n-1]
my_list = [1, 2, 3, 4, 'a', 'b', 'c']
'c' = my_list[7-1] # =6 


def addition(n1, n2):
    print(n1)
    print(n2)
    print(n1+n2)

addition(3,2)
