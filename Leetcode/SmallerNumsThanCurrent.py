class Solution:
    def evalRPN(self, tokens: list) -> int:
        
        stack = []
        for token in tokens:
            # Token is a number, add it to the stack
            if token not in set(["+","-","*","/"]):
                stack.append(int(token))
            else:
                if token == "+":
                    op1 = stack.pop()
                    op2 = stack.pop()
                    result = op2 + op1
                    stack.append(result)
                elif token ==  "-":
                    op1 = stack.pop()
                    op2 = stack.pop()
                    result = op2 - op1
                    stack.append(result)
                elif token == "*":
                    op1 = stack.pop()
                    op2 = stack.pop()
                    result = op2 * op1
                    stack.append(result)
                elif token == "/":
                    op1 = stack.pop()
                    op2 = stack.pop()
                    result = abs(op2) // abs(op1)
                    if (op2 < 0) ^ (op1 < 0):
                        result = -result

                    stack.append(result)
                print(f"{op2} {token} {op1} = {result}")
        return stack[0]

if __name__=="__main__":
    s = Solution()
    #print(s.evalRPN(["2","1","+","3","*"]))
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    print(s.evalRPN(["4","-2","/","2","-3","-","-"]))