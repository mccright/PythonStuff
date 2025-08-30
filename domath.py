#!/usr/bin/python3

import ast
import sys
import operator
from math_evaluator.explicit import calc as explicit_calc, op_map
from math_evaluator.implicit import calc as implicit_calc, valid_ops, allowed_types

# This depends entirely on the Math Evaluator package.
# see: https://medium.com/@r.harvey/how-i-made-a-math-evaluator-on-24-lines-65afe8e560fd
# and the code at: https://github.com/theRealProHacker/MathEvaluator
#

# Support both ** and ^ as power of...
valid_ops.add(ast.Pow)
op_map[ast.BitXor] = operator.__pow__

errmsg = "Malformed equation? The Python package Math Evaluator accepts:\n \
    ° operands\n \
        · ints and\n \
        · floats\n \
    ° operators\n \
        · unary +-\n \
        · binary +-*^**/ and\n \
        · parentheses ()"


def domath(equation):
    expression = equation
    try:
        result = implicit_calc(equation)
    except Exception as e:
        try:
                result = explicit_calc(equation)
                return(result)
        except Exception as e:
            print(f"{expression} errored out in explicit_calc with: {e}")
            print(f"{errmsg}")
            sys.exit(1)
        print(f"{expression} errored out in implicit_calc with: {e}")
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
        # remove commas & $ signs from any of the numbers, if present
        clean_equation_a = equation.replace(",", "")
        clean_equation = clean_equation_a.replace("$", "")
        print(f"{clean_equation} = {domath(clean_equation)}")
        sys.exit()

if __name__ == "__main__":
    # print(f"{str(sys.argv[1:])}")
    main(2, 'USAGE: script_name <input_equation_in_quotes>')
