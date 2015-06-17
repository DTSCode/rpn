#!/usr/bin/env python

import readline
import sys, signal
import parse_expr, compile_to_rpn, solve_rpn

def hook_ctrl_c(signal, frame):
    print ""
    sys.exit(0)

signal.signal(signal.SIGINT, hook_ctrl_c)

readline.parse_and_bind("tab: complete")
readline.parse_and_bind("set editing-mode vi")

while True:
    expr = raw_input("-> ")

    if expr == "quit":
        sys.exit(0)

    tokens = parse_expr.parse_expr(expr);
    rpn_expr = compile_to_rpn.compile_to_rpn(tokens);
    solution = solve_rpn.solve_rpn(rpn_expr)

    if solution != "":
        print "Result:", solution
        print ""
