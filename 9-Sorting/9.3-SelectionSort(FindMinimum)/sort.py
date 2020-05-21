# Without Spaces
#str = list(input('Enter Statement:'))
# With Spacees
str = list(input('Enter Statement: ').split(' '))
for i in range(0, len(str), 1):
    for j in range(0, len(str), 1):
        if (j>=i):
            if str[i]>str[j]:
                temp = str[i]
                str[i] = str[j]
                str[j] = temp
print(str)
