#execution of string containing code
statement = 'print("execution of string containing code")'
code_statement = """
def square(x):
    return x*x

print('square of 2: ',square(2))
"""
exec(statement)
exec(code_statement)