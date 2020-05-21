statement = list(input('Statement:').split(' '))
ele = input('Element:')
#new way of for loop
for index, item in enumerate(statement):
    if item == ele:
        print('Location',index)
