class Stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        return self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

#括号匹配问题:给一个字符串,其中包含小括号、中括号、大括号,求该字符串中的括号是否匹配
#eg:
#()()[]{}        匹配
#([{()}])        匹配
#[](            不匹配
#[(])           不匹配


def bracket_matching(s):
    match = {")":"(","]":"[","}":"{"}
    stack = Stack()
    for ch in s:
        if ch in ["(","[","{"]:
            stack.push(ch)
        else: #即:ch in [ ")","]","}" ]
            if stack.is_empty():
                return False
            elif stack.get_top() == match[ch]:
                stack.pop()
            else: #即:stack.get_top() != match[ch]
                return False
    return stack.is_empty()

s= Stack()
print(s.pop())

