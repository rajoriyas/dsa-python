from DynamicStackLinkedList import *
symbol = dict()
symbol['^']=3
symbol['*']=2
symbol['/']=2
symbol['+']=1
symbol['-']=1

stack = Stack()
postfix = Stack()
#check the condition of property
#if inserted symbol has more priority, returns True, means tells for pop

def priority(old, new, val):
    global symbol, stack, postfix
    if old in symbol and new in symbol:
        if symbol[old]>=symbol[new]:
            postfix.push(val)
            return True
        else:
            stack.push(val)
            return False
    else:
        stack.push(val)
        return False

"""
def InfixToPosfix(str):
    global symbol, stack
    for s in str:
        for index, value in symbol.items():
            if s==index:
                if stack.top==-1:
                    stack.push(s)
                elif stack.top>-1:
                    temp=stack.pop()
                    while priority(temp, s, temp) and stack.top>-1:
                        temp=stack.pop()
                    stack.push(s)
                s=None
        if s!=None:
            postfix.push(s)
    while stack.top>-1:
        postfix.push(stack.pop())
    exp = list()
    while postfix.top>-1:
        exp.append(postfix.pop())
    print('Postfix Expression:', sep=' ', end='', flush=True)
    for e in reversed(range(len(exp))):
        print(exp[e], sep=' ', end='', flush=True)
    print('')
"""

def InfixToPosfix(str):
    global symbol, stack, postfix
    for s in str:
        if s=='(':
            stack.push(s)
            s=None
        if s in symbol:
            if stack.top==-1:
                stack.push(s)
                s=None
            elif stack.top>-1:
                temp = stack.pop()
                while priority(temp, s, temp):
                    temp = stack.pop()
                stack.push(s)
                s=None
        if s==')':
            temp=stack.pop()
            while temp!='(' and stack.top>-1:
                postfix.push(temp)
                temp=stack.pop()
            s=None
        if s!=None:
            postfix.push(s)
            s=None
    while stack.top>-1:
        postfix.push(stack.pop())
    final = list()
    while postfix.top>-1:
        final.append(postfix.pop())
    for f in reversed(final):
        if f!='None':
            print(f, sep=' ', end='', flush=True)
    print('')

def main():
    InfixToPosfix(input('Enter Infix Expression:'))

if __name__ == '__main__':
    main()
