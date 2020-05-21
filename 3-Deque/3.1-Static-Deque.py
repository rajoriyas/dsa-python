class Deque():
	def __init__(self, size):
		self.size = size
		self.Deque = [None for i in range(size)]
		#self.Deque = list()
		self.rear = -1
		self.front = -1

	def insertFront(self, val):
		if self.front == 0 and self.rear == self.size-1:
			return 'Deque is full'
		else:
			if(self.front==-1 and self.rear==-1):
				self.front=self.rear=0
			else:
				if(self.front==0 and self.rear!=self.size-1):	#if first element, in forward direction, is occupied
					for i in reversed(range(self.front, self.rear+1)):
						self.Deque[i+1]=self.Deque[i]
					self.rear+=1
				elif(self.front>0):	#if first element, in forward direction, is not occupied
					self.front-=1
			self.Deque[self.front] = val
			return self.Deque, 'REAR:'+str(self.rear), 'FRONT:'+str(self.front)

	def insertRear(self, val):
		if self.front == 0 and self.rear == self.size-1:
			return 'Deque is full'
		else:
			if(self.front==-1 and self.rear==-1):
				self.front=self.rear=0
			else:
				if(self.rear==self.size-1 and self.front!=0):	#if first element, in backward direction, is occupied
					for i in range(self.front, self.rear+1):
						self.Deque[i-1]=self.Deque[i]
					self.front -= 1
				if(self.rear<self.size-1):
					self.rear += 1
			self.Deque[self.rear] = val
		return self.Deque, 'REAR:'+str(self.rear), 'FRONT:'+str(self.front)

	def deleteFront(self):
		if self.front == -1:
			return 'Deque is empty,', 'REAR:'+str(self.rear), 'FRONT:'+str(self.front)
		else:
			self.Deque[self.front] = None
			if self.front == self.rear:
				self.front = self.rear = -1
			else:
				self.front += 1
		return self.Deque, 'REAR:'+str(self.rear), 'FRONT:'+str(self.front)

	def deleteRear(self):
		if self.front == self.rear+1 or self.front == -1:
			self.front=-1
			self.rear=-1
			return 'Deque is empty', 'REAR:'+str(self.rear), 'FRONT:'+str(self.front)
		else:
			"""
			for i in range(self.front, self.rear-1):
				self.Deque[i]=self.Deque[i+1]
			self.Deque[self.rear-1] = None
			"""
			self.Deque[self.rear] = None
			if self.front == self.rear:
				self.front = self.rear = -1
			else:
				self.rear -= 1
		return self.Deque, 'REAR:'+str(self.rear), 'FRONT:'+str(self.front)

def main():
	size = int(input('Size:'))
	deque = Deque(size)
	process = True
	while process:
		print('1-InsertFront\t2-InsertLast\t3-DeleteFront\t4-DeleteLast\t5-Exit')
		choice = input('Choice:')
		if choice == '1':
			print(deque.insertFront(input('Value:')))
		elif choice == '2':
			print(deque.insertRear(input('Value:')))
		elif choice == '3':
			print(deque.deleteFront())
		elif choice == '4':
			print(deque.deleteRear())
		elif choice == '5':
			process = False
		else:
			print('Please Enter Valid Input.')

if __name__ == '__main__':
	main()
