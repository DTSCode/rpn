import operator

global ops

ops = {
    "*" : [operator.mul, 3, "left"],
    "x" : [operator.mul, 3, "left"],
    "/" : [operator.div, 3, "left"],
    "+" : [operator.add, 2, "left"],
    "-" : [operator.sub, 2, "left"],
    "^" : [operator.pow, 4, "right"],
    "(" : [None, 5, "neither"],
    ")" : [None, 5, "neither"]
}
