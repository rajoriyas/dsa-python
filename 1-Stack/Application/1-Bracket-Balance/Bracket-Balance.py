from DynamicStackLinkedList import *

def main():
    stack_parentheses = Stack()
    stack_braces = Stack()
    stack_square = Stack()
    stack_character = Stack()

    open_parantheses = '{'
    close_parantheses = '}'

    open_braces = '('
    close_braces = ')'

    open_square = '['
    close_square = ']'

    str = input('String:')
    for s in str:
        if s==open_braces:
            stack_braces.push(s)
        if s==close_braces and stack_braces.top!=-1:
            stack_braces.push()
        if s==open_parantheses:
            stack_parentheses.push(s)
        if s==close_parantheses and stack_parentheses.top!=-1:
            stack_parentheses.pop()
        if s==open_square:
            stack_square.push(s)
        if s==close_square and stack_square.top!=-1:
            stack_square.pop()
    if stack_braces.top==-1 and stack_parentheses.top==-1 and stack_square.top==-1:
        print('Balance Bracket')
    else:
        print('Unalance Bracket')

if __name__ == '__main__':
    main()
