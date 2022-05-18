### Handling Error Using Secorater 

def Error_Handler(func):
    def Inner_Function(*args,**kwrgs):
        try:
            func(*args,**kwrgs)
        except TypeError:
            print(f'{func.__name__} wrong data type. Enter Number Here')
    return Inner_Function


@Error_Handler
def Mean(a,b):
    print((a+b)/2)




Mean(2,2)