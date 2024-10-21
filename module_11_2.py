import inspect
def  introspection_info(obj):
    if (isinstance(obj,str) or isinstance(obj,int) or isinstance(obj,float)
            or isinstance(obj,list) or isinstance(obj,dict) or isinstance(obj,tuple)):
        _methods = [name for name in dir(obj) if '__'not in name]
        attributes =  dir(obj)
    else:
        _methods = [m for m in inspect.getmembers(obj, predicate=inspect.ismethod)]
        attributes =  [name for name in dir(obj) if '__'not in name]
    return {'type':type(obj),'methods':_methods,
            'attributes':attributes,
            'module': inspect.getmodule(obj)}

class Test_ins:
    a = 1
    b = 'str'
    def test_metod(self):
        pass

number_info = introspection_info('42')
test_cl = Test_ins()
number_info2 = introspection_info(test_cl)
print(number_info)
print(number_info2)


