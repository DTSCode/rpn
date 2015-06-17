import operator_table, colors

class InvalidStackError(Exception): pass
class VariableNotDefinedError(Exception): pass
class BindError(Exception): pass

def is_num(obj):
    try:
        int(obj)
        return True

    except ValueError:
        return False

current_token = None
current_var_name = None

def solve_rpn(tokens):
    try:
        stack = []

        for token in tokens:
            current_token = token

            if token in operator_table.ops:
                rhs, lhs = stack.pop(), stack.pop()

                if token == "=":
                    if is_num(lhs):
                        raise BindError

                    if not is_num(rhs):
                        if rhs in operator_table.var_list:
                            rhs = operator_table.var_list[rhs]

                        else:
                            current_var_name = rhs
                            raise VariableNotDefinedError

                    operator_table.var_list[lhs] = rhs
                    return colors.blue("(" + lhs + " => " + str(rhs) + ")")

                else:
                    if not is_num(lhs):
                        if lhs in operator_table.var_list:
                            lhs = operator_table.var_list[lhs]

                        else:
                            current_var_name = lhs
                            raise VariableNotDefinedError

                    if not is_num(rhs):
                        if rhs in operator_table.var_list:
                            rhs = operator_table.var_list[rhs]

                        else:
                            current_var_name = rhs
                            raise VariableNotDefinedError

                    stack.append(operator_table.ops[token][0](float(lhs), float(rhs)))

            else:
                stack.append(token)

        if len(stack) > 1:
            raise InvalidStackError

        if not is_num(stack[0]):
            if stack[0] in operator_table.var_list:
                stack[0] = operator_table.var_list[stack[0]]

            else:
                current_var_name = stack[0]
                raise VariableNotDefinedError

        return stack[0]

    except IndexError:
        print colors.red("(error) expression has insufficient number of values\n")
        return ""

    except InvalidStackError:
        print colors.red("(error) expression has too many values\n")
        return ""

    except VariableNotDefinedError:
        print colors.red("(error) variable {") + colors.blue(current_var_name) + colors.red("} is not defined\n")
        return ""

    except BindError:
        print colors.red("(error) cannot bind literal value to literal value\n")
        return ""

