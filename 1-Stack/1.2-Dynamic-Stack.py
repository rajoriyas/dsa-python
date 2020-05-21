class Stack():
	def __init__(self):
		self.Stack = list()
		self.top = -1

	def push(self, val):
		self.top += 1
		self.Stack.append(val)
		return "Stack-->>"+str(self.Stack)+"\nTop-->>"+str(self.top)

	def pop(self):
		self.Stack.pop()
		self.top -= 1
		return "Stack-->>"+str(self.Stack)+"\nTop-->>"+str(self.top)

def main():
	stack = Stack()
	process = True
	while process:
		print('1-Push\t2-Pop\t3-Exit')
		choice = input('Choice:')
		if choice == '1':
			print(stack.push(input('Value:')))
		elif choice == '2':
			print(stack.pop())
		elif choice == '3':
			process = False
		else:
			print('Please Enter Valid Input.')

if __name__=="__main__":
	main()
