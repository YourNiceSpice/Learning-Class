#автоматический код расширяющий функционал класса
#возврашает надстроенный класс,либо возвращает надстроенный экземпляр
#Предотвращают избыточность


#данный пример перехватывает доступ к неопределенным атрибутам экземпляра.
def decorator(cls) : # При декорировании @
    class Wrapper:
        def __init__(self, *args) : # При создании экземпляров
            self.wrapped = cls(*args)
        def __getattr__(self, name) : # При извлечении атрибутов
            return getattr(self.wrapped, name)
    return Wrapper
@decorator
class С: # C = decorator(C)
    def __init__ (self, x, у) : # Запускается методом Wrapper,__init__
        self.attr = 'spam'

x = C(6, 7) # В действительности вызывается Wrapper (6 , 1)
print(x.attr) # Запускается Wrapper. getattr , выводится spam


данный декоратор,предотвращает вызов более одного экз.от этого класса
instances = {}
def singleton(aClass):
    def onCall(*args, **kwargs):
        if aClass not in instances:
            instances[aClass] = aClass(*args,**kwargs)
        return instances[aClass]
    return onCall
@singleton
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate
bob = Person('Bob', 40, 10)
print(bob.name, bob.pay())
sue = Person('Sue', 50, 20)
print(sue.name, sue.pay())


