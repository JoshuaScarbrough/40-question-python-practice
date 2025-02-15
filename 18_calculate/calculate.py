def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
        
    """
    result = 0

    if operation == "add" and make_int == True:
        result = int(a + b)
        return f"{message} {result}"
    elif operation == "add": 
        result = a + b
        return f"{message} {result}"
    
    if operation == "subtract" and make_int == True:
        result = int(a - b)
        return f"{message} {result}"
    elif operation == "subtract": 
        result = a - b
        return f"{message} {result}"
    
    if operation == "multiply" and make_int == True:
        result = int(a * b)
        return f"{message} {result}"
    elif operation == "multiply": 
        result = a * b
        return f"{message} {result}"
    
    if operation == "divide" and make_int == True:
        result = int(a / b)
        return f"{message} {result}"
    elif operation == "divide": 
        result = a / b
        return f"{message} {result}"
    
    if operation != "add" or operation != "subtract" or operation != "multiply" or operation != "divide":
        return None

        

