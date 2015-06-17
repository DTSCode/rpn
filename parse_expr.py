import colors, operator_table

def parse_expr(expr):
    tokens = []
    token_val = ""

    for elem in expr:
        if elem in operator_table.ops:
            if token_val != "":
                tokens.append(token_val)
                token_val = ""

            tokens.append(elem)

        elif elem in " \t\n":
            if token_val != "":
                tokens.append(token_val)
                token_val = ""

        elif elem.isdigit() or elem.isalpha() or elem in "_.":
            token_val = token_val + elem

        elif elem == "#":
            break

        else:
            print colors.red("(error) token {") + colors.yellow(elem) + colors.red("} is not a valid token\n")
            return []

    if token_val != "":
        tokens.append(token_val)

    return tokens
