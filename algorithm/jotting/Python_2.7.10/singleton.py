class Singleton(object):
  def __new__(cls, *args, **kwargs):
    if not hasattr(cls, '__instance'):
      orig = super(Singleton, cls)
      cls.__instance = orig.__new__(cls, *args, **kwargs)
    return cls.__instance

class MyClass(Singleton):
  a = 1

###############################################################################

class Borg(object):
  _state = {}
  def __new__(cls, *args, **kwargs):
    ob = super(Borg, cls).__new__(cls, *args, **kwargs)
    ob.__dict__ = cls._state
    return ob

class MyClass2(Borg):
  a = 1

###############################################################################

def singleton(cls, *args, **kw):
  instances = {}
  def getinstance():
    if cls not in instances:
      instances[cls] = cls(*args, **kw)
    return instances[cls]
  return getinstance

@singleton
class MyClass:
  pass

###############################################################################

# mysingleton.py
class My_Singleton(object):
  def foo(self):
    pass

my_singleton = My_Singleton()

# to use
from mysingleton import my_singleton

my_singleton.foo()


