# Without Spaces
#str = list(input('Enter Statement:'))

# With Spacees
choice = input('1:Integer\n2:Character\nEnter Choice:')
str = list(input('Enter Statement: ').split(' '))
if choice=='1':
    str = [int(s) for s in str]

interval=len(str)//2
def compare(str, interval):
    if interval>0:
        i=0
        while i<len(str):
            if (i+interval)<len(str) and str[i]>str[i+interval]:
                temp=str[i]
                str[i]=str[i+interval]
                str[i+interval]=temp
            i+=1
        compare(str, interval//2)
    if interval==0:
        i=0
        while i<len(str)-1:
            if str[i]>str[i+1]:
                temp=str[i]
                str[i]=str[i+1]
                str[i+1]=temp
            i+=1
compare(str, interval)
print(str)
