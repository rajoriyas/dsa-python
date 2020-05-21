class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Node():
    def __init__(self, info=None, next=None):
        self.info = info
        self.next = next

class LinkedList():
    def __init__(self, info=None):
        self.temp = Node()
        self.ptr = Node()
        self.node = Node(info=info)

    def insert(self, info, pos=0):
        #check: linklist exists or not
        pos = int(pos)
        if pos==0:
            if not(self.node.info):
                self.node = Node(info=info)
            else:
                self.node = Node(info=info, next=self.node)
        elif pos>0:
            if pos<=self.len():
                i=0
                self.ptr = self.node
                while i<pos-1:
                    self.ptr = self.ptr.next
                    i+=1
                self.ptr.next = Node(info=info, next=self.ptr.next)
            else:
                print(bcolors.FAIL+'Error:Index is out of bound.'+ bcolors.ENDC)

    def append(self, info):
        self.temp = Node(info=info)
        if not(self.node.info):
            self.node = self.temp
        else:
            # when we initialize any datatype by another datatype at the time we just allocate same memory to new one from previous one.
            self.ptr = self.node
            while self.ptr.next:
                self.ptr = self.ptr.next
            self.ptr.next = self.temp

    def delete(self, pos=0):
        pos=int(pos)
        if not(self.node.info):
            self.node = Node()
            print(bcolors.FAIL+'Error:Linked List is not exist.'+ bcolors.ENDC)
        else:
            if pos==0 and self.len()>1:
                self.node = self.node.next
            elif pos==0 and self.len()==1: #if there is a single element
                self.node = Node()
            elif pos>0 and pos<self.len()-1:
                i=0
                self.ptr = self.node
                while i<pos-1:
                    self.ptr = self.ptr.next
                    i+=1
                self.ptr.next = self.ptr.next.next
            elif pos==self.len()-1:
                i=0
                self.ptr = self.node
                while i<pos-1:
                    self.ptr = self.ptr.next
                    i+=1
                self.ptr.next = None
            else:
                print(bcolors.FAIL+'Error:Index is out of bound.'+ bcolors.ENDC)

    def len(self):
        self.ptr = self.node
        count=0
        while self.ptr:
            self.ptr=self.ptr.next
            count+=1
        return count

    def show(self):
        print(bcolors.OKGREEN+'LinkList:'+ bcolors.ENDC, sep=' ', end='', flush=True)
        count=0
        self.ptr = self.node
        while self.ptr:
            print(bcolors.OKBLUE+str(self.ptr.info)+' '+ bcolors.ENDC, sep=' ', end='', flush=True)
            self.ptr=self.ptr.next
            count+=1
        print('')

def main():
    list = LinkedList()
    process=True
    while process:
        print(bcolors.HEADER+'1:Insert\n2:Inject\n3:Append\n4:Delete\n5:Length\n6:Show\n7:Exit'+ bcolors.ENDC)
        try:
            choice=input('press ENTER to continue:')
            if choice=='7':
                process=False
                break
            elif choice=='1':
                list.insert(info=input('Value:'))
            elif choice=='2':
                list.insert(info=input('Value:'), pos=input(bcolors.BOLD+'Position:'+ bcolors.ENDC))
            elif choice=='3':
                list.append(input('Value:'))
            elif choice=='4':
                list.delete(input(bcolors.BOLD+'Position:'+ bcolors.ENDC))
            elif choice=='5':
                len = list.len()
                print('')
                print('Length:',len)
            elif choice=='6':
                list.show()
            else:
                print(bcolors.WARNING+'Alert: Enter Valid Input!'+ bcolors.ENDC)
        except ValueError:
            print(bcolors.WARNING+'Alert: Enter Valid Input!'+ bcolors.ENDC)

if __name__ == '__main__':
    main()
