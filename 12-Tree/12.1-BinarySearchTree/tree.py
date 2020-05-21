class Node():
    def __init__(self,  left=None, info=None, right=None):
        self.left=left
        self.info=info
        self.right=right

class CompleteBinaryTree():
    def __init__(self):
        self.node=Node()
        self.ptr=Node()
        self.last=list()

    def insert(self, info):
        if not(self.node) or self.node.info is None:
            self.node=Node(info=info)
        else:
            self.ptr=self.node
            while self.ptr and self.ptr.info is not None:
                if self.ptr.info>info:
                    if not(self.ptr.left) or self.ptr.left.info is None:
                        self.ptr.left=Node(info=info)
                        break
                    else:
                        self.ptr=self.ptr.left
                elif self.ptr.info<info:
                    if not(self.ptr.right) or self.ptr.right.info is None:
                        self.ptr.right=Node(info=info)
                        break
                    else:
                        self.ptr=self.ptr.right
                elif self.ptr.info==info:
                    break
        print("Tree:", sep=" ", end="", flush=True)
        self.show(scheme="NLR", ptr=self.node)
        print("")

    def show(self, scheme, ptr):
        if scheme=="NLR":
            if not(ptr) or ptr.info is None:
                return
            print(ptr.info, " ", sep=" ", end="", flush=True)
            self.show(scheme="NLR", ptr=ptr.left)
            self.show(scheme="NLR", ptr=ptr.right)
        if scheme=="LNR":
            if not(ptr) or ptr.info is None:
                return
            self.show(scheme="LNR", ptr=ptr.left)
            print(ptr.info, " ", sep=" ", end="", flush=True)
            self.show(scheme="LNR", ptr=ptr.right)
        if scheme=="LRN":
            if not(ptr) or ptr.info is None:
                return
            self.show(scheme="LRN", ptr=ptr.left)
            self.show(scheme="LRN", ptr=ptr.right)
            print(ptr.info, " ", sep=" ", end="", flush=True)

    def search(self, info, ptr):
        if ptr and ptr.info is not None:
            if ptr.info==info:
                print("Value:", ptr.info, "is found in tree.")
                return ptr
            else:
                if ptr.info>info:
                    ptr=ptr.left
                    ptr=self.search(info, ptr)
                elif ptr.info<info:
                    ptr=ptr.right
                    ptr=self.search(info, ptr)
                return ptr
        else:
            print("Value:", info, "is not found in tree.")
            return None
    #Right-Lefty Child
    def min(self, ptr):
        loc=ptr
        while ptr and ptr.info is not None:
            if loc.info>ptr.info:
                loc=ptr
            ptr=ptr.left
        return loc

    def parent(self, ptr, info):
        if ptr:
            if ptr.left and ptr.left.info==info:
                return ptr, "left"
            elif ptr.right and ptr.right.info==info:
                return ptr, "right"
            else:
                if ptr.info>info:
                    ptr, dir=self.parent(ptr.left, info)
                elif ptr.info<info:
                    ptr, dir=self.parent(ptr.right, info)
                return ptr, dir

    def delete(self, info):
        ptr=self.search(info=info, ptr=self.node)
        if ptr!=None:
            if (not(ptr.right) or ptr.right.info is None) and (not(ptr.left) or ptr.left.info is None):
                ptr.info=None
                #ptr=Node()
                #Don't "ptr=Node()", because it just allocate another location, don't replace previous one
            elif (not(ptr.right) or ptr.right.info is None) and ((ptr.left) or ptr.left.info is not None):
                if ptr.info == self.node.info:
                    self.node = self.node.left
                else:
                    prev, dir=self.parent(ptr=self.node, info=info)
                    if dir=="left":
                        prev.left=ptr.left
                    elif dir=="right":
                        prev.right=ptr.left
            elif (not(ptr.left) or ptr.left.info is None) and ((ptr.right) or ptr.right.info is not None):
                if ptr.info == self.node.info:
                    self.node = self.node.right
                else:
                    prev, dir=self.parent(ptr=self.node, info=info)
                    if dir=="left":
                        prev.left=ptr.right
                    elif dir=="right":
                        prev.right=ptr.right
            elif ((ptr.left) or ptr.left.info is not None) and ((ptr.right) or ptr.right.info is not None):
                min=self.min(ptr=ptr.right)
                # "prev, dir=self.parent(ptr=self.node, info=min.info)" can't be below "ptr.info= min.info" beacuse if this line is above, then min.info can be found on top of node which don't give the old location where still value is present and we have to remove.
                prev, dir=self.parent(ptr=self.node, info=min.info)
                ptr.info= min.info
                #Why always "min.right"?
                #beacuse "min" will never contain "min.left" because "min.left" has smaller value then min.
                #if "min.left" exixts then "min.left" will become output of "min()" function
                if dir=="left":
                    prev.left=min.right
                elif dir=="right":
                    prev.right=min.right
                #ptr.info, min = min.info, Node()
                #Don't "min=Node()", because it just allocate another location, don't replace previous one
            print("Tree:", sep=" ", end="", flush=True)
            self.show(scheme="NLR", ptr=self.node)
            print("")

    def isExtendedBinaryTree(self, ptr):
        if ptr and ptr.info is not None:
            if (not(ptr.right) or ptr.right.info is None) and (not(ptr.left) or ptr.left.info is None):
                return True
            elif (not(ptr.left) or ptr.left.info is None) and ((ptr.right) or ptr.right.info is not None):
                return False
            elif (not(ptr.right) or ptr.right.info is None) and ((ptr.left) or ptr.left.info is not None):
                return False
            elif ((ptr.left) or ptr.left.info is not None) and ((ptr.right) or ptr.right.info is not None):
                if self.isExtendedBinaryTree(ptr.left) and self.isExtendedBinaryTree(ptr.right):
                    return True
                else:
                    return False
        else:
            return True

    def MaxDepth(self, ptr, count=0):
        if ptr and ptr.info is not None:
            count+=1
            countLeft=0
            countRight=0
            if ptr.left:
                countLeft=self.MaxDepth(ptr=ptr.left, count=count)
            if ptr.right:
                countRight=self.MaxDepth(ptr=ptr.right, count=count)
            if countLeft!=0 or countRight!=0:
                return max(countLeft, countRight)
            else:
                return count
        else:
            return 0

    def isFullBinaryTree(self, ptr, depth, avoid=1):
        if ptr.left and ptr.left.info is not None and ptr.right and ptr.right.info is not None and depth>avoid:
            validateLeft = self.isFullBinaryTree(ptr.left, depth-1)
            validateRight = self.isFullBinaryTree(ptr.right, depth-1)
            if validateLeft and validateRight:
                return True
            else:
                return False
        elif depth==avoid:
            #last row is neglected.
            return True
        else:
            return False

    def LastElement(self, ptr, depth):
        if depth>0:
            if depth==1:
                self.last.append(ptr.info)
                return
            if ptr.left:
                self.LastElement(ptr.left, depth-1)
            elif not(ptr.left) or ptr.left.info is None:
                self.last.append(None)
            if ptr.right:
                self.LastElement(ptr.right, depth-1)
            elif not(ptr.right) or ptr.right.info is None:
                self.last.append(None)
        else:
            #Case:depth==0, means no element
            self.last.append(None)

    def isCompleteBinaryTree(self, ptr):
        if self.MaxDepth(ptr=self.node)>1:
            if self.isFullBinaryTree(ptr=self.node, depth=self.MaxDepth(ptr=self.node)-1, avoid=1):
                self.LastElement(ptr=self.node, depth=self.MaxDepth(ptr=self.node))
                #Removing last None
                while self.last[-1]==None:
                    self.last.pop()
                #from first to Non-None Element
                for i in range(len(self.last)):
                    if self.last[i]==None:
                        self.last.clear()
                        return False
                self.last.clear()
                return True
            else:
                self.last.clear()
                return False
        elif self.MaxDepth(ptr=self.node)==1:
            #Single Node Tree is always be a Complete Binary Tree
            return True
        else:
            #No Node Tree is never be a Complete Binary Tree
            return False

