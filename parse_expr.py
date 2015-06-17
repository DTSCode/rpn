def parse_expr(expr):
    tokens = []
    number_val = ""

    for elem in expr:
        if elem in "*x/+-^()":
            if number_val != "":
                tokens.append(number_val)
                number_val = ""

            tokens.append(elem)

        elif elem in " \t\n":
            if number_val != "":
                tokens.append(number_val)
                number_val = ""

            pass

        else:
            number_val = number_val + elem

    if number_val != "":
        tokens.append(number_val)

    return tokens
