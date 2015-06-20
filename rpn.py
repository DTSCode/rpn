#!/usr/bin/env python

import readline
import sys, signal
import parse_expr, compile_to_rpn, solve_rpn, colors

def hook_ctrl_c(signal, frame):
    print ""
    sys.exit(0)

signal.signal(signal.SIGINT, hook_ctrl_c)

readline.parse_and_bind("tab: complete")
readline.parse_and_bind("set editing-mode vi")

EXPR_TYPES = ["INFIX", "RPN"]

while True:
    expr = raw_input(colors.green("[~>] "))
    current_count = 0
    tokens_list = parse_expr.parse_expr(expr)
    expression_type = EXPR_TYPES[INFIX]

    for tokens in tokens_list:
        current_count = current_count + 1
        rpn_expr = []
        solution = ""


        if tokens == ["quit"]:
            sys.exit(0)

        elif len(tokens) > 0 and tokens[0] == "infix":
            expression_type = EXPR_TYPES[0]
            tokens = tokens[1:]

        elif len(tokens) > 0 and tokens[0] == "rpn":
            expression_type = EXPR_TYPES[1]
            rpn_expr = tokens[1:]

        if tokens != [] and expression_type == EXPR_TYPES[0]:
            rpn_expr = compile_to_rpn.compile_to_rpn(tokens)

        if rpn_expr != [] or expression_type == EXPR_TYPES[1]:
            solution = solve_rpn.solve_rpn(rpn_expr)

        if solution != "":
            print colors.green("Result(") + colors.cyan(str(current_count)) + colors.green("): ") + colors.blue(str(solution))

    print ""
