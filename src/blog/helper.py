def Fibonacci(input_val):
    if input_val<0:
        pass
    elif input_val==1: 
        return 0
    elif input_val==2: 
        return 1
    else: 
        return Fibonacci(input_val-1)+Fibonacci(input_val-2) 
