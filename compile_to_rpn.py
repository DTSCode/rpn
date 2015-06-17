import operator_table, colors

def is_num(obj):
    try:
        int(obj)
        return True

    except ValueError:
        return False

def compile_to_rpn(tokens):
    operator_stack = []
    rpn_code = []

    for token in tokens:
        if is_num(token):
            rpn_code.append(token)

        elif token == "(":
            operator_stack.append(token)

        elif token == ")":
            try:
                while True:
                    current_operator = operator_stack.pop()

                    if current_operator == "(":
                        break

                    rpn_code.append(current_operator)

            except IndexError:
                print colors.red("(error) mismatched parens\n")
                return

        elif token in operator_table.ops:
            while len(operator_stack) > 0 and ((operator_table.ops[token][2] == "left" and operator_table.ops[token][1] <= operator_table.ops[operator_stack[-1]][1]) or (operator_table.ops[token][2] == "right" and operator_table.ops[token][1] < operator_table.ops[operator_stack[-1]][1])):
                operator = operator_stack.pop()

                if operator != "(":
                    rpn_code.append(operator)

                else:
                    operator_stack.append("(")
                    break

            operator_stack.append(token)

        else:
            rpn_code.append(token)

    while len(operator_stack) > 0:
        operator = operator_stack.pop()

        if operator == "(":
            print colors.red("(error) mismatched parens\n")
            return []

        rpn_code.append(operator)

    return rpn_code
