# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/13 下午5:00


"""
任务描述：
    将文件（/Users/developer/Desktop/test.txt）中的数据进行分割并且按照以下规律保存起来：
    - 小甲鱼的对话单独保存为 boy_*.txt的文件（去掉"小甲鱼:"）
    - 小客服的对话单独保存为 girl_*.txt的文件（去掉"小客服：）
    - 文件中总共有三段对话，分别保存为boy_1.txt，girl_1.txt，boy_2.txt，girl_2.txt，boy_3.txt，girl_3.txt共6个文件
      （提示：文件中不同的对话间已经使用"=============="分割

文件内容：
    小客服：小甲鱼，今天有客户问你有没有女朋友？
    小甲鱼：咦？？？
    小客服：我跟她说你有女朋友了！
    小甲鱼：。。。
    小客服：她让你分手后考虑下她！然后我说:"您要买个优盘，我就帮您留意下~"
    小甲鱼：然后呢？
    小客服：她买了两个，说发一个货就好了~
    小甲鱼：呃。。。。。。。。你真牛！
    小客服：那是，谁让我是语C最可爱的小客服嘛~
    小甲鱼：下次有人想调戏你我不阻止~
    小客服：滚！！！
    =====================================================================
    小客服：小甲鱼，有个好评很好笑哈。
    小甲鱼：哦？
    小客服："有了小甲鱼，妈妈以后不用担心我的学习了~"
    小甲鱼：哈哈哈，我看到了呀，我还发微博呢~
    小客服：嗯嗯，我看了你的微博呀~
    小甲鱼：哟西~
    小客服：那个有条回复"左手拿着小甲鱼，右手拿着打火机，哪里不会点哪里，so_easy！"
    小甲鱼：T_T
    =====================================================================
    小客服：小甲鱼，今天一个会员想找你
    小甲鱼：哦？什么事？
    小客服：她说一个学生月薪已经超过12K了
    小甲鱼：哪里的？
    小客服：上海的
    小甲鱼：那正常，那家公司？
    小客服：他没说呀
    小甲鱼：哦
    小客服：老大，为什么我工资那么低啊？？是时候涨涨工资了！
    小甲鱼：啊，你说什么？我在外边呢，这里好吵呀。。。。。。
    小客服：滚！！！

"""

f = open('test.txt')
boy = []
girl = []
count = 1
for each_line in f:
    if each_line[:6] != '======':
        # 我们这里进行字符串分割操作
        (role, line_spoken) = each_line.split("：", 1)
        if role == '小甲鱼':
            boy.append(line_spoken)
        if role == '小客服':
            girl.append(line_spoken)
    else:
        # 文件的分别保存操作
        # 起文件名
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'
        # 新建文件，打开文件
        boy_file = open(file_name_boy, 'w')
        girl_file = open(file_name_girl, 'w')
        # 把对话内容保存到文件
        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()
        # 初始化 boy和girl 列表，不然会保存有上一次的对话内容
        boy = []
        girl = []
        count += 1


file_name_boy = 'boy_' + str(count) + '.txt'
file_name_girl = 'girl_' + str(count) + '.txt'
# 新建文件，打开文件
boy_file = open(file_name_boy, 'w')
girl_file = open(file_name_girl, 'w')
# 把对话内容保存到文件
boy_file.writelines(boy)
girl_file.writelines(girl)

boy_file.close()
girl_file.close()

f.close()
