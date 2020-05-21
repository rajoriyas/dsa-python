from linkedlist import *
class Node():
    def __init__(self, vertice=None, neighbour=None, next=None, prev=None):
        self.prev=prev
        self.vertice=vertice
        self.neighbour=LinkedList(neighbour)
        self.next=next

class Graph():
    def __init__(self):
        self.node=Node()

    def insert(self, vertice, neighbour):
        if not(self.node) or self.node.vertice is None:
            self.node=Node(vertice=vertice, neighbour=neighbour)
        else:
            ptr = self.node
            while ptr.next and ptr.next.vertice is not None:
                if ptr.vertice == vertice:
                    ptr.neighbour.append(neighbour)
                    self.display()
                    return
                ptr = ptr.next
            if ptr.vertice == vertice:
                ptr.neighbour.append(neighbour)
            else:
                ptr.next=Node(vertice=vertice, neighbour=neighbour, prev=ptr)
        self.display()


    def display(self):
        if not(self.node) or self.node.vertice is None:
            print("Graph is empty.")
        else:
            ptr = self.node
            print('Graph:')
            while ptr and ptr.vertice is not None:
                print(ptr.vertice, ":" ,sep=" ", end="", flush=True)
                ptr.neighbour.show()
                print("")
                ptr=ptr.next

class BFS():
    def __init__(self):
        self.graph=Graph()
        self.visited=list()
        self.traversed=list()

    def visit(self, ptr):
        neighbour=ptr.neighbour.node
        while neighbour and neighbour.info is not None:
            if neighbour.info not in self.visited and neighbour.info not in self.traversed:
                self.visited.append(neighbour.info)
            neighbour=neighbour.next

    def search(self, vertice):
        ptr=self.graph.node
        while ptr.next and ptr.next.vertice is not None:
            if ptr.vertice==vertice:
                return ptr
            ptr=ptr.next
        if ptr.vertice==vertice:
            return ptr
        return None

    def Traversal(self):
        if not(self.graph.node) or self.graph.node.vertice is None:
            print('Graph is empty.')
        else:
            self.visited.append(self.graph.node.vertice)
            print(self.graph.node.vertice)
            while self.visited:
                temp=self.visited[0]
                node=self.search(vertice=temp)
                if node is not None:
                    self.visit(ptr=node)
                self.traversed.append(self.visited.pop(0))
                print(self.visited)
        print(self.traversed)

class DFS():
    def __init__(self):
        self.graph=Graph()
        self.stack=list()
        self.traversed=list()

    def search(self, vertice):
        ptr=self.graph.node
        while ptr.next and ptr.next.vertice is not None:
            if ptr.vertice==vertice:
                neighbour=ptr.neighbour.node
                while neighbour and neighbour.info is not None:
                    if neighbour.info not in self.stack and neighbour.info not in self.traversed:
                        self.stack.append(neighbour.info)
                        self.traversed.append(neighbour.info)
                        return True
                    neighbour=neighbour.next
            ptr=ptr.next
        if ptr.vertice==vertice:
            neighbour=ptr.neighbour.node
            while neighbour and neighbour.info is not None:
                if neighbour.info not in self.stack and neighbour.info not in self.traversed:
                    self.stack.append(neighbour.info)
                    self.traversed.append(neighbour.info)
                    return True
                neighbour=neighbour.next
        return False

    def Traversal(self, info):
        if not(self.graph.node) or self.graph.node.vertice is None:
            print('Graph is empty.')
        else:
            self.stack.append(info)
            temp=self.stack[len(self.stack)-1]
            self.traversed.append(temp) if temp not in self.traversed else self.traversed
            while self.search(vertice=temp):
                temp=self.stack[len(self.stack)-1]
            else:
                self.stack.pop(len(self.stack)-1)
                temp=self.stack.pop(len(self.stack)-1)
                if self.stack:
                    self.Traversal(info=temp)

def main():
    option=input('1:BFS\n2:DFS\nValue:')
    if option=="1":
        bfs=BFS()
        process=True
        while process:
            print('1:Insert\n2:Show\n3:BFS Traversal\n4:Exit')
            try:
                choice=input('Enter Choice:')
                if choice=='4':
                    process=False
                    break
                elif choice=='1':
                    bfs.graph.insert(vertice=input('Vertice:'), neighbour=input('Neighbour:'))
                elif choice=='2':
                    bfs.graph.display()
                elif choice=='3':
                    bfs.Traversal()
                else:
                    print('Alert: Enter Valid Input!')
            except ValueError:
                print('Alert: Enter Valid Input!')
    if option=="2":
        dfs=DFS()
        process=True
        while process:
            print('1:Insert\n2:Show\n3:DFS Traversal\n4:Exit')
            try:
                choice=input('Enter Choice:')
                if choice=='4':
                    process=False
                    break
                elif choice=='1':
                    dfs.graph.insert(vertice=input('Vertice:'), neighbour=input('Neighbour:'))
                elif choice=='2':
                    dfs.graph.display()
                elif choice=='3':
                    dfs.Traversal(info=dfs.graph.node.vertice)
                    print(dfs.traversed)
                else:
                    print('Alert: Enter Valid Input!')
            except ValueError:
                print('Alert: Enter Valid Input!')

if __name__ == '__main__':
    main()
