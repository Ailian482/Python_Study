import xlwt

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet1")
# 这里开始插入数据
# 循环插入10万条数据
for i in range(100000):
    sheet1.write(i,0,"data"+str(i))
book.save("data.xls")
