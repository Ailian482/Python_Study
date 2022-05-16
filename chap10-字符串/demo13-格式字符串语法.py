# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2022/4/27 下午5:31

# 按位置访问参数
print('{0}, {1}, {3}'.format(*'abcd'))

# 按名称访问参数
print('{latitude}, {longitude}, {latitude}'.format(latitude='37.24N', longitude='-115.89W'))
coder = {'latitude': '37.24N', 'longitude': '-115.89W'}
print('coders:{latitude}, {longitude}, {longitude}'.format(**coder))
# 访问参数的属性
a = 3 -6j
print("The complex number {0} is formed from the real part {0.real} "
      "and the imaginary part {0.imag}.".format(a))


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)

class Test(object):
    def  __init__(self, *value):
        self.data = value

class TestStr(Test):
    def __str__(self):
        return '[value]: %s' % self.data

print(TestStr([12, 23, 45, 65]))
# print(str(Point(3, 6)))
#
# # 访问参数的项
# coord_1 = (3, 5)
# print('X:{0[0]}; Y:{0[1]}'.format(coord_1))
#
# # 替换 %s 和 %r
# print("repr() shows quotes: {!r}; str() dosen't: {!s}".format('test1', 'test2'))
#
# # 对齐文本以及指定宽度
# print("{:<30}".format("left aligned"))
# print("{:>30}".format("right aligned"))
# print("{:>30}".format("Ailian aligned Ailian aligned Ailian aligned Ailian aligned Ailian aligned"))
# print("{:^60}".format('center'))
# print()
