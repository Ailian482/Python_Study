# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/8/22 下午12:10

var_list = ['刘德华', '张学友', '张国荣', '张学友', '黎明', '郭富城', '小沈阳', '刘能', '宋小宝', '赵四']
# 1. len(list)  检测当前列表的长度，列表中元素的个数
res = len(var_list)  # 9

# 2. list.count()  检测当前列表中指定元素出现的次数
res_c = var_list.count('张学友')  # 2

# 3. list.append()  向列表的尾部追加新的元素，返回值为None
var_list.append('阿君')  # 返回值为 None
print(var_list)  # ['刘德华', '张学友', '张国荣', '张学友', '黎明', '郭富城', '小沈阳', '刘能', '宋小宝', '赵四', '阿君']

# 4. list.insert(index, sub)  向指定的索引位置添加元素，当指定的位置超出列表长度，则在列表尾部添加，不会报错
var_list.insert(20, '小朱')
print(var_list)  # ['刘德华', '张学友', '张国荣', '张学友', '黎明', '郭富城', '小沈阳', '刘能', '宋小宝', '赵四', '阿君', '小朱']

# 5. list.pop(index)  可以对列表中指定的索引位置上的元素做 出栈 操作，返回出栈的元素，如果索引位置超出范围，则会报错
res_p = var_list.pop()  # 默认会把列表中最后的一个元素出栈
res_p5 = var_list.pop(5)
print(res_p)  # 小朱
print(res_p5)  # 郭富城
print(var_list)  # ['刘德华', '张学友', '张国荣', '张学友', '黎明', '小沈阳', '刘能', '宋小宝', '赵四', '阿君']

# 6. list.remove(sub)  可以指定列表中的元素进行 删除，只删除第一个，如果没有找到，则会报错
var_list.remove('刘德华')  # 返回值为 None
print(var_list)  # ['张学友', '张国荣', '张学友', '黎明', '小沈阳', '刘能', '宋小宝', '赵四', '阿君']

# 7. list.index(sub[,start [, end]])  可以查找指定元素在列表中第一次出现的索引位置
res_i = var_list.index('张学友')
print(res_i)  # 0
res_i1 = var_list.index('阿君', 3, 16)
print(res_i1)  # 8

# 8. list.extent(sub)  接收一个容器类型的数据，把容器中的元素追加到原列表中
var_list.extend([1, 2, 3, 4, 5, 6])  # 返回值为 None
var_list.extend('小朱')
print(var_list)  # ['张学友', '张国荣', '张学友', '黎明', '小沈阳', '刘能', '宋小宝', '赵四', '阿君', 1, 2, 3, 4, 5, 6, '小', '朱']

# 9. list.clear()  移除列表中的所有元素
# var_list.clear()  # 返回值为 None
# print(var_list)  # []

# 10. list.reverse()  列表翻转
var_list.reverse()  # 返回值为 None
print(var_list)  # ['朱', '小', 6, 5, 4, 3, 2, 1, '阿君', '赵四', '宋小宝', '刘能', '小沈阳', '黎明', '张学友', '张国荣', '张学友']

# 11. list.sort([reverse=True/False])  默认对列表进行从小到大排序，直接改变列表元素的顺序
var_list = ['刘德华', '张学友', '张国荣', '张学友', '黎明', '郭富城', '小沈阳', '刘能', '宋小宝', '赵四']
var_list.sort()
print(var_list)  # ['刘德华', '刘能', '宋小宝', '小沈阳', '张国荣', '张学友', '张学友', '赵四', '郭富城', '黎明']
var_list.sort(reverse=True)  # 从大到小反向排序
print(var_list)  # ['黎明', '郭富城', '赵四', '张学友', '张学友', '张国荣', '小沈阳', '宋小宝', '刘能', '刘德华']

# 12. list.re([reverse=True/False])  默认对列表进行从小到大排序，取出列表中的元素重新排序，不会改变原列表的顺序
paixu = sorted(var_list)
print(paixu)  # ['刘德华', '刘能', '宋小宝', '小沈阳', '张国荣', '张学友', '张学友', '赵四', '郭富城', '黎明']
print(var_list)  # ['黎明', '郭富城', '赵四', '张学友', '张学友', '张国荣', '小沈阳', '宋小宝', '刘能', '刘德华']

