#зачем нужны классы?
#класс по сути лишь определяет доп. пространство имён как модули и имена.
от модуля отлич:создает экземпляры,наследуется,перегружает операции.
#ООП предназначено для многократного использования кода — вы производите
#разложение кода с целью минимизации избыточности и программируете путем
#настройки того, что уже существует, а не изменяете код на месте или пишете его
#с нуля.
#Определить свой тип данных
#создать инфраструктуру с общими чертами поведения.Типа робот типичный
    #но при этом при помощи наследования сделать класс роботов зеленых,они на 90 проц будут копировать
    #общее поведение роботов но класс зеленых роботов будет задавать им уникальный цвет.
#классы хороши для настройки кода и локализации имён
#возможность работы с фрэймворками,где всё уже описано до нас
#Паттерны проектирования это и есть структура Классов их взаимосвязей

class Myclass:
    a = 10
    def say_hi(self):#порт для экземплярчика
        print('privetik')

print(Myclass.a)#execute Myclass namespace throught the dot
a = Myclass()
print(Myclass.say_hi(a))

class Newclass:
    pass

x = Newclass()
x.count = 0
x.count += 1

print(Newclass)

#__________init________________

class Initer:
    a = 100500
    def __init__(self,track:int): #self take instance, x in this case and make namespace.Эта штука определяет поведение
                        #экземпляра класса по умолчанию
        self.something = 0
        self.bigass = True
        self.nigga = 'Black'
        self.track = track #это переданный аргумент в __init__

    def inc(self):#в селф залетает Y понял да
        print('эквивалентно')
#self.track мы инициализируем для экземпляра
y = Initer('233')
if y.bigass:
    print('OK')
print(y.a)
#В чем разница меджу инит и просто аргуметом ка кнапример переменная а,
#В том,что при создании экземпляра Y всё что в ините,переноситься в пространство имен экземляра Y.
#Атрибут А он уже находит в пространстве имен самого класса,так как не нашел
# ВАЖНО.Если атрибут не в инит то он будет ОБЩИМ для всех экземплярчиков.
y.inc()
Initer.inc(y)#вот что такое селф
всё,что тебе нужно знать о селф:
экземпляр.метод(аргументы...) ---- класс.метод(экземпляр, аргументы...)


#_______________задание_1_Коробка с деньгами_____________________________
class MoneyBox:
    def __init__(self,capacity):# это называется конструктор
        self.capacity = capacity
        self.count = 0
    def can_add(self,add:int):
        if self.count + add <= self.capacity:
            return True
        else:
            return False
    def add(self,add:int):
        if self.can_add(add):#внимательно,вызвали таким образом верхний метод
            self.count += add
        else:
            print("OVERFLOW")

wallet = MoneyBox(4000)
wallet.add(4200)
wallet.add(4200)
wallet.add(3999)
wallet.can_add(1)
wallet.can_add(2)
print(wallet.count)


# #НАСЛЕДОВАНИЕ
# #Важно знать: атрибут он будет искать пока не найдет
# #при множественном наследовании он вначале пойдет в класс слева
#
# #Чем отличается класс от экземпляра:Класс это шаблон(фабрика для создания экземп)
# #экземпляр это свой нэймспэйс  в пределах видиости программы,хранит свои уникальные данные
# class Namespaces:
#     spam = 99
#     def setname(self,name):
#         self.name=name
#     def display(self):
#         print(self.name)
# x = Namespaces()
# y = Namespaces()
# x.setname('burgen')
# x.display()
# x.name = "cocosic"
# x.display()
#
# y.name = 'dffd'#вот сдесь ты сделал атрибут экземпляра,а не класса.
# x.display()
# y.display()
#
# x.spam#выведет 99
# y.spam#same
# #but
# x.spam = 456
# x.spam#456
# y.spam#99
##класс показывает,что экз,переоределил для себя атриб.класса по имени data.и в функции display выводит его
# class Mixednames:
#     data = 'sprunk'
#     def __init__(self,value):
#         self.value = value
#     def display(self):
#         print(self.data,Mixednames.data)
# o = Mixednames(1)
# o.display()
# o.data = 'spam'
# o.display()

# class Super:
#     def __init__ (self, x):
#         pass
# class Sub(Super):
#     def __init__ (self, x, y) :
#         Super.__init__ (self, x) # Выполнить метод__ init__ суперкласса
#         pass # Выполнить специальные действия инициализации
# I = Sub(1, 2)

