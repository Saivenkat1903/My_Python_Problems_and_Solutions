''' This code is to approximate the root of a function by using Newton Raphson method. The given function is x**2+e**x which is represented as x**2+exp(x) in sympy
    This function does not have real roots, therefore this method will only give an approximation to the lowest point in an interval choosen.'''

import sympy as sp                                                              #imports library to use as sp

''' Converts the given function to a sympy symbol function and gets necessary input'''

fun=sp.sympify("x**2+exp(x)")                                                   #Turns the function string entered into a sympy object so that sympy methods can be used on it.

'''Ensures that the variable is taken as a symbol'''
x=sp.Symbol(str(list(fun.free_symbols)[0]))                                     #This code extracts the variable in the function and stores it as x. This allows the function to be of any variable not just x

''' We use a loop to ask for the values of a,b in case people enter the wrong values for a,b'''
while True:                                                                     #We use While True to keep the loop running until proper values of a,b are given
  a,b=map(lambda x: float(x),input("Which interval should be used? (for an interval [a,b] please type in 'a b' with a space between them)\n").split())  #This input accepts 2 floats seperated by a space, the map function is to ensure a and b are floats, [a,b] denotes the interval
  if a<b:                                                                       #this checks that a,b are proper by seeing if a<b
    break                                                                       #In the true case, the loop can be broken and we can move to the rest of the code
  else:
    print("Please input floats such that a<b")                                  #If not, the print statement says what is wrong with the values, and the while loop asks for another input

tol=float(input("Enter the tolerence or accuracy required.\n"))                 #This code asks for the tolerance required and converts it to a float

x_o=(a+b)/2                                                                     #This code stores the first value required that is (a+b)/2 as x_o to use in the newton method

f_x=None                                                                        #We make variable f_x and give it a None type so that it can be used in the while loop, else python has no way of verifiying the condition in the while loop

count=0                                                                         #We make a count variable to ensure that the while loop does not run in definitely

while f_x!=0:                                                                   #f_x denotes the value of the function at x_n for n={0,1,2,3,4,...} therefore if it is zero then we are done and have our root. Thus we wantt our condition to be that it doesn't equal 0
  f_x=fun.subs({x:x_o})                                                         #Gives the value of f_x at x_o
  d=sp.Derivative(fun,x).doit().subs({x:x_o})                                   #Gives the value of the derivative of f_x at x_o
  new=x_o-(f_x/d)                                                               #stores the new value of x_1 computed via the newton method in the variable new
  f_new=fun.subs({x:new})                                                       #Gives the value of the function at the new value x_1 calculated previously
  x_o=new                                                                       #This line tells python to now make x_o take the value of new
  f_x=f_new                                                                     #This line tells python to now make f_x take the value of f_new
  print(f_x)                                                                    #This line prints the new value of f_x, this is just to see how the loop goes through values of f_x
  count=count+1                                                                 #This code ensures that each time the loop runs, the count increments by 1
  if f_x <=tol and f_x>=(-1*tol):                                               #This condition checks if the value of f_x falls in the tolerance range speceified, if so the loop breaks
    break                                                                       #Break Statement
  elif count==1000:                                                             #In case the first condiiton isn't fulfilled, this condition ensures that as soon as the loop runs 1000 times, the loop will break. This ensures that infinite loops don't occur
    break                                                                       #Break Statement

if count==1000:                                                                 #To ensure 2 outputs based on how the loop is broken, we add the condition here again
  print("The function does not take any values which are "+str(tol)+" close to 0. Please choose a higher tolerance.")  #Tells the user why we face an error due to the tolerance value being too accurate
else:
  print("An approximation of the root is "+str(x_o))                            #Tells the user the value of approximation of the root
  print("The value of the function at that point is "+str(fun.subs({x:x_o})))   #Tells the user the value of the function at that approximate root

sp.plotting.plot(fun,ylim=[0,10])
