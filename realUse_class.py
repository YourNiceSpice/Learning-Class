#отношение: являются
class Employee: #common behavior class
    def __init__(self,name,salary=0):
        self.name = name
        self.salary = salary
    def __repr__(self):
        return  'Name:%s, salary =%s' % (self.name, self.salary) #как сюда поставить класс нэйм
        #return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)
    def give_rise(self,percent):
        self.salary = self.salary + (self.salary * percent)
    def work(self):
        pass #сделать абстракный метод
class Server(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,salary=50000)
    def work(self):
        print(self.name,'work with clients')
class Chef(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,salary=40000)
    def work(self):
        print(self.name,'make food')
class PizzaRobot(Chef):
    def __init__(self,name):
        Chef.__init__(self,name)
    def work(self):
        print(self.name,'make pizza')

for klass in Employee,Server,Chef,PizzaRobot:
    obj = klass(klass.__name__)
    print(obj)

#Композиция!
class Processor: #суперкласс
    def __init__(self,writer,reader):
        self.writer = writer
        self.reader = reader
    def process(self):
        while True:
            data = self.reader.readline()
            if not data: break
            data = self.converter(data)
            self.writer.write(data)
    def conventer(self):  #абстракный метод Суперкласса,ожидает заполнения подклассами
        assert False,'converter must be definded'

class Uppercase(Processor): #определяет только уникальную логику поведения в классе
    def conventer(self):
        return data.upper()

class HTMLize:
    def write(self, line):
        print('<PRE>%s</PRE>' % line.rstrip())


#КЛАССЫ являются объектами.Фабрики классов.Это метод,принимающий аргументом класс

def factory(aClass,*args,**kwargs):
    return aClass(*args,**kwargs)
class Person:
    def __init__(self,name,job=None):
        self.name = name
        self.job = job

object = factory(Person,'Arthur','Manager')
object.name

#Подмешивание.