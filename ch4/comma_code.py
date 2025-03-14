"""
A solution to the comma code practice problem.
"""


def comma_code(x):
    # Might be cleaner to just use a single for loop to parse this but
    # exposes some new stuff.
    x = [str(y) for y in x]

    n = len(x)
    if n == 0:
        return ""
    elif n == 1:
        return x[0]
    
    # Get everything but the last part.
    fancy = ", ".join(x[:-1])

    # Append the last part with `, and`
    fancy += f", and {x[-1]}"

    return fancy