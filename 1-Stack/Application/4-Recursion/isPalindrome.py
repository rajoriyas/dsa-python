from DynamicStackLinkedList import *
class Validation():
    def isPalindrome(self, str):
        for_ptr=0
        rev_ptr=len(str)-1
        palindrome=True
        while rev_ptr>=for_ptr:
            if str[for_ptr]!=str[rev_ptr]:
                palindrome=False
            for_ptr+=1
            rev_ptr-=1
        return palindrome

    def for_count(self, str):
        if self.isPalindrome(str):
            return 0
        str=str[1:]
        temp = 1+self.for_count(str)
        for_stack_push.push(temp)
        for_stack_push.display()
        return temp

    def rev_count(self, str):
        if self.isPalindrome(str):
            return 0
        str=str[:-1]
        return 1+self.rev_count(str)

    def count(self, str):
        return min(self.for_count(str), self.rev_count(str))

def main():
    global for_stack_push, for_stack_pop
    for_stack_push = Stack()
    for_stack_pop = Stack()
    validate = Validation()
    str = input('String:')
    print('Count:',validate.count(str))

if __name__ == '__main__':
    main()
