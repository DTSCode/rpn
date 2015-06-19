import operator, math, sys

global ops
global var_list

ops = {
    "=" : [None, 0, "right"],
    "+" : [operator.add, 2, "left"],
    "-" : [operator.sub, 2, "left"],
    "*" : [operator.mul, 3, "left"],
    "/" : [operator.div, 3, "left"],
    "^" : [operator.pow, 4, "right"],
    "%" : [operator.mod, 4, "right"],
    "@" : [operator.mul, 19, "left"],
    "(" : [None, 20, "neither"],
    ")" : [None, 20, "neither"]
}

var_list = {
    "VER" : 3.1,
    "PI" : math.pi,
    "E" : math.e,
    "MAX" : sys.float_info[0],
    "MIN" : sys.float_info[3],
    "DIG" : sys.float_info[6]
}
