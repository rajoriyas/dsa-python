from linkedlist import *
color = bcolors()

class Stack():
    def __init__(self):
        self.stack=LinkedList()
        self.top = -1

    def push(self, info):
        self.stack.insert(info=info)
        self.stack.show()
        self.top += 1
        print('Top :',self.top)

    def pop(self):
        if self.top == -1:
            print(color.WARNING+'Alert: Stack is empty'+color.ENDC)
            return 0
        self.stack.delete()
        self.stack.show()
        self.top -= 1
        print('Top :',self.top)

def main():
    stack = Stack()
    process = True
    while process:
    	print('1-Push\t2-Pop\t3-Exit')
    	choice = input('Choice:')
    	if choice == '1':
    		stack.push(input('Value:'))
    	elif choice == '2':
    		stack.pop()
    	elif choice == '3':
    		process = False
    	else:
    		print('Please Enter Valid Input.')

if __name__ == '__main__':
    main()
