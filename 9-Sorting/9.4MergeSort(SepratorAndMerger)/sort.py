import pprint
pp = pprint.PrettyPrinter(indent=4)
# Without Spaces
#str = list(input('Enter Statement:'))

# With Spacees
print('Choice:')
print('1:Integer\n2:Character')
choice = input()
input = list(input('Enter Statement: ').split(' '))
if choice == '1':
    input = [int(i) for i in input]
print('Input Expression:', input)

count=0
def seprator(expression):
    global count
    count+=1
    lb=mid=0
    ub=len(expression)-1
    if lb<ub:
        mid=int((lb+ub)/2)
        preExpression=list()
        postExpression =list()
        for i in range(len(expression)):
            if i<=mid:
                preExpression.append(expression[i])
            elif i>mid:
                postExpression.append(expression[i])
        left=seprator(preExpression)
        right=seprator(postExpression)
        #print(left, right)
        expression=sortThenMerge(left, right)
        return expression
    elif lb==ub:
        #print(list(expression))
        return list(expression)


def sortThenMerge(leftExp, rightExp):
    temp = list()
    i=j=0
    while i<len(leftExp) and j<len(rightExp):
        if leftExp[i]<rightExp[j]:
            temp.append(leftExp[i])
            i+=1
        elif leftExp[i]>=rightExp[j]:
            temp.append(rightExp[j])
            j+=1
    while i==len(leftExp) and j<len(rightExp):
        temp.append(rightExp[j])
        j+=1
    while i<len(leftExp) and j==len(rightExp):
        temp.append(leftExp[i])
        i+=1
    return temp

print('Output Expression:', seprator(input))
