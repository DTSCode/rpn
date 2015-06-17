import operator_table

class InvalidStackError(Exception): pass
class BadParenError(Exception): pass

current_token = None

def solve_rpn(tokens):
    try:
        stack = []

        for token in tokens:
            current_token = token

            if token not in operator_table.ops:
                stack.append(int(token))

            else:
                rhs, lhs = stack.pop(), stack.pop()
                stack.append(operator_table.ops[token][0](lhs, rhs))

        if len(stack) > 1:
            raise InvalidStackError

        return stack[0]

    except ValueError:
        print "(error) token {%s} is a not a number or operator\n" % current_token
        return ""

    except IndexError:
        print "(error) expression has insufficient number of values\n"
        return ""

    except InvalidStackError:
        print "(error) too many values\n"
        return ""
