# Without Spaces
#str = list(input('Enter Statement:'))
# With Spacees
str = list(input('Enter Statement: ').split(' '))
i=0
while i<len(str)-1:
    if str[i]>str[i+1]:
        temp=str[i]
        str[i]=str[i+1]
        str[i+1]=temp
        i=-1
    i+=1
print(str)
