# codeing=utf-8
# @Time    : 2017-09-29
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : python面向对象编程（OOP）初探
# @Url     : http://www.17python.com/
# @Details : python面向对象编程（OOP）初探
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# python面向对象编程（OOP）初探
###################################
'''
## 面向对象编程

说起面向对象编程，除了那些晦涩抽象的定义，我脑海中印象比较深的就是那张王宝强的表情图：程序员？面向对象编程？哈哈哈没有对象你编毛程？

## 三大特征

学过java的同学应该非常的了解这三个特征：*封装、继承、多态*
在Python的世界中，一切都是对象，为什么要用面向对象模式来进行编程？因为这样更接近人类对自然的认识过程，更直观，如果对面向编程的理论不太了解，建议百度搜索相关知识了解一下。

## Python中的Class

在Python中定义一个Class是非常简单的，语方法如下：

    Class classname(object):
        pass

其中（object）是用来定义需要继承的父类，Python中，可以继承多个类，这个与java的单继承不同。


'''


def run():
    print("我会跑！")


class Animal(object):
    k = 0  # 类属性

    def __init__(self, name):  # 类构造器
        self.name = name  # 实例的属性
    # 实例的方法

    def say(self):
        Animal.k += 1
        print("{0}:我会呼吸！".format(self.name))
        print("Animal.k={0}".format(Animal.k))


a = Animal("aaaa")
a.say()  # 执行实例的方法
print("Animal.k:{0}".format(Animal.k))  # 打印类属性
print(Animal.__init__)
print(Animal.say)
Animal.m = 1
a.color = "red"  # 动态的添加属性
a.run = run()  # 动态的添加属性
print("我的颜色是=%s" % a.color)
print("Animal.m=%s" % Animal.m)
print("a.m=%s" % a.m)
# print("Animal.a：%s" % Animal.a)  这里会抛出错误

'''
上这的实例不难发现，在类中，包括`k`类变量、`self.name`实例变量、`say`实例的方法，这些成员，都是类的的属性。
Python中的实例对象可以动态的添加类变量及实例变量，只需要点一个`.`这和Java不同（当然Java也可以通过反射aop切面方式动态为对象添加功能方法）。

## 构造器和self

`__init__(self)`类中的这个特殊方法就是类的构造器，`self`代表着这个类创建的对象。
关于成员变量我们可以这样理解：对象和类说：`关于变量，你的就是我的，我的确只是我的。`


## Python的继承

Python中，类的继承很简单方便，看下下边的代码
'''


class Dog(Animal):
    k = 999  # 我们定义了一个与父类相同的类变量

    def __init__(self, name):  # 同样定义了一个相同名称的实例变量
        Animal.__init__(self, name)  # 注意这里没有:::::号

    def say(self):
        print(self.name + ":我的叫声是：汪汪汪！")
        print("Dog.k={0}".format(Dog.k)),


dog = Dog("wangwang")
dog.say()
print("Animal.k:{0}".format(Animal.k))  # 打印父类属性
print("Dog.k:{0}".format(Dog.k))  # 打印子类属性
# dog.run #这个动态添加到父类创建的实例中的变量是无法继承过来的。 非得执行的话会报错。

'''
通过上边的例子，我们不难看出，类继承后，实例的变量是可以继承的，通过调用父类的`__init__()`方法来简化实例构造。
但是父类的类属性是无法继承的，他们互相独立存在在内存中。
`Dog`类中的也有一个`say()`的方法，象这样与父类拥有相同的方法名称而具有不相同的执行结果的行为叫做方法重写。

## 多态

我们在创建一个新类继承`Animal`
'''


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def say(self):
        print(self.name + ":我的叫声是：喵喵喵")


cat = Cat("Tom")
cat.say()

'''
`isinstance()`函数，可以用来判断一个变量是否是某个类，我们测试一下

'''

print(isinstance(cat, Cat))  # True
print(isinstance(cat, Animal))  # True
print(isinstance(a, Animal))  # True
print(isinstance(a, Cat))  # False

'''
很明显，动物的对象不能说成是猫，但猫的对象可以是猫类，说猫是动物类也没什么错误。也就是说，继承是从上到下。
那多态是什么？我们还需要一个函数，然后来看看。

'''


def isay(animal):
    animal.say()


isay(a)  # aaaa:我会呼吸！
isay(dog)  # wangwang:我的叫声是：汪汪汪！
isay(cat)  # Tom:我的叫声是：喵喵喵

'''
通过`isay()`方法的输出，我们多少对多态这个概念有那么一点了解了，回想当年学Java的多态的时候，和现在的情况大同小异乎？
如果我们随便建一个类，包括`say()`方法，然后用`isay()`方法输出打印，会不会也是产生多态的效果呢？
答案是：会的！在`Pyhong`中，这就是动态语言的“鸭子类型”，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
然在`Java`静态语言中，则会对父类进行检查，如果不是同一个父类，那么就会报错。

好吧，有关Python类，对象相关先说到这里，希望大家国庆节快乐哦！

'''
