import operator_table

def compile_to_rpn(tokens):
    operator_stack = []
    rpn_code = []

    for token in tokens:
        try:
            current_number = int(token)
            rpn_code.append(current_number)

        except ValueError:
            if token == "(":
                operator_stack.append(token)

            elif token == ")":
                try:
                    while True:
                        current_operator = operator_stack.pop()

                        if current_operator == "(":
                            break

                        rpn_code.append(current_operator)

                except IndexError:
                    print "(error) mismatched parens"

            elif token in operator_table.ops:
                while len(operator_stack) > 0 and ((operator_table.ops[token][2] == "left" and operator_table.ops[token][1] <= operator_table.ops[operator_stack[-1]][1]) or (operator_table.ops[token][2] == "right" and operator_table.ops[token][1] < operator_table.ops[operator_stack[-1]][1])):
                    operator = operator_stack.pop()

                    if operator != "(":
                        rpn_code.append(operator)

                    else:
                        operator_stack.append("(")

                operator_stack.append(token)
    try:
        while len(operator_stack) != 0:
            current_operator = operator_stack.pop()

            if current_operator in ["(", ")"]:
                raise BadParenError

            rpn_code.append(current_operator)

    except BadParenError:
        print "(error) mismatched parens"

    return rpn_code
