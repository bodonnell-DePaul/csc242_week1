x = 4
import random

def double(y):
    x = 2
    x = x+y
    print(x)

def h(n):
    try:
        #HAPPY PATH :-)
        print('Start h')
        print(1/n)
        print(n)
    except ZeroDivisionError as ze:
        #YOU CAN'T DIVIDE BY ZERO
        print(ze.add_note('Hey you can\'t divide by zero'))
        print(ze)
    except Exception as myException:
        #THINGS ARE BROKEN :-(
        print(myException.add_note('Hey you can\'t do that'))
        pass

def g(n):
    print('Start g')
    h(n-1)
    print(n)

def f(n):
    print('Start f')
    g(n-1)
    print(n)

def functionForScope(b):       # f has global scope, b has local scope
    a = 6       # this a has scope local to function call f()
    print(id(a))
    return a*b,'this is so cool', a*a, b*b

print(id(x))
OG, myStr, alltheAs, alltheBs = functionForScope(10)
f(2)
h('hello')
double(10)
print('Global variable: {}'.format(x))


