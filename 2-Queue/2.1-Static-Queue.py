class Queue():
	def __init__(self, size):
		self.size = size
		self.Queue = [None for i in range(size)]
		#self.Queue = list()
		self.front = -1	#tells position where data dequeues
		self.rear = -1	#tells position where data enqueues
		self.msg = ''

	def enqueue(self, val):
		if self.rear==self.size-1:
			self.msg = 'Unable to insert, Queue is Full'
			#return 'Queue is Full'
		else:
			self.msg = ''
			if self.front == -1:
				self.front = 0
			self.rear += 1
			self.Queue[self.rear] = val
		#return self.Queue, 'REAR:'+str(self.rear), 'FRONT:'+str(self.front)

	def dequeue(self):
		if self.front==-1:
			self.msg = 'Unable to delete, Queue is empty'
			#return 'Queue is empty'
		else:
			self.msg = ''
			self.Queue[self.front]=None
			if self.front == self.rear:
				self.front = self.rear = -1
			else:
				self.front += 1
		#return self.Queue, 'REAR:'+str(self.rear), 'FRONT:'+str(self.front)

	def display(self):
		if self.msg  != '':
			return self.msg
		temp = list()
		for val in reversed(self.Queue):
			if val != None:
				temp.append(val)
		return 'REAR:'+str(self.rear), temp, 'FRONT:'+str(self.front)

def main():
	size = int(input('Size:'))
	queue = Queue(size)
	process = True
	while process:
		print('1-Enqueue\t2-Dequeue\t3-Exit')
		choice = input('Choice:')
		if choice == '1':
			#print(queue.enqueue(input('Value:')))
			queue.enqueue(input('Value:'))
			print(queue.display())
		elif choice == '2':
			#print(queue.dequeue())
			queue.dequeue()
			print(queue.display())
		elif choice == '3':
			process = False
		else:
			print('Please Enter Valid Input.')

if __name__ == '__main__':
	main()
