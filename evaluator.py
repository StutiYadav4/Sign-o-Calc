from math import sqrt
import re

def safe_eval(expression):
    try:
        # Replace ^ with ** for power
        expression = expression.replace('^', '**')

        # Replace √number or √(something) with sqrt(...)
        expression = re.sub(r'√(\d+(\.\d+)?|\([^\)]+\))', r'sqrt(\1)', expression)

        allowed_chars = set('0123456789+-*/(). ')
        if all(c in allowed_chars or c.isalpha() for c in expression):
            return str(eval(expression))
        else:
            return "Invalid"
    except:
        return "Error"