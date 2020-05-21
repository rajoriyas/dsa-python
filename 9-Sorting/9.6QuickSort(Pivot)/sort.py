# Without Spaces
#str = list(input('Enter Statement:'))

# With Spacees
choice = input('1:Integer\n2:Character\nEnter Choice:')
str = list(input('Enter Statement: ').split(' '))
if choice=='1':
    str = [int(s) for s in str]
out = list()
def partition(str):
    left=list()
    right=list()
    if len(str)>1:
        pivot=str[-1]
        str=str[:-1]
        for s in str:
            if s<pivot:
                left.append(s)
            if s>=pivot:
                right.append(s)
        print(pivot, left, right)
        partition(left)
        out.append(pivot)
        partition(right)
        return
    if len(str)==1:
        out.append(str[0])
        return
partition(str)
print(out)
