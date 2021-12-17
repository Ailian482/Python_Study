import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

"""
VBoxLayout：垂直盒布局
Application：应用
Widget：微件，是一种web2.0的衍生物，就像是一个小型的应用程序
        以往Widget 只可以通过本身的嵌入代码添加到网页当中，如今可以将这些Widget 直接添加到自己的电脑桌面来使用，从而增加桌面的功能性。
        很多网站现在已经有了自己的Widget，你可以直接从这些网站中获取Widget 的嵌入代码，然后直接将他们添加到你的桌面或者博客上。
Label：标签
"""

# 建立application对象
app = QApplication(sys.argv)
# 建立窗体对象
Window = QWidget()
# 设置窗体大小
Window.resize(500, 500)

# 设置样式
Window.layout = QVBoxLayout()
Window.label = QLabel("Hello World!")
Window.setStyleSheet("font-size:25px;margin-left:155px;")
Window.setWindowTitle("PyQt5 窗口")
Window.layout.addWidget(Window.label)
Window.setLayout(Window.layout)

# 显示窗体
Window.show()
# 运行程序
sys.exit(app.exec_())
