'''
def fun(a):

    print ('fun')
    def func1(b):
        print('fun1')
        print(a+b)
    return func1

mm=fun(2)
mm(3)
#shang shi bi bao
'''

def funNew(fun):
    print('funNew')
    def fun1(a,b,c):
        print('abc')
        print('c:')
        return fun(a,b)
    return fun1


@funNew
def myFun(a,b):
    return a+b
#funNew(myFun)(a,b)  if myFun run the machine run left code of ':'
#myFun=funNew(myFun)
#myFun()=fun1
aa=myFun(1,3,4)# return fun1(a,b,c) a:1,b:3,c:4
print(aa)




