# -*- coding: utf-8 -*-

import types # 包含类型的定义
from enum import Enum
from types import MethodType

# 建立类
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, self.age)

tom = Student('Tom', '19')
# tom.print_info()

# 限制对类的访问
class Person():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 0 <= age <= 100:
            self.__age = age
        else:
            raise ValueError('bad age')

lisa = Person('Lisa', 18)
lisa.set_age(20)
# print(lisa.get_age())

# 继承和多态,子类继承父类的属性和方法，但是可以重写
class Animal():
    def run(self):
        print('animal')

class Dog(Animal):
    def run(self):
        print('dog')

# 没有继承Animal
class Cat():
    def run(self):
        print('cat')

dog = Dog()
# dog.run()

def run_twice(animal):
    animal.run()
    animal.run()

# run_twice(Animal())
# run_twice(Dog())
# run_twice(Cat()) # 仍然输出cat，python传入的参数不一定必须是Animal或其子类，只要具有run方法的类即可。（鸭子类型）

# 类型判断
# print(type(123)) # int
# print(type(1.23)) # float
# print(type('123')) # str
# print(type(int)) # type

# print(type(lambda x: x) == types.LambdaType) # True

# 实例判断, 子类的对象是父类的实例，反之不成立，基本类型也可以用isinsrance来判断
# print(isinstance(dog, Animal)) # True
# print(isinstance(dog, Dog)) # True
# print(isinstance([1,2,3], (list, tuple))) # True


# 获取一个对象的所有属性和方法:dir(),以list形式返回
# print(dir('abc'))

# 可以通过重写对象的方法来改变获取的值

# 获取并操纵对象的属性
animal = Animal()
# print(hasattr(animal, 'age')) # False
setattr(animal, 'age', 20)
# print(hasattr(animal, 'age'), getattr(animal, 'age'))  # True 20

# 可以对不存在的属性设置访问时返回的默认值
# getattr(animal, 'name', 'no name')

# 实例属性和类属性，实例属性通过self绑定，类属性直接定义
class Plant():
    name = 'Plant'

plant = Plant()
# 实例没有name属性时，会打印类的name属性，若实例有相应的属性，则打印实例的属性
# print(plant.name)
plant.name = 'flower' # 给实例添加name属性， 动态绑定属性
# print(plant.name)

# 给实例动态绑定属性和方法
class Tree():
    pass

tree = Tree()

def set_age(self, age):
    self.age = age

tree.set_age = MethodType(set_age, tree)
tree.set_age(25)
# print(tree.age)

# 直接对实例绑定的属性和方法，对该类的其他实例不起作用
# tree1 = Tree()
# print(tree1.age)

# 可以通过给类直接绑定属性和方法，使其对类的所有实例都起作用
Tree.set_age = set_age
tree1 = Tree()
tree1.set_age(20)
# print(tree1.age)

# 使用__slots__限制可以对实例添加的属性和方法,但仅对当前类的实例起作用，对类的子类的实例不起作用
class Teacher():
    __slots__ = ('name', 'age')

# python可以使用多重继承,主功能之外的类，一般有Mixin
# class Bird(Animal, Dog):
#     pass

Weekday = Enum('Weekday', ('Sun', 'Mon', 'Tue', 'Wed'))

# for name, member in Weekday.__members__.items():
#     print(name, member, member.value)
# Sun Weekday.Sun 1
# Mon Weekday.Mon 2
# Tue Weekday.Tue 3
# Wed Weekday.Wed 4

class Color(Enum):
    red = 1
    black = 2
    green = 3

# 有多种方法可以访问枚举常量
# print(Color.red)
# print(Color['red'])
# print(Color(1))
# print(Color.red.value)


# python的函数和类的定义是在运行时用type()动态创建的
def fn(self, name = 'word'):
    print('hello %s' % name)

Hello = type('Hello', (object,), dict(hello = fn))
h = Hello()
h.hello()
# type的第一个参数为类名，第二个参数为继承的父类集合(tuple),第三个参数为方法名称与函数绑定

# 使用元类,通过元类茶 u 能感觉爱你出类，再创建实例
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls. name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
print(L)