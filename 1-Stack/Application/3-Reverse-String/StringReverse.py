from DynamicStackLinkedList import *

def main():
    stack = Stack()

    string = input('String:')
    for s in string:
        stack.push(s)
    string=""
    top = stack.top
    while top>-1:
        string += str(stack.pop())
        top-=1
    print('Reversed String:'+string)

if __name__ == '__main__':
    main()
