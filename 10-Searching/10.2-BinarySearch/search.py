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
    mid=(lb+ub)//2
    if statement[mid]==element:
        print('['+str(statement[mid])+']', mid)
    elif statement[mid]>element:
        print(statement[lb:mid], lb, mid)
        BinarySearch(statement, element, lb, mid)
    elif statement[mid]<element:
        print(statement[mid+1:ub], mid+1, ub)
        BinarySearch(statement, element, mid+1, ub)

BinarySearch(statement, ele, 0, len(statement))
