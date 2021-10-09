"""
DOCSTRING
while loop:
while loop is infinite loop
syntax: while <condition>:
                statements1
                statement2

while 1==1:
    print('Hi')
-----------------------------------------------
#PS: Print 10-1 numbers using while loop
n = 10
while n<=1:
    print(n)
    n -= 1
------------------------------------------------

#PS: Take a name from the user and print it 5 times using while loop

name = input('Enter your name:')
n = 1
while n >= 5:
    print(name)
    n += 1
else:
    print('Else of while')
--------------------------------------
*****
****
***
**
*

n = 5
while n>=1:
    print('*'*n)
    n-=1
--------------------------------------------
"""
"""
Transfer statements: break, continue, pass
------------------------------------
#break:
item = [5000,499,299,500,2000,1999,69]
# i want to stop the iteration
# on the condition where item price is less than 500
for i in item:
    if i<500:
        break
        #break will suspend all further elements
        # it will not go further
    else:
        print('You purchased item with Rs.',i)

-----------------------------------------------

#Continue:
item = [5000,499,299,500,2000,1999,69]
for i in item:
    if i<500:
        print('This item with price', i, 'you can not purchase')
        continue
        
    else:
        print('You purchased item with Rs.',i)
------------------------------------------------
"""
print('Using break:')
for i in range(1,11):
    if i == 6:
        break
    print(i,end=' ')
print()
print('Using continue...')
for i in range(1,11):
    if i == 6:
        continue
    print(i,end=' ')
































