''' From Amit shah Doing Math with Python, Sympy equation solver '''

from sympy.plotting import plot
from sympy import Symbol,sympify,solve

expr1=input("Enter your first expression in terms of x and y:\n")
expr2=input('Enter your second expression in terms of x and y:\n')

try:
    expr11=sympify(expr1)
    expr22=sympify(expr2)

except:
    print("Invalid expression(s)")

y=Symbol("y")
thing1=solve(expr11,y)[0]
thing2=solve(expr22,y)[0]

p=plot(thing1,thing2)

answer=solve((expr11,expr22), dict=True)

print("The solution for both the equations are/is {0}".format((answer)))
