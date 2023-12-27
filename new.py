# sum = 0
# for i in range(1, 100):
#     sum = sum + i
#
# print(sum)

"""
md5算法，是一个不可逆的加密算法，因 md5 的不可逆性，并且加密长度固定，可以是 32位 或者 16位（去掉 md5 的前后 8 位），
一般应用于密码加密，或者验证API接口的签名，在项目应用当中，经常会用到，特别是API请求的签名验证，这样可以很有效的保证数据的安全性和传输数据的可控性。

什么是不可逆的呢？
    就是不能通过加密后的内容得到加密前的内容
"""
import hashlib

# corpCode = "666888999"
# password = "@12345678"
corpCode = "32131"
password = "a1111111"

# 1. md5 加密
sign = hashlib.md5((corpCode + hashlib.md5(password.encode('utf-8')).hexdigest()).encode('utf-8')).hexdigest()
print(sign)

# 2. 使用 update 方法
""" update 有拼接的效果
    如下方的例子中：
        两次传入要加密的值 password 都是一样的，但是两次生成的 md5加密值 是不一样的
        第二次生成的 md5加密值 是与 password+password 一样的，即 sign_1=sign_2
    为了避免加密值被拼接，加密新的内容时，需要重新定义 hashlib.md5()
"""
m2 = hashlib.md5()  # 创建 md5 对象
m2.update(password.encode(encoding='utf-8'))  # 第一次传入加密内容为 password
sign = m2.hexdigest()
print(sign)  # ef209c9343ca8c715265781876657b18
m2.update(password.encode(encoding='utf-8'))  # 第二次传入加密内容为 password，使用update其实是已经拼接成 password+password 了
sign_1 = m2.hexdigest()
print(sign_1)  # 4fd7ffc8f8b9025e8dec9cedf18092f1

m2 = hashlib.md5()  # 需要重新定义
m2.update((password+password).encode('utf-8'))  # 加密内容为  password+password = "a1111111a1111111"
sign_2 = m2.hexdigest()
print(sign_2)  # 4fd7ffc8f8b9025e8dec9cedf18092f1

# 3. 使用 binascii 库解码
# import binascii
#
# md = hashlib.md5(password.encode(encoding='utf-8'))
# print(md.hexdigest())  # 获取加密后的字符串
# print(md.digest())  # 获取16进制的加密值
#
# print(binascii.hexlify(md.digest()).decode(encoding='utf-8'))  # 转换16进制的加密值为字符串
# print(binascii.unhexlify(md.hexdigest()))  # 将字符串转换为16进制


# print('32位加密串小写', m2.hexdigest())
# print('32位加密串大写', m2.hexdigest().upper())
# print('16位加密串小写', m2.hexdigest()[8:24])
# print('16位加密串大写', m2.hexdigest().upper()[8:24])
