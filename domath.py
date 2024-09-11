#!/usr/bin/python3

import ast
import sys
from math_evaluator.implicit import calc

# This depends entirely on the Math Evaluator package.
# see: https://medium.com/@r.harvey/how-i-made-a-math-evaluator-on-24-lines-65afe8e560fd
# and the code at: https://github.com/theRealProHacker/MathEvaluator
#


errmsg = "Malformed equation? The Python package Math Evaluator accepts:\n \
    ° operands\n \
        · ints and\n \
        · floats\n \
    ° operators\n \
        · unary +-,\n \
        · binary +-*/ and\n \
        · parantheses ()"


def domath(equation):
    expression = equation
    try:
        result = calc(equation)
    except Exception as e:
        print(f"{expression} errored out with: {e}")
        print(f"{errmsg}")
        sys.exit(1)
    return(result)


def main(num_args: int, usage: str):
    if len(sys.argv) != num_args:
        this_script = sys.argv[0]
        usage_message = usage.replace("script_name", str(this_script))
        print(usage_message)
        sys.exit(1)
    equation = sys.argv[1]
    if equation != None:
        print(f"{equation} = {domath(equation)}")
        sys.exit()

if __name__ == "__main__":
    main(2, 'USAGE: script_name <input_equation_in_quotes>')
