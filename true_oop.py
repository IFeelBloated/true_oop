import sys
obj_state = 0

def obj():
    global obj_state
    #for UFCS(Uniform Function Call Syntax)
    def _getattr(self, func):
        module = sys.modules['__main__'] if hasattr(sys.modules['__main__'], func) else sys.modules[self.__module__]
        return lambda *args, **kw: getattr(module, func)(self, *args, **kw)
    #to dynamically attach member functions
    def _setattr(self, attr, value):
        if callable(value):
            setattr(type(self), attr, value)
        else:
            self.__dict__[attr] = value
    settings = {'__getattr__' : _getattr, '__setattr__' : _setattr}
    obj_class = type('obj'+str(obj_state), (object,), settings)
    obj_state += 1
    return obj_class()
