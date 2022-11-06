from main import MainWindow
from ui_Calc import *


class pageFunc(MainWindow):
        def stacked1(self):
                self.ui.standard_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border-left: 5px solid rgb(3, 111, 196);\n"
"	text-align:left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}")
                self.ui.Scientific_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	text-align:left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}")
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
                self.ui.Currency_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	text-align:left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}")

                

                if self.ui.stackedWidget.currentIndex() == 0:
                        pass
                else:
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
                        self.ui.stackedWidget.setCurrentIndex(0)
                        if self.ui.history_scrl.height() == 421:
                                self.ui.history_scrl.setFixedHeight(0)
                        if self.ui.history_btn.x() != 400:
                                self.ui.history_btn.move(400,33)

        def stacked2(self):
                self.ui.Scientific_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border-left: 5px solid rgb(3, 111, 196);\n"
"	text-align:left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}")
                self.ui.standard_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	text-align:left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}")
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
                self.ui.Currency_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	text-align:left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}")

                if self.ui.stackedWidget.currentIndex() == 1:
                        pass
                else:
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
                self.ui.stackedWidget.setCurrentIndex(1)
                if self.ui.history_scrl.height() == 421:
                        self.ui.history_scrl.setFixedHeight(0)
                if self.ui.history_btn.x() != 400:
                        self.ui.history_btn.move(400,33)

        

        def stacked3(self):
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
                self.ui.standard_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	text-align:left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}")
                self.ui.Scientific_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	text-align:left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}")    
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

                

                if self.ui.stackedWidget.currentIndex() == 2:
                        pass
                else:
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

                        with open("data\data.txt", "r") as f:
                                data = f.read()
                                self.ui.update_lbl.setText(data)
                        self.ui.stackedWidget.setCurrentIndex(2)
                        if self.ui.history_scrl.height() == 421:
                                self.ui.history_scrl.setFixedHeight(0)
                        if self.ui.history_btn.x() == 400:
                                self.ui.history_btn.move(450,33)


        def about(self):
                self.ui.standard_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	text-align:left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}")
                self.ui.Scientific_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	text-align:left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}")    
                self.ui.Currency_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	text-align:left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}")    

                

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


                else:
                        self.ui.about.setFixedHeight(181)
                        self.ui.about_btn.setStyleSheet(u'''QPushButton {\n
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
                        