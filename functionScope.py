                                        #                             ______
a = 10                                  #----------> GLOBAL VARIABLE        |
def some_function():                    #                                  |- both a hv diff SCOPE 
    a = 15                              #----------> LOCAL VARIABLE  _____|
    print("In function, a =", a)        #----------> LOCAL VARIABLE is prioritized here.


some_function()

print("Outside function, a =", a)

############################################################

b = 2

def some_function2():
    global b
    b = 3
    print("In function2, b =", b)

some_function2()

print("outside function2, b =", b)

