'''class多次继承'''

class A:
    kk = 0
    def __init__(self,name):
        print("A:顶层父类")
        self.name = name

    def say(self):
        print("A说：我是{}".format(self.name))

class B(A):
    kk = 10
    # def __init__(self,name):
    #     self.name = name

    def say(self):
        print("B说：我是{}".format(self.name))


class C(B):
    kk = 22
    # def __init__(self,name):
    #     self.name = name

    def say(self):
        print("C说：我是{}".format(self.name))


aa = A("aa")
bb = B("bb")
cc = C("cc")

aa.say()
bb.say()
cc.say()
