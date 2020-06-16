# class Counter_stathicmethod:
#     '''статический метод никак не связан с экземплярами.Ему они не нужны.
#     с его помощью можно что-то поднастраивать в классе и не парица.И вызывать метод без передачи экземпляра'''
#     instances = 0
#
#     def __init__(self):
#         Counter_stathicmethod.instances += 1
#
#     @staticmethod
#     def print_intsances():
#         print('Number of instances: %s' % Counter_stathicmethod.instances)
#     #эквивалент декоратору
#     #print_instances = staticmethod(print_instances)
#
# Counter_stathicmethod.print_intsances()

#________________________________________________________метод класса__________________________________________
#!!!получает самый нижний экземпляр класса в наследовании!!!ПОМНИ
class Counter_classmethod:
    '''статический метод никак не связан с экземплярами.Ему они не нужны.
    с его помощью можно что-то поднастраивать в классе и не парица.И вызывать метод без передачи экземпляра'''
    instances = 0

    def __init__(self):
        Counter_classmethod.instances += 1

    @classmethod
    def print_instsances(cls):
        print('Number of instances: %s,%s ' % (cls.instances, cls.__name__))
    #эквивалент декоратору
    #print_instances = classmethod(print_instances)

class Sub(Counter_classmethod):

    @classmethod
    def print_instsances(cls):
        print('From class...%s' % cls.__name__)
        Counter_classmethod.print_instsances()#look,you can calling without any instances

class Other(Sub): pass

Sub.print_instsances()
z = Other
z.print_instsances()#занаследовал функцию от Sub

class Main:
    number = 0
    def __init__(self):
        self.count = Main.number
        self.count += 1

    @classmethod
    def count(cls):
        print('Here %s %s' % (cls.number,cls.__name__))

class SubMain(Main):
    number = 0
    def __init__(self):
        Main.__init__(self)
class Null(SubMain):
    number = 0

SubMain.count()
x = Null()
x.count()
SubMain.count()















class Replay:
    data = ['roi']
    def __init__(self,name):
        self.name = name
        Replay.data.append(self.name)

    @classmethod
    def print_data(cls):#replay
        print('Now look %s' % cls.data)

Replay.print_data()
z = Replay('nikki')
z.print_data()
