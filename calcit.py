import sys
from math import *
# Experiment evaluating math expressions. Not unique.

try:
    # Put quotes around your expression on the command line
    inputs = (sys.argv)
    # Remove the executing script name from the input dict (array)
    expression = inputs[1:]
    # Convert the input dict to a string
    expression = " ".join(str(x) for x in expression)

    if not isinstance(expression, str):
        raise TypeError('The expression must be a string.')
    if not expression:
        raise ValueError('The expression cannot be empty.')
    # return eval(expression, namespace)
    # Print that to the terminal without a newline char
    print(f"{expression} =", end=" ", file=sys.stdout, flush=True)
except Exception as err:
    raise RuntimeError("Evaluating expression '%s' failed: %s"
            % (expression, err))

try:
	# this dict started with a honeybot plugin by Abdur-Rahmaan Janhangeer
	# https://github.com/pyhoneybot/honeybot/blob/master/src/honeybot/plugins/downloaded/calc/main.py
    # I added a few more functions from: https://www.w3schools.com/python/module_math.asp
	safe_dict = {
		"acos": acos,
		"asin": asin,
		"atan": atan,
		"atan2": atan2,
		"ceil": ceil,
		"cos": cos,
		"cosh": cosh,
		"degrees": degrees,
		"e": e,
		"exp": exp,
		"fabs": fabs,
		"factorial": factorial,
		"floor": floor,
		"fmod": fmod,
		"frexp": frexp,
		"gcd": gcd,
		"hypot": hypot,
		"isqrt": isqrt,
		"ldexp": ldexp,
		"log": log,
		"log2": log2,
		"log10": log10,
		"modf": modf,
		"pi": pi,
		"pow": pow,
		"prod": prod,
		"radians": radians,
		"remainder": remainder,
		"sin": sin,
		"sinh": sinh,
		"sqrt": sqrt,
		"tan": tan,
		"tanh": tanh,
		"trunc": trunc
	}
	# Thie approach immediately below is unsafe in an uncontrolled environment
	#     print("{}".format(eval(expression)))
	# The approach below is safer - with sanity-checking/constraining of inputs
	print("{}".format(eval(expression, {"__builtins__": None}, safe_dict)))
except Exception as ex:
    print(f"error: {__file__}: {ex}")
