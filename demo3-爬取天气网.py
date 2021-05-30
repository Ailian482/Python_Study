
def ABS(x):
    # x为0或者正数，直接输出x本身
    if type(1) == type(x):
        if x >= 0:
            return x
        else:
            return -x
    else:
        print("TypeError")

print(ABS(-10))


print(abs(2))

print(hex(10))

print(oct(10))

print(bin(10))

class Dog(object):
    def __init__(self, name):
        self.dog_name = name

    @classmethod
    def eat(cls, dog_name, food):
        print("%s喜欢吃%s" % (dog_name, food))


# 有 @classmethod，在类上进行调用函数，类函数名.类方法()
Dog.eat("阿黄", "骨头")




class Dog(object):
    def __init__(self, name):
        self.dog_name = name

    def eat(self, food):
        print("%s喜欢吃%s" % (self.dog_name, food))

# 没有 @classmethod，在实例上进行调用函数，类函数名().类方法()
Dog("阿虎").eat("骨头")



