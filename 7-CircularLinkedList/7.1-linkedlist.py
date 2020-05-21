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
        self.info=info
        self.next=next

class CircularLinkedList():
    def __init__(self):
        self.ptr=Node()
        self.temp=Node()
        self.node=Node()
        self.node.next=self.node

    def len(self):
        self.ptr=self.node
        count=0
        while self.ptr.info!=None:
            count+=1
            if self.ptr.next==self.node:
                break
            self.ptr=self.ptr.next
        return count

    #pos=pos-1 because indexing starts from 0
    def insert(self, info, pos=1):
        pos=int(pos)-1
        if self.len()==0:
            self.node=Node(info=info)
            self.node.next=self.node
            #print(self.len())
        elif self.len()>0:
            if pos==0:
                self.temp=Node(info=info, next=self.node)
                self.ptr=self.node
                process=True
                while process and self.ptr.info!=None:
                    if self.ptr.next==self.node:
                        process=False
                        break
                    self.ptr=self.ptr.next
                self.ptr.next=self.temp
                self.node=self.temp
            elif pos>0:
                if pos==self.len():
                    self.ptr=self.node
                    process=True
                    while process and self.ptr.info!=None:
                        if self.ptr.next==self.node:
                            process=False
                            break
                        self.ptr=self.ptr.next
                    self.ptr.next=Node(info=info, next=self.node)
                elif pos<self.len():
                    i=0
                    self.ptr=self.node
                    while i<pos-1:
                        self.ptr=self.ptr.next
                        i+=1
                    self.ptr.next=Node(info=info, next=self.ptr.next)
                else:
                    print(bcolors.WARNING+'Index is out of bound.'+bcolors.ENDC)
            else:
                print(bcolors.WARNING+'Index is out of bound.'+bcolors.ENDC)
        self.show()

    def append(self, info):
        if self.len()==0:
            self.node=Node(info=info)
            self.node.next=self.node
        elif self.len()>0:
            self.ptr=self.node
            process=True
            while process and self.ptr.info!=None:
                if self.ptr.next==self.node:
                    process=False
                    break
                self.ptr=self.ptr.next
            self.ptr.next=Node(info=info, next=self.node)
        self.show()

    #pos=pos-1 because indexing starts from 0
    def delete(self, pos):
        pos=int(pos)-1
        if self.len()==0:
            print('Circular Linked List is empty.')
        elif self.len()==1 and pos==0:
            self.node=Node()
        elif self.len()>1 and pos==0:
            self.ptr=self.node
            process=True
            while process and self.ptr.info!=None:
                if self.ptr.next==self.node:
                    process=False
                    break
                self.ptr=self.ptr.next
            self.ptr.next=self.node.next
            self.node=self.node.next
        elif pos>0 and pos<self.len():
            i=0
            self.ptr=self.node
            while i<pos-1:
                self.ptr=self.ptr.next
                i+=1
            self.ptr.next=self.ptr.next.next
        elif pos==self.len():
            self.ptr=self.node
            process=True
            while process and self.ptr.info!=None:
                if self.ptr.next==self.node:
                    process=False
                    break
                self.ptr=self.ptr.next
            self.ptr=self.node
        else:
            print(bcolors.WARNING+'Index is out of bound.'+bcolors.ENDC)
        self.show()

    def show(self):
        self.ptr=self.node
        process=True
        while process and self.ptr.info!=None:
            print(self.ptr.info, " ", sep=" ", end="", flush=True)
            self.ptr=self.ptr.next
            if self.ptr==self.node:
                process=False
        print('')

def main():
    list = CircularLinkedList()
    process=True
    while process:
        print(bcolors.WARNING+'Note* Position Starts From:1'+ bcolors.ENDC)
        print(bcolors.HEADER+'1:Insert\n2:Inject\n3:Append\n4:Delete\n5:Length\n6:Show\n7:Exit'+ bcolors.ENDC)
        try:
            choice=input('Enter Choice:')
            if choice=='7':
                process=False
                break
            elif choice=='1':
                list.insert(info=input('Value:'))
            elif choice=='2':
                list.insert(info=input('Value:'), pos=input(bcolors.BOLD+'Position:'+ bcolors.ENDC))
            elif choice=='3':
                list.append(info=input('Value:'))
            elif choice=='4':
                list.delete(pos=input(bcolors.BOLD+'Position:'+ bcolors.ENDC))
            elif choice=='5':
                print('Length:', list.len())
            elif choice=='6':
                list.show()
            else:
                print(bcolors.WARNING+'Alert: Enter Valid Input!'+ bcolors.ENDC)
        except ValueError:
            print(bcolors.WARNING+'Alert: Enter Valid Input!'+ bcolors.ENDC)

if __name__ == '__main__':
    main()
