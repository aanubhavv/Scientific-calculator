from main import MainWindow
from ui_Calc import *

class menufunc(MainWindow):
    def togglemenu(self, enable):

        if enable:
            width = self.ui.side_bar.width()

            if width == 0:
                self.ui.side_bar.setFixedWidth(151)
                self.ui.menu_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 2px solid rgb(30, 30, 30);\n"
"	padding-top: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}")
            else:

                if self.ui.about.height() == 181:
                    self.ui.about.setFixedHeight(0)
                    self.ui.about_btn.setStyleSheet(u"QPushButton {\n"
        "	color: rgb(255, 255, 255);\n"
        "	background-color: rgb(30, 30, 30);\n"
        "	text-align:left;\n"
        "	padding-left: 10px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "	color: rgb(255, 255, 255);\n"
        "	background-color: rgb(147, 147, 147);\n"
        "}")

                    page =  self.ui.stackedWidget.currentIndex()
                    if page == 0:
                            self.ui.standard_btn.setStyleSheet(u'''QPushButton {\n
    color: rgb(255, 255, 255);\n
    background-color: rgb(30, 30, 30);\n
    border-left: 5px solid rgb(3, 111, 196);\n
    text-align:left;\n
    padding-left: 10px;\n
}\n
QPushButton:hover {\n
    color: rgb(255, 255, 255);\n
    background-color: rgb(147, 147, 147);\n
}''')

                    elif page == 1:
                            self.ui.Scientific_btn.setStyleSheet(u'''QPushButton {\n
    color: rgb(255, 255, 255);\n
    background-color: rgb(30, 30, 30);\n
    border-left: 5px solid rgb(3, 111, 196);\n
    text-align:left;\n
    padding-left: 10px;\n
}\n
QPushButton:hover {\n
    color: rgb(255, 255, 255);\n
    background-color: rgb(147, 147, 147);\n
}''')

                    elif page == 2:
                            self.ui.Currency_btn.setStyleSheet(u'''QPushButton {\n
    color: rgb(255, 255, 255);\n
    background-color: rgb(30, 30, 30);\n
    border-left: 5px solid rgb(3, 111, 196);\n
    text-align:left;\n
    padding-left: 10px;\n
}\n
QPushButton:hover {\n
    color: rgb(255, 255, 255);\n
    background-color: rgb(147, 147, 147);\n
}''')

                self.ui.side_bar.setFixedWidth(0)
                self.ui.menu_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid rgb(44, 44, 44);\n"
"	padding-top: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}")




