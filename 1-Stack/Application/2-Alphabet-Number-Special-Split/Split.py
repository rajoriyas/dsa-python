from DynamicStackLinkedList import *

def main():
    stack_special = Stack()
    stack_num = Stack()
    stack_alpha = Stack()

    str = input('String:')
    for s in str:
        if s.isnumeric():
            stack_num.push(s)
        elif s.lower().isalpha():
            stack_alpha.push(s)
        else:
            stack_special.push(s)

    stack_num.display()
    stack_alpha.display()
    stack_special.display()

if __name__ == '__main__':
    main()
