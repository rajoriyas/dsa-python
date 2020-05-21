# Without Spaces
#str = list(input('Enter Statement:'))
# With Spacees
str = list(input('Enter Statement:').split(' '))
for i in range(len(str)):
    for j in range(len(str)):
        if str[i]<str[j]:
            temp=str[i]
            str[i]=str[j]
            str[j]=temp
print(str)