def main():
    tree = CompleteBinaryTree()
    process=True
    while process:
        print('1:Insert\n2:Show-Preorder\n3:Show-Inorder\n4:Show-Postorder\n5:Delete\n6:is Extended Binary Tree?\n7:is Complete Binary Tree?\n8:is Full Binary Tree?\n9:Last Element\n10:Exit')
        choice=input('Choice:')
        if choice=='10':
            process=False
            break
        elif choice=='1':
            tree.insert(info=int(input('Value:')))
        elif choice=='2':
            print("Tree:", sep=" ", end="", flush=True)
            tree.show(scheme="NLR", ptr=tree.node)
            print("")
        elif choice=='3':
            print("Tree:", sep=" ", end="", flush=True)
            tree.show(scheme="LNR", ptr=tree.node)
            print("")
        elif choice=='4':
            print("Tree:", sep=" ", end="", flush=True)
            tree.show(scheme="LRN", ptr=tree.node)
            print("")
        elif choice=='5':
            tree.delete(info=int(input("Value:")))
        elif choice=='6':
            print("Extended Binary Tree:", tree.isExtendedBinaryTree(ptr=tree.node))
        elif choice=='7':
            print("Complete Binary Tree:", tree.isCompleteBinaryTree(ptr=tree.node))
        elif choice=='8':
            print("Full Binary Tree:", tree.isFullBinaryTree(ptr=tree.node, depth=tree.MaxDepth()))
        elif choice=='9':
            tree.LastElement(ptr=tree.node, depth=tree.MaxDepth(ptr=tree.node))
            print("Last Element", tree.last)
            tree.last.clear()

if __name__ == '__main__':
    main()