#Наследование
#варианты настройки классов
class Super2:
    def method(self):
        print('in Super.method')
    def abstraction(self):
        self.action()#вот этого метода по-сути еще не существует
    def action(self):
        assert False, 'action must be definded'#защита,на случай,если его вызовут из какого то наследника,у которого
                           #этот метод определен не будет
class Sub(Super2):
    def method(self):
        print('starting Sub. method')
        Super2.method(self)
        print('ending Sub.method')#Sub.method просто расширяет поведение Super.method, а не полностью замещает его:

class Subsub(Super2):
    pass
    def action(self):
        print("Вот он наш метод,указанный в супер-классе")

if __name__ == '__main__':
    for klass in (Sub, Subsub):
        print('\n' + klass.__name__)
        klass().method()
        klass().abstraction()
    print('\nProvider...')
    x = Subsub()
            #Взгляни на супер класс,его называют абстрактным за то,что он определил в методе функцию,которой в при
            #нципе не существует.Остается только надеяться,что ее кто-то применит
#Вложенные классы
X = 1
def nester () :
    X = 2   # Локальное имя: 2
    print(X)
    class С:
        X = 3
        print(X)
        def methodi(self)
            print(X) # В объемлющем def (не 3 в классе!) : 2
            print(self.X)
        def method2(self)
            X = 4 # Скрывает имя из класса
            print(X)
            self.X = 5 # Находится в экземпляре: 5
            print(self.X)
    I = C()
    I.methodi()
    I.method2()
print(X) # Глобальное имя: 1
nester (     # Остаток: 2, 3, 2, 3, 4, 5
print('-'*40)
# Тут пойми,приеритет видимости у Х определенного в функции


def classtree(cls, indent):
    print('.' * indent + cis.__name__ )  # Вывести здесь имя класса
    for supercls in cls.__bases__:#посмотерть кортеж наследников
        classtree(supercls, indent+3)
def instancetree(inst):
    print('Tree of %s' % inst) # Показать экземпляр
    classtree(inst.__class__ , 3) #Подняться к его классу
def selftest():
    class A: pass
    class В(A): pass
    class C(A): pass
    class D (В, C) : pass
    class E: pass
    class F(D,E) : pass
    instancetree(B())
    instancetree(F())
if __name__ == '__main__': selftest ()

#ПЕРЕГРУЗКА ОПЕРАЦИЙ.Это автометоды класса.

class Number:
    def __init__(self,number):
        self.data = number
    def __sub__(self,other):
        return Number(self.data - other)#новый экз.

X = Number(5)
Y = X-2
y.data

#__getitem__  and   __setitem__
class Indexer():
    def __getitem__(self, item):
        return item**2
X = Indexer()
X[5]

#__getattr__ and __setattr__     перехватывает ссылки на атрибуты,смотрит сущ.такой атрибут или нет

class Empty:
    myattr = 220
    def __getattr__(self, item):
        if item == 'myattr':
            return 110
        else:
            raise AttributeError(item)
X = Empty()
print(X.myattr) #Вернет 220
X.asdf #return AttributeError

class Setattr: #перехватывает все присваивания значений атрибутам
    def __setattr__(self, key, value):
        if key == 'name':
            self.__dict__[key] = value + ' - ' + 'New gamer'
        else:
            raise AttributeError(key)
X = Setattr()
X.name = 'Pavel Simonov'
print(X.name)
X.worker


class PrivacyExeptions(Exception):pass #применение сет аттр для защиты атрибутов
class CheckPrivacy(PrivacyExeptions):
    def __setattr__(self, key, value):
        if key in self.privaces:
            raise PrivacyExeptions(key,self)
        else:
            self.__dict__[key] = value
class Test1(CheckPrivacy):
    privaces = ['name','age']
class Test2(CheckPrivacy):
    privaces = ['rule','function']
X=Test1()
Y=Test2()
X.rule = 'Court'
print(X.__dict__)
X.age = 13

__repr__
class BeautyInput:
    def __init__(self,value = None):
        self.value = value
    def __repr__(self):#без нее выведет : <__main__.BeautyInput object at 0x0000027AD8A47288>
        return 'Attribut(%s)' % self.value
X = BeautyInput()
print(X)
X.value = 10
print(X)

#__call__
class Call:#хочу отметить трюки с передачами аргументов.
    def __call__(self, *args, **kwargs):
        print('Called',args,kwargs)
X = Call()
X(1,3,4,i='req')
X(*(1,2,3,4,5,6),**dict(s=2,r=9))

#Bonus функция замыкания
def callback(color):
    def onecall():
        print('turn',color)
    return onecall

color = callback('Yellow')
color()

#Проектирование с использованием классов!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!





