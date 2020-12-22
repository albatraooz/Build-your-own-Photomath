

def RPN(expression: str) -> str:

    output_queue = []
    operator_stack = []

    OPERATORS = {'+', '-', '*', '/'}
    LEFT_PARENTHESES = '('
    RIGHT_PARENTHESES = ')'
    LOWER_PRECEDENCE_OPERATORS = {'+', '-'}
    GREATER_PRECEDENCE_OPERATROS = {'*', '/'}


    for character in expression:
        if character.isspace():
            continue
        elif character.isdigit():
            output_queue.append(character)
        elif character in OPERATORS:
            while operator_stack and operator_stack[-1] in GREATER_PRECEDENCE_OPERATROS:
                output_queue.append(operator_stack.pop())
            operator_stack.append(character)
        elif character is LEFT_PARENTHESES:
            operator_stack.append(character)
        elif character in RIGHT_PARENTHESES:
            while operator_stack and operator_stack[-1] is not LEFT_PARENTHESES:
                output_queue.append(operator_stack.pop())
            if operator_stack[-1] is LEFT_PARENTHESES:
                operator_stack.pop()

    operator_stack.reverse()
    output_queue.extend(operator_stack)

    return output_queue

def reversePolishEvaluator(expression: str) -> int:
    stack = []

    if not expression:
        return 0

    for character in expression:
        if character.isdigit():
            stack.append(int(character))
        else:
            first_operand = stack.pop()
            second_operand = stack.pop()

            if character == '+':
                stack.append(int(first_operand) + int(second_operand))
            elif character == '-':
                stack.append(int(second_operand) - int(first_operand))
            elif character == '*':
                stack.append(int(first_operand) * int(second_operand))
            elif character == '/':
                stack.append(int(second_operand) / int(first_operand))

    if len(stack) > 1:
        return "INVALID EXPRESSION"

    return stack[0]


print(reversePolishEvaluator(RPN("(1 - 3*2)*(((1+2) + 4)*5)")))
