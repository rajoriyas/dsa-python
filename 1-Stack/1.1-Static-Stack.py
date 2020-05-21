class Stack():
	def __init__(self, size):
		self.size = size
		self.Stack = [None for i in range(size)]
		self.top = -1

	def push(self, val):
		if self.top == self.size-1:
			return "Stack is full."
		self.top += 1
		self.Stack[self.top] = val
		return "Stack-->>"+str(self.Stack)+"\tTop-->>"+str(self.top)

	def pop(self):
		if self.top == -1:
			return "Stack is empty."
		self.Stack[self.top] = None
		self.top -= 1
		return "Stack-->>"+str(self.Stack)+"\tTop-->>"+str(self.top)

def main():
	stack = Stack(int(input('Size:')))
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
