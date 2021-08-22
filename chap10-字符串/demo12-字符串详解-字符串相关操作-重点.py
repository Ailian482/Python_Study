# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/8/21 下午9:59

"""

"""
var = 'iloveyoutosimimadaandilikeyou'
# 1. 检测一个字符串是否存在于一个字符串中
res = 'loves' in var
print(res)  # False

# 2. 获取字符串的长度 len()
res_len = len(var)
print(res_len)  # 29

# ==================== 字符串查找相关函数=======================
# 3. str.find(sub[, start[, end]])
# 从左向右 获取指定字符在字符串中第一次出现(多个字符则第一个字符)的索引位置，未找到则返回 -1
res_f = var.find("you")
print(res_f)  # 5
res_f1 = var.find('you', 9, 29)
print(res_f1)  # 26
res_f1 = var.find('you', 9, 27)
print(res_f1)  # -1

# 4. str.rfind(sub[, start[, end]])
# # 从右向左 获取指定字符在字符串中第一次出现(多个字符则第一个字符)的索引位置，未找到则返回 -1
res_fr = var.rfind('you')
print(res_fr)  # 26
res_fr1 = var.find('you', 0, 10)
print(res_fr1)  # 5

# 5. str.index()  和 find 方法一样，只不过如果没有找到则 报错
res_i = var.index('you')
print(res_i)  # 5
# res_i1 = var.index('yous')
# print(res_i1)  # ValueError: substring not found

# 6. str.rindex()  和 rfind 方法一样，只不过如果没有找到则 报错

# 7. str.count(sub[, start[, end]])  统计一个字符在字符串中出现的次数
res_c = var.count('you')
print(res_c)  # 2

# ============================================================
str = "user_admin_id_123"
# 8. str.split(sub[, count])  按照指定的字符 从左向右 进行分割，把一个字符串分割成一个列表
sut = str.split('_')
print(sut)  # ['user', 'admin', 'id', '123']

# 可以指定分割的次数
sut_1 = str.split('_', 2)
print(sut_1)  # ['user', 'admin', 'id_123'] 只分割了两次

# 练习，将下面字符串进行分割，规则，每一组按 & 分割，然后获取每一组的 等号 右边的值
str_1 = 'uid=123&type=ab&kw=hh'
key_list = str_1.split("&")
res_list = []
for i in key_list:
    r = i.split('=')
    # print(r.pop())  # pop() 从集合中移除并返回任意一个元素，如果集合为空，则会返回引发 KeyError
    res_list.append(r[1])
print(res_list)  # ['123', 'ab', 'hh']

# 9. str.rsplit(sub[, count])  按照指定的字符 从右向左 进行分割，把一个字符串分割成一个列表
sut_r = str.rsplit('_')
print(sut_r)  # ['user', 'admin', 'id', '123']

# 可以指定分割的次数
sut_r1 = str.rsplit('_', 2)
print(sut_r1)  # ['user_admin', 'id', '123'] 只分割了两次

# 10. str.join()  按照指定的字符，把容器类型中的数据连接成一个字符串
var_list = ['user', 'admin', 'id', '123']
str_join = '@'.join(var_list)
print(str_join)  # user@admin@id@123

# 11. str.strip()  可以去除字符串左右两侧的指定字符
var_s = '#####这是一个文章的标题###'
ret_s = var_s.strip('#')
print(var_s, len(var_s))  # #####这是一个文章的标题### 17
print(ret_s, len(ret_s))  # 这是一个文章的标题 9

# 12. str.rstrip()  可以去除字符串右两侧的指定字符
# 13. str.lstrip()  可以去除字符串左两侧的指定字符

# 14. str.replace(原字符串要替换的字符, 替换字符[, 替换个数])  替换
var_r = 'iloveyoutosimimadaandiloveyou'
ret_r = var_r.replace('love', 'like')
print(ret_r)  # ilikeyoutosimimadaandilikeyou
ret_r1 = var_r.replace('love', 'like', 1)
print(ret_r1)  # ilikeyoutosimimadaandiloveyou

# 15. str.center(num[,sub])  如果字符串 var_c 不够10个长度，那么就用 sub 将在原字符串 var_c 左右两边补到 num个长度，在原字符串左右两边
var_c = 'love'
ret_c = var_c.center(10, "*")
print(ret_c, 'ret_c的长度为：{}'.format(len(ret_c)))  # ***love*** ret_c的长度为：10

# 16. str.rjust(num[, sub])  如果字符串 var_c 不够10个长度，那么就用 sub 将在原字符串 var_c 右侧补到 num个长度，在原字符串左右两边
# 17. str.ljust(num[, sub])  如果字符串 var_c 不够10个长度，那么就用 sub 将在原字符串 var_c 左侧补到 num个长度，在原字符串左右两边

