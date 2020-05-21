choice = input('1:Integer\n2:Character\nChoice:')
statement = list(input('Statement:').split(' '))
ele = input('Element:')
if choice=='1':
    statement = [int(s) for s in statement]
    ele = int(ele)

#Bubble Sort
def sort(str):
    for i in range(len(str)):
        for j in range(len(str)):
            if str[i]<str[j]:
                str[i], str[j]=str[j], str[i]

sort(statement)
print('Sorted Statement:\n'+str(statement))

def BinarySearch(statement, element, lb, ub):
    pos=int(lb+(float((ub-1-lb)/(statement[ub-1]-statement[lb]))*(element-statement[lb])))
    if statement[pos]==element:
        print('['+str(statement[pos])+']', pos)
    elif statement[pos]>element:
        print(statement[lb:pos], lb, pos)
        BinarySearch(statement, element, lb, pos)
    elif statement[pos]<element:
        print(statement[pos+1:ub], pos+1, ub)
        BinarySearch(statement, element, pos+1, ub)

BinarySearch(statement, ele, 0, len(statement))
