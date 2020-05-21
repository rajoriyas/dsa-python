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
    def __init__(self, prev=None, info=None, next=None):
        self.prev=prev
        self.info=info
        self.next=next

class DoubleEndedLinkedList():
    def __init__(self):
        self.node=Node()
        self.temp=Node()
        self.ptr=Node()
        self.count=0

    def len(self):
        self.ptr=self.node
        self.count=0
        while self.ptr and self.ptr.info!=None:
            self.count+=1
            self.ptr = self.ptr.next
        return self.count

    def insert(self, info, pos=0):
        pos=int(pos)
        if self.len()==0:
            self.node=Node(info=info)
        else:
            if pos==0:
                self.node=Node(info=info, next=self.node)
                self.node.next.prev=self.node
            elif pos>0 and pos<self.len():
                i=0
                self.ptr=self.node
                while i<pos:
                    self.ptr=self.ptr.next
                    i+=1
                self.ptr.next=Node(info=info, next=self.ptr.next, prev=self.ptr)
                self.ptr.next.next.prev=self.ptr.next
            elif pos==self.len():
                self.append(info)
            else:
                print('Position is out of bound.')

    def append(self, info):
        if self.len()==0:
            self.node=Node(info=info)
        else:
            self.ptr=self.node
            while self.ptr.next:
                self.ptr = self.ptr.next
            self.ptr.next=Node(info=info, prev=self.ptr)

    def delete(self, pos=0):
        pos=int(pos)
        if self.len()==0:
            print('Double Ended Linked List is empty.')
        elif self.len()==1:
            self.node=Node()
        else:
            if pos==0:
                self.node=self.node.next
                self.node.prev=None
            elif pos>0 and pos<self.len()-1:
                i=0
                self.ptr=self.node
                while i<pos-1:
                    self.ptr=self.ptr.next
                    i+=1
                self.ptr.next=self.ptr.next.next
                self.ptr.next.prev=self.ptr
            elif pos==self.len()-1:
                i=0
                self.ptr=self.node
                while i<pos-1:
                    self.ptr=self.ptr.next
                    i+=1
                self.ptr.next=None
            else:
                print('Position is out of bound.')

    def show(self):
        self.ptr=self.node
        self.count=0
        while self.ptr and self.ptr.info!=None:
            print(self.ptr.info+" ", sep=' ', end='', flush=True)
            self.ptr = self.ptr.next
            self.count+=1
        print('\nLength:', self.count)

    def rev_show(self):
        self.ptr=self.node
        self.count=0
        while self.ptr.next:
            self.ptr=self.ptr.next
        while self.ptr:
            self.count-=1
            print(self.ptr.info+" ", sep=' ', end='', flush=True)
            self.ptr=self.ptr.prev
        print('\nLength:', self.count)

def main():
    list = DoubleEndedLinkedList()
    process=True
    while process:
        print(bcolors.HEADER+'1:Insert\n2:Inject\n3:Append\n4:Delete [0-(Length-1)]\n5:Length\n6:Show\n7:Reverse Show\n8:Exit'+ bcolors.ENDC)
        try:
            choice=input('Enter choice:')
            if choice=='8':
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
                print('Length:',len)
            elif choice=='6':
                list.show()
            elif choice=='7':
                list.rev_show()
            else:
                print(bcolors.WARNING+'Alert: Enter Valid Input!'+ bcolors.ENDC)
        except ValueError:
            print(bcolors.WARNING+'Alert: Enter Valid Input!'+ bcolors.ENDC)

if __name__ == '__main__':
    main()
