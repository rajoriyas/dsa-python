class Heap():
    def __init__(self, info=None, left=None, right=None):
        self.info=info
        self.left=left
        self.right=right

class HeapOperation():
    def __init__(self):
        self.heap=Heap()
        self.count=0
        self.last=list()

    def maxDepth(self):
        count=0
        ptr = self.heap
        while ptr and ptr.info is not None:
            count+=1
            ptr=ptr.left
        return count

    #Check Only One None at a time
    def NoneParent(self, info, depth, ptr):
        if depth>1 and ptr and ptr.info is not None:
            LeftCheck=RightCheck=False
            if not(ptr.left) or ptr.left is None:
                ptr.left=Heap(info=info)
                return True
            elif not(ptr.right) or ptr.right is None:
                ptr.right=Heap(info=info)
                return True
            elif ptr.left:
                LeftCheck=self.NoneParent(info=info, depth=depth-1, ptr=ptr.left)
                if LeftCheck:
                    return LeftCheck
                elif not(LeftCheck) and ptr.right:
                    RightCheck=self.NoneParent(info=info, depth=depth-1, ptr=ptr.right)
                    return RightCheck
        if depth==1:
            return False

    def append(self, info, ptr):
        if not(ptr.left) or ptr.left.info is None:
            ptr.left=Heap(info=info)
            return
        elif not(ptr.right) or ptr.right.info is None:
            ptr.right=Heap(info=info)
            return
        elif ptr.left:
            self.append(info=info, ptr=ptr.left)
        elif ptr.right:
            self.append(info=info, ptr=ptr.right)

    def insert(self, info):
        depth=self.maxDepth()
        if depth>0:
            if not(self.NoneParent(info=info, depth=depth, ptr=self.heap)):
                self.append(info=info, ptr=self.heap)
        elif depth==0:
            self.heap=Heap(info=info)
        self.Heapify(ptr=self.heap)
        self.show(ptr=self.heap)
        print('')

    def Heapify(self, ptr):
        self.count+=1
        if ptr and ptr.info is not None and ptr.left and ptr.left.info is not None:
            #for min Heap: ptr.info>ptr.left.info
            if ptr.info<ptr.left.info:
                ptr.info, ptr.left.info=ptr.left.info, ptr.info
                self.Heapify(ptr=self.heap)
            else:
                self.Heapify(ptr=ptr.left)
        if ptr and ptr.info is not None and ptr.right and ptr.right.info is not None:
            #for min Heap: ptr.info>ptr.right.info
            if ptr.info<ptr.right.info:
                ptr.info, ptr.right.info=ptr.right.info, ptr.info
                self.Heapify(ptr=self.heap)
            else:
                self.Heapify(ptr=ptr.right)

    def parent(self, info, ptr):
        if ptr and ptr.info is not None:
            if ptr.left and ptr.left.info==info:
                return ptr, "left"
            elif ptr.right and ptr.right.info==info:
                return ptr, "right"
            else:
                prev=dir=None
                if ptr.left:
                    prev, dir=self.parent(info=info, ptr=ptr.left)
                if prev is None and ptr.right:
                    prev, dir=self.parent(info=info, ptr=ptr.right)
                return prev, dir
        else:
            return None, None
    #Left-Righty Child
    def rightMost(self, ptr, depth):
        if depth>1:
            if ptr.left and ptr.left.info is not None:
                self.rightMost(ptr=ptr.left, depth=depth-1)
            if ptr.right and ptr.right.info is not None:
                self.rightMost(ptr=ptr.right, depth=depth-1)
            return
        elif depth==1:
            if ptr and ptr.info is not None:
                self.last.append(ptr.info)
                return

    def delete(self):
        temp=None
        if (not(self.heap.left) or self.heap.left.info is None) and (not(self.heap.right) or self.heap.right.info is None):
            temp, self.heap.info = self.heap.info, None
        else:
            if self.heap.left and self.heap.left is not None:
                self.rightMost(ptr=self.heap.left, depth=self.maxDepth()-1)
                prev, dir=self.parent(info=self.last[-1], ptr=self.heap)
                if dir=="left":
                    temp, self.heap.info, prev.left.info=self.heap.info, prev.left.info, None
                elif dir=="right":
                    temp, self.heap.info, prev.right.info=self.heap.info, prev.right.info, None
            if (not(self.heap.left) or self.heap.left.info is None) and (self.heap.right and self.heap.right.info is not None):
                self.heap.left, self.heap.right = self.heap.right, None
        self.Heapify(ptr=self.heap)
        return temp

    def sorting(self):
        sortedList=list()
        while self.heap and self.heap.info is not None:
            sortedList.append(self.delete())
        print(sortedList)

    def show(self, ptr):
        if not(ptr) or ptr.info is None:
            return
        self.show(ptr=ptr.left)
        print(ptr.info, " ", sep=" ", end="", flush=True)
        self.show(ptr=ptr.right)

def main():
    heap = HeapOperation()
    process=True
    while process:
        print('1:Insert\n2:Delete\n3:Show\n4:Sorting\n5:Exit')
        choice=input('Choice:')
        if choice=='5':
            process=False
            break
        elif choice=='1':
            heap.insert(info=int(input('Value:')))
        elif choice=='2':
            heap.delete()
        elif choice=='3':
            heap.show(ptr=heap.heap)
            print("")
        elif choice=='4':
            heap.sorting()


if __name__ == '__main__':
    main()
