from DynamicStackLinkedList import *
class PostfixToInfix():
    def __init__(self, str):
        self.infixExpression=Stack()
        self.stack=Stack()
        self.postfixExpression=str

    def convertor(self):
        #Read in reversed
        for element in reversed(self.postfixExpression):
            if element.lower().isalpha():
                self.infixExpression.push(element)
            else:
                #first oprator=newly poped and secondary opeartor=lastly poped
                op1=self.infixExpression.pop()
                op2=self.infixExpression.pop()
                exp='('+str(op1)+str(element)+str(op2)+')'
                self.infixExpression.push(exp)
        self.infixExpression.display()

def main():
    poi=PostfixToInfix(input('Write Expression:'))
    poi.convertor()

if __name__ == '__main__':
    main()
