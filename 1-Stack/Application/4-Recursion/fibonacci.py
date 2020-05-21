from DynamicStackLinkedList import *
from linkedlist import *
stack = Stack()
color = bcolors()
class Fibonacci():
    def recursion(self, num):
        if num==1:
            return 1
        return num*self.recursion(num-1)

    def stack(self, num):
        while num>0:
            stack.display()
            stack.push(num)
            num-=1
        fibonacci=1
        top = stack.top
        while top>-1:
            stack.display()
            fibonacci *= int(stack.pop())
            top -= 1
        return fibonacci


def main():
    num =int(input('Number: '))
    fibonacci = Fibonacci()
    print(color.WARNING+'Fibonacci using Recursion:'+color.ENDC, fibonacci.recursion(num))
    print(color.WARNING+'Fibonacci using Stack:'+color.ENDC, fibonacci.stack(num))

if __name__ == '__main__':
    main()
