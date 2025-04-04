class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack_list = []
        for token in tokens:
            try:
                token_value = int(token)
                stack_list.append(token_value)
                continue                
            except ValueError:
                num_1 = stack_list.pop()
                num_2 = stack_list.pop()
                if token == '+':
                    stack_list.append(num_2+num_1)
                elif token == '-':
                    stack_list.append(num_2-num_1)
                elif token == '*':
                    stack_list.append(num_2*num_1)
                else:
                    stack_list.append(int(num_2/num_1))
        return stack_list[0]