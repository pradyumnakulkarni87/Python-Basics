# if elif and else use for building a small application: Laptop purchase

name = input('You good name please')
print('Hello',name,'Welcome to our online shop XYZ')

budget = float(input('What is your budget:Rs.'))

print('***Good, well we have following options...****')

if budget>=35000:
    print('In this, we have 3 options')
    print('1. Sony\n2. Dell\n3.Lenovo\n')
    choice= int(input('Please select your choice:'))
    if choice==1:
        print('Great you have choosen Sony')
        ram= int(input('How much RAM size you needed:'))
        if ram==8:
            print('Your total cost is:Rs.45999/-')               


elif budget>=25000:#less than 35k to 25k
    print('In this, we have 3 options')
    print('1.Dell\n2.HP\n3.Asus')

else:
    print('We also give second hand laptops')
    print('If you interested then contact on: 2323435')

    
    
    
    
