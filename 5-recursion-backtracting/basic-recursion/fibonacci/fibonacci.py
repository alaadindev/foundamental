def fibonacci(step):
    if step == 1:
        return 0 
    if step == 2:
        return 1
    return fibonacci(step-1) + fibonacci(step-2) 

print(fibonacci(7))