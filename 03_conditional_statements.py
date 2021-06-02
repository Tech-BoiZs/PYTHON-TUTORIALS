'''
if statement

if-else statement

if-elif statement

'''

'''
if statement syntax

if <condition>:
    statement
'''

'''a=5

if a==4:
    print(a)
'''

# Syntax for if-else statement

'''

if <condition>:
    if statement
else:
    else statement

'''

# greatest of two no a and b

'''
a=5
b=10
if a>b:
    print("a is greatest") # execute when a is greater  
else:
    print("b is greatest") # execute when b is greater
'''

'''

syntax for if-elif

if <condition>:
    if statement
elif <condition>:
    elif statement
else:
    else statement
    
'''

# greatest of three no a, b and c
a=10
b=5
c=17
if a>b: # 10>5 is true goto if
    if a>c: # 10>17 is false goto elif
        print(a) # execute when two conditions are true
    elif b>c: # 5>17 is false goto else
        print(b) # execute when b>c is true
    else: # display c since a<b<c => a<c so, c is greatest
        print(c) # execute when all the given condition are false

    
    

