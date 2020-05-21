class Queue():
	def __init__(self):
		self.Queue = list()
		self.front = -1	#tells position where data will dequeue
		self.rear = 0	#tells position where data will enqueue

	def enqueue(self, val):
		if self.front == -1:
			self.front = 0
		self.Queue.append(val)
		self.rear += 1
		return self.Queue, 'REAR:'+str(self.rear), 'FRONT:'+str(self.front)

	def dequeue(self):
		self.msg = ''
		self.front += 1
		if(len(self.Queue)==1):
			self.front = -1
			self.rear = 0
			return 'Stack is empty'
		if(len(self.Queue)>1):
			self.Queue.pop(0)
		return self.Queue, 'REAR:'+str(self.rear), 'FRONT:'+str(self.front)

def main():
	queue = Queue()
	process = True
	while process:
		print('1-Enqueue\t2-Dequeue\t3-Exit')
		choice = input('Choice:')
		if choice == '1':
			print(queue.enqueue(input('Value:')))
		elif choice == '2':
			print(queue.dequeue())
		elif choice == '3':
			process = False
		else:
			print('Please Enter Valid Input.')

if __name__ == '__main__':
	main()
