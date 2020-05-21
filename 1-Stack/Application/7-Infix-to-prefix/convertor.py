from DynamicStackLinkedList import *
class InfixToPrefix():
    def __init__(self, str):
        self.prefixExpression=Stack()
        self.stack=Stack()
        self.expression=reversed(str)
        self.symbol=dict()
        self.symbol['^']=3
        self.symbol['*']=2
        self.symbol['/']=2
        self.symbol['+']=1
        self.symbol['-']=1

    def changeOnBasesOfPriority(self, inStackVal, newVal):
        if inStackVal in self.symbol and newVal in self.symbol:
            if self.symbol[inStackVal]>=self.symbol[newVal]:
                #transfer to Prefix Stack, because new one has less priority
                self.prefixExpression.push(inStackVal)
                return True
            else:
                #no need of change, because new one has high priority
                self.stack.push(inStackVal)
                return False
        else:
            #for ')' and '(' symbol, no need of change, because no need of priority evalution
            self.stack.push(inStackVal)
            return False

    def convertor(self):
        for element in self.expression:
            if element==')':
                self.stack.push(element)
                element=None
            if element in self.symbol:
                if self.stack.top==-1:
                    self.stack.push(element)
                    element=None
                elif self.stack.top>-1:
                    temp=self.stack.pop()
                    while self.changeOnBasesOfPriority(temp, element):
                        temp=self.stack.pop()
                    self.stack.push(element)
                    element=None
            if element=='(':
                temp=self.stack.pop()
                while temp!=')' and self.stack.top>-1:
                    self.prefixExpression.push(temp)
                    temp=self.stack.pop()
                element=None
            if element!=None:
                self.prefixExpression.push(element)
        while self.stack.top>-1:
            self.prefixExpression.push(self.stack.pop())
        #stack already print reversed output, so no need to change
        self.prefixExpression.display()

def main():
    iop=InfixToPrefix(input('Write Expression:'))
    iop.convertor()

if __name__ == '__main__':
    main()
