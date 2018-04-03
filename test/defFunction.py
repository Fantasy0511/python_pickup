def func1():
    return 1
 
def func2():
    return 2
 
def func3(call_times):
    while call_times > 0:
        yield func1()
        yield func2()
        call_times -= 1
  
for i in func3(10):
    print(i)
