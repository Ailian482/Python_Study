# 1. 导入包
import xlwings as xw

# 2. 创建 APP 应用对象，即打开 WPS Office 应用
# app = xw.App(visible=True, spec='WPSOffice')
# pid1 = app.pid  # 通过这个 pid 去指定操作打开的应用
# print(pid1)

app = xw.apps[95341]  # 指定打开的应用
app.activate()  # 激活应用，激活之后，才能操作应用（例如：新建工作簿、在工作簿写内容）
wb = app.books.add()  # 新建一个工作簿
sht = wb.sheets['Sheet1']  # Sheet1 是 sheet 表的名称
sht.range('A1').value = 'hahaha Hello Python!'  # 指定单元格 输入内容
wb.save()  # 保存工作簿
wb.close()  # 关闭工作簿
app.kill()  # 关闭应用，即释放资源





"""
xlwings 操作 Excel 表格时报错：
    aem.findapp.ApplicationNotFoundError: Local application 'Microsoft Excel.app' not found
原因分析：
    报错意思是电脑本地找不到 Microsoft Excel.app。我的 Mac 上只有 WPS，所以在启动 xlwings 的时候需要指定 WPS。例如：
        app = xw.App(spec='wpsoffice')    
"""
# app = xw.App(spec='wpsoffice')
# pid = app.pid
# print(pid)
#
# app = xw.apps
# print(app.count)