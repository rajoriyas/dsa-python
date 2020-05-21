class Node():
    def __init__(self,  left=None, info=None, right=None, bf=0):
        self.left=left
        self.info=info
        self.right=right
        # Balance Factor
        self.bf=bf

class CompleteBinaryTree():
    def __init__(self):
        self.node=Node()
        self.ptr=Node()
        self.last=list()

    def maxDepth(self, ptr, depth=0):
        if ptr and ptr.info is not None:
            depth+=1
            leftDepth=0
            rightDepth=0
            if ptr.left and ptr.left.info is not None:
                leftDepth=self.maxDepth(ptr=ptr.left, depth=depth)
            if ptr.right and ptr.right.info is not None:
                rightDepth=self.maxDepth(ptr=ptr.right, depth=depth)
            if leftDepth!=0 or rightDepth!=0:
                return max(leftDepth, rightDepth)
            else:
                return depth
        else:
            return depth

    def insert(self, info, ptr):
        if not(self.node) or self.node.info is None:
            self.node=Node(info=info)
        else:
            if ptr.info>info:
                if not(ptr.left) or ptr.left.info is None:
                    ptr.left=Node(info=info)
                else:
                    self.insert(info=info, ptr=ptr.left)
            elif ptr.info<info:
                if not(ptr.right) or ptr.right.info is None:
                    ptr.right=Node(info=info)
                else:
                    self.insert(info=info, ptr=ptr.right)
            else:
                print('Element already exixts.')
            ptr.bf=self.maxDepth(ptr=ptr.left)-self.maxDepth(ptr=ptr.right)
            self.rotate(ptr=ptr)
            return

    def rotationPath(self, ptr, depth=0, dir=""):
        if ptr and ptr.info is not None:
            depth+=1
            leftDepth=0
            rightDepth=0
            if ptr.left and ptr.left.info is not None:
                leftDepth, dir=self.rotationPath(ptr=ptr.left, depth=depth, dir=dir)
            if ptr.right and ptr.right.info is not None:
                rightDepth, dir=self.rotationPath(ptr=ptr.right, depth=depth, dir=dir)
            if leftDepth>rightDepth:
                dir+="L"
                return leftDepth, dir
            elif leftDepth<rightDepth:
                dir+="R"
                return rightDepth, dir
            else:
                return depth, dir
        else:
            return depth, dir

    def CalculateBalanceFactor(self, ptr):
        if ptr and ptr.info is not None:
            leftDepth=rightDepth=0
            if ptr.left and ptr.left.info is not None:
                self.CalculateBalanceFactor(ptr=ptr.left)
                leftDepth=self.maxDepth(ptr=ptr.left)
            if ptr.right and ptr.right.info is not None:
                self.CalculateBalanceFactor(ptr=ptr.right)
                rightDepth=self.maxDepth(ptr=ptr.right)
            ptr.bf=leftDepth-rightDepth
            return


    def rotate(self, ptr):
        if abs(ptr.bf)>=2:
            depth, dir=self.rotationPath(ptr=ptr)
            dir=dir[::-1]   # Reversed String

            # Left Rotate
            if dir[:2]=="LL":
                temp=Node(info=ptr.info, right=ptr.right if ptr.right and ptr.right.info is not None else None)
                #temp.bf=self.maxDepth(ptr=temp.left)-self.maxDepth(ptr=temp.right)
                self.CalculateBalanceFactor(ptr=self.node)

                ptr.info, ptr.left, ptr.right = ptr.left.info, ptr.left.left, ptr.left.right

                ptr2 = ptr.right
                if ptr2 and ptr2.info is not None:
                    while ptr2.right and ptr2.right.info is not None:
                        ptr2 = ptr2.right
                    ptr2.right = temp
                else:
                    ptr.right = temp

                #ptr.right.bf=self.maxDepth(ptr=ptr.right.left)-self.maxDepth(ptr=ptr.right.right)
                #ptr.left.bf=self.maxDepth(ptr=ptr.left.left)-self.maxDepth(ptr=ptr.left.right)
                #ptr.bf=self.maxDepth(ptr=ptr.left)-self.maxDepth(ptr=ptr.right)
                self.CalculateBalanceFactor(ptr=self.node)
                self.rotate(ptr=ptr.right)

            # Right Rotate
            if dir[:2]=="RR":
                temp=Node(info=ptr.info, left=ptr.left if ptr.left and ptr.left.info is not None else None)
                #temp.bf=self.maxDepth(ptr=temp.left)-self.maxDepth(ptr=temp.right)
                self.CalculateBalanceFactor(ptr=self.node)

                ptr.info, ptr.right, ptr.left = ptr.right.info, ptr.right.right, ptr.right.left

                ptr2 = ptr.left
                if ptr2 and ptr2.info is not None:
                    while ptr2.left and ptr2.left.info is not None:
                        ptr2 = ptr2.left
                    ptr2.left = temp
                else:
                    ptr.left = temp

                #ptr.right.bf=self.maxDepth(ptr=ptr.right.left)-self.maxDepth(ptr=ptr.right.right)
                #ptr.left.bf=self.maxDepth(ptr=ptr.left.left)-self.maxDepth(ptr=ptr.left.right)
                #ptr.bf=self.maxDepth(ptr=ptr.left)-self.maxDepth(ptr=ptr.right)
                self.CalculateBalanceFactor(ptr=self.node)
                self.rotate(ptr=ptr.left)

            # Left-Right Rotate
            if dir[:2]=="LR":
                ptr.info, ptr.right = ptr.left.right.info, Node(info=ptr.info, right=ptr.right if ptr.right and ptr.right.info is not None else None)
                #ptr.right.bf=self.maxDepth(ptr=ptr.right.left)-self.maxDepth(ptr=ptr.right.right)
                self.CalculateBalanceFactor(ptr=self.node)

                if ptr.left.right.right and ptr.left.right.right.info is not None:
                    temp = ptr.right
                    ptr2 = ptr.right = ptr.left.right.right
                    while ptr2.right and ptr2.right.info is not None:
                        ptr2 = ptr2.right
                    ptr2.right = temp
                ptr.left.right = ptr.left.right.left if (ptr.left.right.left and ptr.left.right.left.info is not None) else None

                #ptr.right.bf=self.maxDepth(ptr=ptr.right.left)-self.maxDepth(ptr=ptr.right.right)
                #ptr.left.bf=self.maxDepth(ptr=ptr.left.left)-self.maxDepth(ptr=ptr.left.right)
                #ptr.bf=self.maxDepth(ptr=ptr.left)-self.maxDepth(ptr=ptr.right)
                self.CalculateBalanceFactor(ptr=self.node)
                self.rotate(ptr=ptr.right)

            # Right-Left Rotate
            if dir[:2]=="RL":
                ptr.info, ptr.left = ptr.right.left.info, Node(info=ptr.info, left=ptr.left if (ptr.left and ptr.left.info is not None) else None)
                #ptr.left.bf=self.maxDepth(ptr=ptr.left.left)-self.maxDepth(ptr=ptr.left.right)
                self.CalculateBalanceFactor(ptr=self.node)

                if ptr.right.left.left and ptr.right.left.left.info is not None:
                    temp = ptr.left
                    ptr2 = ptr.left = ptr.right.left.left
                    while ptr2.left and ptr2.left.info is not None:
                        ptr2 = ptr2.left
                    ptr2.left = temp
                ptr.right.left = ptr.right.left.right if (ptr.right.left.right and ptr.right.left.right.info is not None) else None

                #ptr.left.bf=self.maxDepth(ptr=ptr.left.left)-self.maxDepth(ptr=ptr.left.right)
                #ptr.right.bf=self.maxDepth(ptr=ptr.right.left)-self.maxDepth(ptr=ptr.right.right)
                #ptr.bf=self.maxDepth(ptr=ptr.left)-self.maxDepth(ptr=ptr.right)
                self.CalculateBalanceFactor(ptr=self.node)
                self.rotate(ptr=ptr.left)

    def search(self, info, ptr):
        dir=None
        if ptr and ptr.info is not None:
            if ptr.left and ptr.left.info == info:
                return ptr, "left"
            elif ptr.right and ptr.right.info == info:
                return ptr, "right"
            elif ptr.info > info:
                prev, dir = self.search(info=info, ptr=ptr.left)
            elif ptr.info < info:
                prev, dir = self.search(info=info, ptr=ptr.right)
            return prev, dir
        else:
            return prev, dir

    def min(self, ptr):
        loc = ptr
        while ptr and ptr.info is not None:
            if loc.info>ptr.info:
                loc = ptr
            ptr=ptr.left
        return loc

    def findUnBalanceNode(self, ptr):
        if ptr and ptr.info is not None:
            if ptr.left and ptr.left.info is not None:
                loc, bf=self.findUnBalanceNode(ptr=ptr.left)
                if bf and bf is not None and abs(bf)>=2:
                    return loc, bf
            if ptr.right and ptr.right.info is not None:
                loc, bf=self.findUnBalanceNode(ptr=ptr.right)
                if bf and bf is not None and abs(bf)>=2:
                    return loc, bf
            if abs(ptr.bf)>=2:
                return ptr, ptr.bf
            else:
                return None, None
        else:
            return None, None


    def delete(self, info):
        if self.node.info == info:
            min = self.min(ptr=self.node.right)
            prev, dir=self.search(info=min.info, ptr=self.node)
            self.node.info = min.info
            if dir=="left":
                prev.left=min.right
            elif dir=="right":
                prev.right=min.right

            #min.bf=self.maxDepth(ptr=min.left)-self.maxDepth(ptr=min.right)
            #prev.bf=self.maxDepth(ptr=prev.left)-self.maxDepth(ptr=prev.right)
            #self.node.bf=self.maxDepth(ptr=self.node.left)-self.maxDepth(ptr=self.node.right)
        else:
            prev, dir = self.search(info=info, ptr=self.node)
            ptr = prev.left if dir=="left" else prev.right if dir=="right" else None
            if (not(ptr.left) or ptr.left.info is None) and (not(ptr.right) or ptr.right.info is None):
                ptr.info=None

                #ptr.bf=self.maxDepth(ptr=ptr.left)-self.maxDepth(ptr=ptr.right)
            elif (ptr.left and ptr.left.info is not None) and (not(ptr.right) or ptr.right.info is None):
                ptr=ptr.left

                #ptr.bf=self.maxDepth(ptr=ptr.left)-self.maxDepth(ptr=ptr.right)
            elif (not(ptr.left) or ptr.left.info is None) and (ptr.right and ptr.right.info is not None):
                ptr=ptr.right

                #ptr.bf=self.maxDepth(ptr=ptr.left)-self.maxDepth(ptr=ptr.right)
            elif (ptr.left and ptr.left.info is not None) and (ptr.right and ptr.right.info is not None):
                min = self.min(ptr=ptr.right)
                prev, dir=self.search(info=min.info, ptr=self.node)
                ptr.info = min.info
                ptr2 = prev.left if dir=="left" else prev.right if dir=="right" else None
                ptr2 = min.right

                #min.bf=self.maxDepth(ptr=min.left)-self.maxDepth(ptr=min.right)
                #prev.bf=self.maxDepth(ptr=prev.left)-self.maxDepth(ptr=prev.right)
                #ptr.bf=self.maxDepth(ptr=ptr.left)-self.maxDepth(ptr=ptr.right)
        self.CalculateBalanceFactor(ptr=self.node)
        ptr, bf = self.findUnBalanceNode(ptr=self.node)
        while ptr and ptr.info is not None:
            self.rotate(ptr=ptr)
            ptr, bf=self.findUnBalanceNode(ptr=self.node)
        self.show(ptr=self.node)
        print("")

    def show(self, ptr):
        if not(ptr) or ptr.info is None:
            return
        self.show(ptr=ptr.left)
        print("{"+str(ptr.info)+" ", "("+str(ptr.bf)+")}, ", sep=" ", end="", flush=True)
        self.show(ptr=ptr.right)

def main():
    tree = CompleteBinaryTree()
    process=True
    while process:
        print('1:Insert\n2:Show\n3:Delete\n4:Exit')
        choice=input('Choice:')
        if choice=='4':
            process=False
            break
        elif choice=='1':
            tree.insert(info=int(input('Value:')), ptr=tree.node)
            print("Tree:", sep=" ", end="", flush=True)
            tree.show(ptr=tree.node)
            print("")
        elif choice=='2':
            print("Tree:", sep=" ", end="", flush=True)
            tree.show(ptr=tree.node)
            print("")
        elif choice=='3':
            tree.delete(info=int(input('Value:')))

if __name__ == '__main__':
    main()
