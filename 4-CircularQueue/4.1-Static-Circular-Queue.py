class CircularQueue():
	def __init__(self, size):
		self.size = size
		self.CircularQueue = [None for i in range(self.size)]
		self.rear = -1
		self.front = -1

	def enqueue(self, val):
			if (self.rear+1)%self.size==self.front:
				return 'Circular Queue is full'
			else:
				if self.front==-1 and self.rear==-1:
					self.rear=self.front=0
				else:
					self.rear=(self.rear+1)%self.size
				self.CircularQueue[self.rear]=val
				return self.CircularQueue, self.rear, self.front

	def dequeue(self):
			if self.front==-1 and self.rear==-1:
				return 'Circular Queue is full'
			else:
				self.CircularQueue[self.front]=None
				if self.rear==self.front:
					self.rear=self.front=-1
				else:
					self.front=(self.front+1)%self.size
			return self.CircularQueue, self.rear, self.front

def main():
	size = int(input('Size:'))
	circularqueue = CircularQueue(size)
	process = True
	while process:
		print('1-Enqueue\t2-Dequeue\t3-Exit')
		choice = input('Choice:')
		if choice == '1':
			print(circularqueue.enqueue(input('Value:')))
		elif choice == '2':
			print(circularqueue.dequeue())
		elif choice == '3':
			process = False
		else:
			print('Please Enter Valid Input.')

if __name__ == '__main__':
	main()
