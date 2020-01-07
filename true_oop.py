obj_state = 0
symbols = {}

def obj():
    global obj_state
    #for UFCS(Unified Function Call Syntax)
    def _getattr(self, func):
        return lambda *args, **kw: symbols[func](self, *args, **kw)
    #to dynamically attach member functions
    def _setattr(self, attr, value):
        if callable(value):
            setattr(type(self), attr, value)
        else:
            self.__dict__[attr] = value
    settings = dict(__getattr__ = _getattr, __setattr__=_setattr)
    obj_class = type('obj'+str(obj_state), (object,), settings)
    obj_state += 1
    return obj_class()
