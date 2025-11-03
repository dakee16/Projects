class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        return self.top is None

    def __len__(self): 
        # YOUR CODE STARTS HERE
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def push(self,value):
        # YOUR CODE STARTS HERE
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

     
    def pop(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return None
        removed_node = self.top.value
        self.top = self.top.next
        return removed_node

    def peek(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return None
        return self.top.value


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        try:
            float(txt)
            return True
        except:
            return False


    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack object for expression processing

            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix('( 2 { 5.0 } )')
            '2.0 5.0 *'
            >>> x._getPostfix(' 5 ( 2 + { 5 + 3.5 } )')
            '5.0 2.0 5.0 3.5 + + *'
            >>> x._getPostfix ('( { 2 } )')
            '2.0'
            >>> x._getPostfix ('2 * ( [ 5 + -3 ] ^ 2 + { 1 + 4 } )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('[ 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ]')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( { 2 * { { 5 + 3 } ^ 2 + ( 1 + 4 ) } } )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * ( -5 + 3 ) ^ 2 + [ 1 + 4 ]')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ]')
            >>> x._getPostfix(' ( 2 * { 5 + 3 ) ^ 2 + ( 1 + 4 ] }')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')
        '''

        # YOUR CODE STARTS HERE
        postfixStack = Stack()
        bracketStack = Stack()
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0, '{': 0, '[': 0}
        postfix = []
        openlst = ['(','[','{']
        closelst = [')',']','}']
        text = txt.split()
        
                
        isValidExpression = True
        lastWasOperator = False
        lastWasOperand = False
        

        i = 0  # Initialize index variable outside the loop
        while i < len(text):
            ops = text[i]

            if self._isNumber(ops):
                postfix.append(f"{float(ops)}")
                if lastWasOperand:
                    isValidExpression = False
                lastWasOperand = True
                lastWasOperator = False
                if i + 1 < len(text) and text[i + 1] in openlst:
                    postfixStack.push('*')
        
            elif ops in openlst:
                postfixStack.push(ops)
                bracketStack.push(ops)
                lastWasOperator = False
                lastWasOperand = False 

            elif ops in closelst:
                if bracketStack.isEmpty() or openlst[closelst.index(ops)] != bracketStack.peek():
                    isValidExpression = False
                bracketStack.pop()    
                while not postfixStack.isEmpty() and postfixStack.peek() != openlst[closelst.index(ops)]:
                    postfix.append(postfixStack.pop())
                if not postfixStack.isEmpty():
                    postfixStack.pop()
                lastWasOperand = False
                if i + 1 < len(text) and (text[i + 1] in openlst or self._isNumber(text[i + 1])):
                    postfixStack.push('*') 

            elif ops in precedence:
                if lastWasOperator:
                    isValidExpression = False

                while not postfixStack.isEmpty() and precedence[ops] <= precedence[postfixStack.peek()]:
                    postfix.append(postfixStack.pop())
                postfixStack.push(ops)
                lastWasOperator = True
                lastWasOperand = False
            else:
                isValidExpression = False
            i += 1
            
        if lastWasOperator:
            isValidExpression = False
        while not postfixStack.isEmpty():
            top = postfixStack.pop()
            if top in openlst:
                isValidExpression = False
            if isValidExpression:
                postfix.append(top)

        if not bracketStack.isEmpty():
            isValidExpression = False

        if isValidExpression:
            return " ".join(postfix)
        else:
            return None




    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack object to compute the final result as shown in the video lectures
            

            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( [ ( 10 - 2 * 3 ) ] )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * { 3 - 2.45 * [ 4 - 2 ^ 3 ] } + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * [ 4 + 2 * { 5 - 3 ^ 2 } + 1 ] + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + { 3.0 } * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * [ 4 ] ) * [ 2 / 8 + 2 * ( 3 - 1 / 3 ) ] - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            >>> x.setExpr('( 3.5 ) [ 15 ]') 
            >>> x.calculate
            52.5
            >>> x.setExpr('3 { 5 } - 15 + 85 [ 12 ]') 
            >>> x.calculate
            1020.0
            >>> x.setExpr("( -2 / 6 ) + ( 5 { ( 9.4 ) } )") 
            >>> x.calculate
            46.666666666666664
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( ( 2 ) * 10 - 3 * [ 2 - 3 * 2 ) ]')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression

        # YOUR CODE STARTS HERE
        postfix = self._getPostfix(self.__expr) 
        if postfix is None:
            return None

        for ops in postfix.split():
            if self._isNumber(ops):
                calcStack.push(float(ops))
            else: 
                if calcStack.__len__() < 2:
                    return None
                exp2 = calcStack.pop() 
                exp1 = calcStack.pop()
                if ops == '+':
                    ans = exp1 + exp2
                    calcStack.push(ans)
                elif ops == '-':
                    ans = exp1 - exp2
                    calcStack.push(ans)
                elif ops == '*':
                    ans = exp1 * exp2
                    calcStack.push(ans)
                elif ops == '/':
                    if exp2 == 0: 
                        return None
                    ans = exp1 / exp2
                    calcStack.push(ans)
                elif ops == '^':
                    ans = exp1 ** exp2
                    calcStack.push(ans)

        if calcStack.__len__() != 1:
            return None

        return calcStack.pop()



#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 [ x1 - 1 ];x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * { x1 / 2 };x1 = x2 * 7 / x1;return x1 ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * { x1 / 2 }': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        super().__init__()
        self.variables = {}
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        if str(word[0]).isnumeric():
            return False
        return str(word).isalnum() and len(word) > 0 
       

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 ( x1 - 1 )')
            '7 ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        text = expr.split()
        for i in range(len(text)):
            ops = text[i]
            if ops in self.states:
                text[i] = str(self.states[ops])
            elif self._isVariable(ops): 
                return None
        return ' '.join(text)

    
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        expressions = self.expressions.split(';')
        results = {}

        for expr in expressions:
            expr = expr.strip()
            if '=' in expr:
                var, expr = expr.split('=', 1)  # Split only on the first '='
                var = var.strip()
                expr = expr.strip()
                if self._isVariable(var):
                    replaced_expr = self._replaceVariables(expr)
                    if replaced_expr is not None:
                        calcObj.setExpr(replaced_expr)
                        result = calcObj.calculate  # Assuming this method exists and evaluates the expression
                        if result is not None:
                            self.states[var] = result
                            results[var + " = " + expr] = self.states.copy()
                        else:
                            return None  # If calculation failed, return None
                    else:
                        return None  # If replacement failed, return None
            else:
                replaced_expr = self._replaceVariables(expr)
                if replaced_expr is not None:
                    calcObj.setExpr(replaced_expr)
                    result = calcObj.calculate  # Evaluate the expression
                    if result is not None:
                        results['_return_'] = result
                    else:
                        return None  # If calculation failed, return None
                else:
                    return None  # If replacement failed, return None

        return results