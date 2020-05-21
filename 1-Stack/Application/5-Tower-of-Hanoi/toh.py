#   https://www.youtube.com/watch?v=YstLjLCGmgg
#   For n disks, total 2n – 1 moves are required.
#   For n disks, total 2n-1 function calls are made.
from DynamicStackLinkedList import *

class TowerOfHanoi():
    def transfer(self, num, from_rod, to_rod, aux_rod, from_stack, to_stack, aux_stack):
        if num==1:
            print('Disk',num,'From', from_rod, 'To', to_rod)
            temp = from_stack.pop()
            to_stack.push(temp)
            return
        self.transfer(num-1, from_rod, aux_rod, to_rod, from_stack, aux_stack, to_stack)
        print('Disk',num,'From', from_rod, 'To', to_rod)
        temp = from_stack.pop()
        to_stack.push(temp)
        self.transfer(num-1, aux_rod, to_rod, from_rod, aux_stack, to_stack, from_stack)
        return

def main():
    stack_A = Stack()
    stack_B = Stack()
    stack_C = Stack()
    num=int(input('Number of Disks:'))
    for i in range(num, 0, -1):
        stack_A.push(info=i)
    stack_A.display()
    stack_B.display()
    stack_C.display()
    toh = TowerOfHanoi()
    toh.transfer(num, 'A', 'C', 'B', stack_A, stack_C, stack_B)
    stack_A.display()
    stack_B.display()
    stack_C.display()

if __name__ == '__main__':
    main()
#   https://www.youtube.com/watch?v=YstLjLCGmgg
#   For n disks, total 2n – 1 moves are required.
#   For n disks, total 2n-1 function calls are made.
