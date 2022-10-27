def fun1(sex):
   print('in fun1')
   def fun0(fun):
        def fun2():
            if sex=='man':
                print('bang zi!')
            elif sex=='woman':
                print('dong dong!')
            return fun()
        return fun2
   return fun0

@fun1('man')
def man():
    print('good work!!!man')
@fun1('woman')
def woman():
    print('good work!!!woman')
man()