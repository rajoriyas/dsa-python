class PriorityQueue():
    def __init__(self, len):
        self.front=-1
        self.rear=-1
        self.len=len
        self.Queue = [None for i in range(self.len)]
        self.Priority = [0 for i in range(self.len)]
        self.maxPriority = 0

    def insert(self, info, priority):
        if self.rear==(self.len-1):
            print('Priority Queue is overflow.')
        else:
            if self.rear==-1 and self.front==-1:
                self.front+=1
            self.rear+=1
            self.Queue[self.rear]=info
            self.Priority[self.rear]=priority

    def delete(self):
        if self.front==-1:
            print('Priority Queue is underflow.')
        else:
            temp=0
            for i in range(self.front, self.rear+1):
                if self.maxPriority < self.Priority[i]:
                    self.maxPriority = self.Priority[i]
                    temp=i
            for t in range(temp, self.front, -1):
                self.Queue[t]=self.Queue[t-1]
                self.Priority[t]=self.Priority[t-1]
            self.Queue[self.front]=None
            if self.front==self.rear:
                self.front=-1
                self.rear=-1
            else:
                 self.front+=1
            self.maxPriority=0

    def show(self):
        if self.rear!=-1 and self.front!=-1:
            for i in range(self.front, self.rear+1):
                print('(Element:'+str(self.Queue[i])+', Priority:'+str(self.Priority[i])+') ', sep=' ', end='', flush=True)
            print('')
        else:
            print('')


def main():
    queue = PriorityQueue(int(input('Size:')))
    process = True
    while process:
        print('1:Insert\n2:Delete\n3:Show\n4:Exit')
        choice = input('Choice:')
        if choice == '1':
        	queue.insert(input('Value:'), int(input('Priority(>0):')))
        elif choice == '2':
        	queue.delete()
        elif choice == '3':
            queue.show()
        elif choice == '4':
        	process = False
        else:
        	print('Please Enter Valid Input.')

if __name__ == '__main__':
    main()
