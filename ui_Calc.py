# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CalcQdhKoQ.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(441, 671)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"resources/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(44, 44, 44)")
        self.actionNornal = QAction(MainWindow)
        self.actionNornal.setObjectName(u"actionNornal")
        self.actionScientific = QAction(MainWindow)
        self.actionScientific.setObjectName(u"actionScientific")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setBold(True)
        self.centralwidget.setFont(font1)
        self.centralwidget.setStyleSheet(u"QToolTip { \n"
"	color: rgb(255, 255, 255); \n"
"	border: 2px solid rgb(125, 125, 125);\n"
"	background-color: rgb(0, 0, 0); \n"
"	padding: 3px;\n"
"}\n"
"\n"
"/* COMBO BOXES */\n"
"\n"
"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(44, 44, 44);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	color: rgb(148, 148, 148);\n"
"	\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	background-color: rgb(44, 44, 44);\n"
"	background-image: url(D:/Programming/Python/Calculator/resources/arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(58, 58, 58);\n"
"	selection-background-color: rgb(255, 255, 127);\n"
"	border: none;\n"
"}\n"
"\n"
"/* VERTICAL SCROLL BARS */\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb("
                        "255, 255, 255);\n"
"    width: 4px;\n"
"    margin: 6px 0 6px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(197, 197, 197);\n"
"    min-height: 25px;\n"
"	border-radius: 8px\n"
" }\n"
"QScrollBar::handle:vertical:hover {	\n"
"	background: rgb(138, 138, 138);\n"
"    min-height: 25px;\n"
"	border-radius: 8px;\n"
" }\n"
"\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 5px;\n"
"	border-bottom-left-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 5px;\n"
"	border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
""
                        "\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* HORIZONTAL SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 4px;\n"
"    margin: 0px 6px 0 6px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {	\n"
"	background: rgb(138, 138, 138);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(197, 197, 197);\n"
"    min-width: 25px;\n"
"	border-radius: 8px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 5px;\n"
"	border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 5px;\n"
"	border-top-left-radius: 8px;\n"
"    border-bottom-le"
                        "ft-radius: 8px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 40, 441, 701))
        self.stackedWidget.setFont(font1)
        self.standard = QWidget()
        self.standard.setObjectName(u"standard")
        self.TwoButton = QPushButton(self.standard)
        self.TwoButton.setObjectName(u"TwoButton")
        self.TwoButton.setGeometry(QRect(110, 492, 111, 70))
        font2 = QFont()
        font2.setPointSize(14)
        self.TwoButton.setFont(font2)
        self.TwoButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.EightButton = QPushButton(self.standard)
        self.EightButton.setObjectName(u"EightButton")
        self.EightButton.setGeometry(QRect(110, 354, 111, 70))
        self.EightButton.setFont(font2)
        self.EightButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.ThreeButton = QPushButton(self.standard)
        self.ThreeButton.setObjectName(u"ThreeButton")
        self.ThreeButton.setGeometry(QRect(220, 492, 111, 70))
        self.ThreeButton.setFont(font2)
        self.ThreeButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.SevenButton = QPushButton(self.standard)
        self.SevenButton.setObjectName(u"SevenButton")
        self.SevenButton.setGeometry(QRect(0, 354, 111, 70))
        self.SevenButton.setFont(font2)
        self.SevenButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.MultiplyButton = QPushButton(self.standard)
        self.MultiplyButton.setObjectName(u"MultiplyButton")
        self.MultiplyButton.setGeometry(QRect(330, 354, 111, 70))
        self.MultiplyButton.setFont(font2)
        self.MultiplyButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.ZeroButton = QPushButton(self.standard)
        self.ZeroButton.setObjectName(u"ZeroButton")
        self.ZeroButton.setGeometry(QRect(110, 561, 111, 70))
        self.ZeroButton.setFont(font2)
        self.ZeroButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.OneButton = QPushButton(self.standard)
        self.OneButton.setObjectName(u"OneButton")
        self.OneButton.setGeometry(QRect(0, 492, 111, 70))
        self.OneButton.setFont(font2)
        self.OneButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.BackButton = QPushButton(self.standard)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setGeometry(QRect(330, 216, 111, 70))
        self.BackButton.setFont(font2)
        self.BackButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.NegateButton = QPushButton(self.standard)
        self.NegateButton.setObjectName(u"NegateButton")
        self.NegateButton.setGeometry(QRect(0, 561, 111, 70))
        self.NegateButton.setFont(font2)
        self.NegateButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.AddButton = QPushButton(self.standard)
        self.AddButton.setObjectName(u"AddButton")
        self.AddButton.setGeometry(QRect(330, 492, 111, 70))
        self.AddButton.setFont(font2)
        self.AddButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.FourButton = QPushButton(self.standard)
        self.FourButton.setObjectName(u"FourButton")
        self.FourButton.setGeometry(QRect(0, 423, 111, 70))
        self.FourButton.setFont(font2)
        self.FourButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.MinusButton = QPushButton(self.standard)
        self.MinusButton.setObjectName(u"MinusButton")
        self.MinusButton.setGeometry(QRect(330, 423, 111, 70))
        font3 = QFont()
        font3.setPointSize(26)
        self.MinusButton.setFont(font3)
        self.MinusButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.PercentButton = QPushButton(self.standard)
        self.PercentButton.setObjectName(u"PercentButton")
        self.PercentButton.setGeometry(QRect(0, 216, 111, 70))
        self.PercentButton.setFont(font2)
        self.PercentButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.NineButton = QPushButton(self.standard)
        self.NineButton.setObjectName(u"NineButton")
        self.NineButton.setGeometry(QRect(220, 354, 111, 70))
        self.NineButton.setFont(font2)
        self.NineButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.EqualToButton = QPushButton(self.standard)
        self.EqualToButton.setObjectName(u"EqualToButton")
        self.EqualToButton.setGeometry(QRect(330, 561, 111, 70))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.EqualToButton.setFont(font4)
        self.EqualToButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(3, 111, 196);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(3, 124, 217);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(4, 139, 243);\n"
"\n"
"}")
        self.DotButton = QPushButton(self.standard)
        self.DotButton.setObjectName(u"DotButton")
        self.DotButton.setGeometry(QRect(220, 561, 111, 70))
        self.DotButton.setFont(font2)
        self.DotButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.SixButton = QPushButton(self.standard)
        self.SixButton.setObjectName(u"SixButton")
        self.SixButton.setGeometry(QRect(220, 423, 111, 70))
        self.SixButton.setFont(font2)
        self.SixButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.DivideButton = QPushButton(self.standard)
        self.DivideButton.setObjectName(u"DivideButton")
        self.DivideButton.setGeometry(QRect(330, 285, 111, 70))
        font5 = QFont()
        font5.setPointSize(18)
        self.DivideButton.setFont(font5)
        self.DivideButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.SqRootButton = QPushButton(self.standard)
        self.SqRootButton.setObjectName(u"SqRootButton")
        self.SqRootButton.setGeometry(QRect(220, 285, 111, 70))
        self.SqRootButton.setFont(font2)
        self.SqRootButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.FiveButton = QPushButton(self.standard)
        self.FiveButton.setObjectName(u"FiveButton")
        self.FiveButton.setGeometry(QRect(110, 423, 111, 70))
        self.FiveButton.setFont(font2)
        self.FiveButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.CrootButton = QPushButton(self.standard)
        self.CrootButton.setObjectName(u"CrootButton")
        self.CrootButton.setGeometry(QRect(110, 216, 111, 70))
        self.CrootButton.setFont(font2)
        self.CrootButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.SqButton = QPushButton(self.standard)
        self.SqButton.setObjectName(u"SqButton")
        self.SqButton.setGeometry(QRect(110, 285, 111, 70))
        self.SqButton.setFont(font2)
        self.SqButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.CButton = QPushButton(self.standard)
        self.CButton.setObjectName(u"CButton")
        self.CButton.setGeometry(QRect(220, 216, 111, 70))
        self.CButton.setFont(font4)
        self.CButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.DivideByOneButton = QPushButton(self.standard)
        self.DivideByOneButton.setObjectName(u"DivideByOneButton")
        self.DivideByOneButton.setGeometry(QRect(0, 285, 111, 70))
        self.DivideByOneButton.setFont(font2)
        self.DivideByOneButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 2px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.page_label = QLabel(self.standard)
        self.page_label.setObjectName(u"page_label")
        self.page_label.setGeometry(QRect(40, -12, 101, 51))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI Semibold"])
        font6.setPointSize(16)
        font6.setBold(True)
        self.page_label.setFont(font6)
        self.page_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.page_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.outputlabel_scrl = QScrollArea(self.standard)
        self.outputlabel_scrl.setObjectName(u"outputlabel_scrl")
        self.outputlabel_scrl.setGeometry(QRect(0, 50, 441, 111))
        self.outputlabel_scrl.setFocusPolicy(Qt.StrongFocus)
        self.outputlabel_scrl.setFrameShape(QFrame.NoFrame)
        self.outputlabel_scrl.setFrameShadow(QFrame.Plain)
        self.outputlabel_scrl.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.outputlabel_scrl.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 441, 111))
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.OutputLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.OutputLabel.setObjectName(u"OutputLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.OutputLabel.sizePolicy().hasHeightForWidth())
        self.OutputLabel.setSizePolicy(sizePolicy1)
        font7 = QFont()
        font7.setFamilies([u"Segoe UI Semibold"])
        font7.setPointSize(36)
        font7.setBold(True)
        self.OutputLabel.setFont(font7)
        self.OutputLabel.setCursor(QCursor(Qt.IBeamCursor))
        self.OutputLabel.setFocusPolicy(Qt.NoFocus)
        self.OutputLabel.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.OutputLabel.setAcceptDrops(False)
        self.OutputLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.OutputLabel.setFrameShape(QFrame.NoFrame)
        self.OutputLabel.setFrameShadow(QFrame.Plain)
        self.OutputLabel.setLineWidth(1)
        self.OutputLabel.setMidLineWidth(0)
        self.OutputLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.OutputLabel.setWordWrap(False)
        self.OutputLabel.setMargin(10)
        self.OutputLabel.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_3.addWidget(self.OutputLabel)

        self.outputlabel_scrl.setWidget(self.scrollAreaWidgetContents_2)
        self.ques_label = QLabel(self.standard)
        self.ques_label.setObjectName(u"ques_label")
        self.ques_label.setGeometry(QRect(0, 50, 441, 31))
        font8 = QFont()
        font8.setPointSize(12)
        self.ques_label.setFont(font8)
        self.ques_label.setStyleSheet(u"color: rgb(184, 184, 184);\n"
"padding-right: 4px")
        self.ques_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ques_label.setMargin(9)
        self.stackedWidget.addWidget(self.standard)
        self.scientific = QWidget()
        self.scientific.setObjectName(u"scientific")
        self.sqr_button_2 = QPushButton(self.scientific)
        self.sqr_button_2.setObjectName(u"sqr_button_2")
        self.sqr_button_2.setGeometry(QRect(1, 260, 85, 50))
        self.sqr_button_2.setFont(font8)
        self.sqr_button_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.back_button_2 = QPushButton(self.scientific)
        self.back_button_2.setObjectName(u"back_button_2")
        self.back_button_2.setGeometry(QRect(353, 260, 85, 50))
        self.back_button_2.setFont(font2)
        self.back_button_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.clear_button_2 = QPushButton(self.scientific)
        self.clear_button_2.setObjectName(u"clear_button_2")
        self.clear_button_2.setGeometry(QRect(265, 260, 85, 50))
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(True)
        self.clear_button_2.setFont(font9)
        self.clear_button_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.e_button = QPushButton(self.scientific)
        self.e_button.setObjectName(u"e_button")
        self.e_button.setGeometry(QRect(177, 260, 85, 50))
        self.e_button.setFont(font2)
        self.e_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.pi_button = QPushButton(self.scientific)
        self.pi_button.setObjectName(u"pi_button")
        self.pi_button.setGeometry(QRect(89, 260, 85, 50))
        self.pi_button.setFont(font2)
        self.pi_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.exp_button = QPushButton(self.scientific)
        self.exp_button.setObjectName(u"exp_button")
        self.exp_button.setGeometry(QRect(265, 313, 85, 50))
        self.exp_button.setFont(font8)
        self.exp_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.mod_button_2 = QPushButton(self.scientific)
        self.mod_button_2.setObjectName(u"mod_button_2")
        self.mod_button_2.setGeometry(QRect(353, 313, 85, 50))
        self.mod_button_2.setFont(font8)
        self.mod_button_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.mod_button = QPushButton(self.scientific)
        self.mod_button.setObjectName(u"mod_button")
        self.mod_button.setGeometry(QRect(177, 313, 85, 50))
        self.mod_button.setFont(font8)
        self.mod_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.inverse_button_2 = QPushButton(self.scientific)
        self.inverse_button_2.setObjectName(u"inverse_button_2")
        self.inverse_button_2.setGeometry(QRect(89, 313, 85, 50))
        self.inverse_button_2.setFont(font2)
        self.inverse_button_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.croot_button_2 = QPushButton(self.scientific)
        self.croot_button_2.setObjectName(u"croot_button_2")
        self.croot_button_2.setGeometry(QRect(1, 313, 85, 50))
        self.croot_button_2.setFont(font8)
        self.croot_button_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.divide_button_2 = QPushButton(self.scientific)
        self.divide_button_2.setObjectName(u"divide_button_2")
        self.divide_button_2.setGeometry(QRect(353, 366, 85, 50))
        self.divide_button_2.setFont(font2)
        self.divide_button_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.close_bracket_button = QPushButton(self.scientific)
        self.close_bracket_button.setObjectName(u"close_bracket_button")
        self.close_bracket_button.setGeometry(QRect(177, 366, 85, 50))
        self.close_bracket_button.setFont(font2)
        self.close_bracket_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.fact_button = QPushButton(self.scientific)
        self.fact_button.setObjectName(u"fact_button")
        self.fact_button.setGeometry(QRect(265, 366, 85, 50))
        self.fact_button.setFont(font8)
        self.fact_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.sqrt_button_2 = QPushButton(self.scientific)
        self.sqrt_button_2.setObjectName(u"sqrt_button_2")
        self.sqrt_button_2.setGeometry(QRect(1, 366, 85, 50))
        self.sqrt_button_2.setFont(font8)
        self.sqrt_button_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.open_bracket_button = QPushButton(self.scientific)
        self.open_bracket_button.setObjectName(u"open_bracket_button")
        self.open_bracket_button.setGeometry(QRect(89, 366, 85, 50))
        self.open_bracket_button.setFont(font2)
        self.open_bracket_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.NineButton_4 = QPushButton(self.scientific)
        self.NineButton_4.setObjectName(u"NineButton_4")
        self.NineButton_4.setGeometry(QRect(265, 419, 85, 50))
        self.NineButton_4.setFont(font2)
        self.NineButton_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.TwoButton_4 = QPushButton(self.scientific)
        self.TwoButton_4.setObjectName(u"TwoButton_4")
        self.TwoButton_4.setGeometry(QRect(177, 525, 85, 50))
        self.TwoButton_4.setFont(font2)
        self.TwoButton_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.NegateButton_4 = QPushButton(self.scientific)
        self.NegateButton_4.setObjectName(u"NegateButton_4")
        self.NegateButton_4.setGeometry(QRect(89, 578, 85, 50))
        self.NegateButton_4.setFont(font2)
        self.NegateButton_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.SixButton_4 = QPushButton(self.scientific)
        self.SixButton_4.setObjectName(u"SixButton_4")
        self.SixButton_4.setGeometry(QRect(265, 472, 85, 50))
        self.SixButton_4.setFont(font2)
        self.SixButton_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.DotButton_4 = QPushButton(self.scientific)
        self.DotButton_4.setObjectName(u"DotButton_4")
        self.DotButton_4.setGeometry(QRect(265, 578, 85, 50))
        self.DotButton_4.setFont(font2)
        self.DotButton_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.EightButton_4 = QPushButton(self.scientific)
        self.EightButton_4.setObjectName(u"EightButton_4")
        self.EightButton_4.setGeometry(QRect(177, 419, 85, 50))
        self.EightButton_4.setFont(font2)
        self.EightButton_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.SevenButton_4 = QPushButton(self.scientific)
        self.SevenButton_4.setObjectName(u"SevenButton_4")
        self.SevenButton_4.setGeometry(QRect(89, 419, 85, 50))
        self.SevenButton_4.setFont(font2)
        self.SevenButton_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.FiveButton_4 = QPushButton(self.scientific)
        self.FiveButton_4.setObjectName(u"FiveButton_4")
        self.FiveButton_4.setGeometry(QRect(177, 472, 85, 50))
        self.FiveButton_4.setFont(font2)
        self.FiveButton_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.FourButton_4 = QPushButton(self.scientific)
        self.FourButton_4.setObjectName(u"FourButton_4")
        self.FourButton_4.setGeometry(QRect(89, 472, 85, 50))
        self.FourButton_4.setFont(font2)
        self.FourButton_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.OneButton_4 = QPushButton(self.scientific)
        self.OneButton_4.setObjectName(u"OneButton_4")
        self.OneButton_4.setGeometry(QRect(89, 525, 85, 50))
        self.OneButton_4.setFont(font2)
        self.OneButton_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.ZeroButton_4 = QPushButton(self.scientific)
        self.ZeroButton_4.setObjectName(u"ZeroButton_4")
        self.ZeroButton_4.setGeometry(QRect(177, 578, 85, 50))
        self.ZeroButton_4.setFont(font2)
        self.ZeroButton_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.ThreeButton_4 = QPushButton(self.scientific)
        self.ThreeButton_4.setObjectName(u"ThreeButton_4")
        self.ThreeButton_4.setGeometry(QRect(265, 525, 85, 50))
        self.ThreeButton_4.setFont(font2)
        self.ThreeButton_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.sub_button_2 = QPushButton(self.scientific)
        self.sub_button_2.setObjectName(u"sub_button_2")
        self.sub_button_2.setGeometry(QRect(353, 472, 85, 50))
        self.sub_button_2.setFont(font3)
        self.sub_button_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.multiply_button_2 = QPushButton(self.scientific)
        self.multiply_button_2.setObjectName(u"multiply_button_2")
        self.multiply_button_2.setGeometry(QRect(353, 419, 85, 50))
        self.multiply_button_2.setFont(font2)
        self.multiply_button_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.add_button_2 = QPushButton(self.scientific)
        self.add_button_2.setObjectName(u"add_button_2")
        self.add_button_2.setGeometry(QRect(353, 525, 85, 50))
        self.add_button_2.setFont(font2)
        self.add_button_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.equal_button_2 = QPushButton(self.scientific)
        self.equal_button_2.setObjectName(u"equal_button_2")
        self.equal_button_2.setGeometry(QRect(353, 578, 85, 50))
        self.equal_button_2.setFont(font2)
        self.equal_button_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(3, 111, 196);\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(3, 124, 217);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(4, 139, 243);\n"
"}")
        self.log_button = QPushButton(self.scientific)
        self.log_button.setObjectName(u"log_button")
        self.log_button.setGeometry(QRect(1, 525, 85, 50))
        self.log_button.setFont(font8)
        self.log_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.ln_button = QPushButton(self.scientific)
        self.ln_button.setObjectName(u"ln_button")
        self.ln_button.setGeometry(QRect(1, 578, 85, 50))
        self.ln_button.setFont(font8)
        self.ln_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.power_of_ten = QPushButton(self.scientific)
        self.power_of_ten.setObjectName(u"power_of_ten")
        self.power_of_ten.setGeometry(QRect(1, 472, 85, 50))
        self.power_of_ten.setFont(font8)
        self.power_of_ten.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.power_button = QPushButton(self.scientific)
        self.power_button.setObjectName(u"power_button")
        self.power_button.setGeometry(QRect(1, 419, 85, 50))
        self.power_button.setFont(font8)
        self.power_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.page_label_2 = QLabel(self.scientific)
        self.page_label_2.setObjectName(u"page_label_2")
        self.page_label_2.setGeometry(QRect(40, -12, 91, 51))
        self.page_label_2.setFont(font6)
        self.page_label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.page_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.outputlabel_scrl_2 = QScrollArea(self.scientific)
        self.outputlabel_scrl_2.setObjectName(u"outputlabel_scrl_2")
        self.outputlabel_scrl_2.setGeometry(QRect(0, 50, 441, 111))
        self.outputlabel_scrl_2.setFrameShape(QFrame.NoFrame)
        self.outputlabel_scrl_2.setFrameShadow(QFrame.Plain)
        self.outputlabel_scrl_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.outputlabel_scrl_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 441, 111))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.OutputLabel_2 = QLabel(self.scrollAreaWidgetContents_3)
        self.OutputLabel_2.setObjectName(u"OutputLabel_2")
        sizePolicy1.setHeightForWidth(self.OutputLabel_2.sizePolicy().hasHeightForWidth())
        self.OutputLabel_2.setSizePolicy(sizePolicy1)
        self.OutputLabel_2.setFont(font7)
        self.OutputLabel_2.setCursor(QCursor(Qt.IBeamCursor))
        self.OutputLabel_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.OutputLabel_2.setFrameShape(QFrame.NoFrame)
        self.OutputLabel_2.setFrameShadow(QFrame.Plain)
        self.OutputLabel_2.setLineWidth(1)
        self.OutputLabel_2.setMidLineWidth(0)
        self.OutputLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.OutputLabel_2.setWordWrap(False)
        self.OutputLabel_2.setMargin(10)
        self.OutputLabel_2.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_4.addWidget(self.OutputLabel_2)

        self.outputlabel_scrl_2.setWidget(self.scrollAreaWidgetContents_3)
        self.ques_label2 = QLabel(self.scientific)
        self.ques_label2.setObjectName(u"ques_label2")
        self.ques_label2.setGeometry(QRect(0, 50, 441, 31))
        self.ques_label2.setFont(font8)
        self.ques_label2.setStyleSheet(u"color: rgb(184, 184, 184);\n"
"padding-right: 4px")
        self.ques_label2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ques_label2.setMargin(9)
        self.stackedWidget.addWidget(self.scientific)
        self.currency = QWidget()
        self.currency.setObjectName(u"currency")
        self.page_label_3 = QLabel(self.currency)
        self.page_label_3.setObjectName(u"page_label_3")
        self.page_label_3.setGeometry(QRect(40, -12, 91, 51))
        self.page_label_3.setFont(font6)
        self.page_label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.page_label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.OutputLabel_4 = QLabel(self.currency)
        self.OutputLabel_4.setObjectName(u"OutputLabel_4")
        self.OutputLabel_4.setGeometry(QRect(40, 39, 431, 71))
        font10 = QFont()
        font10.setFamilies([u"Segoe UI Semibold"])
        font10.setPointSize(28)
        font10.setBold(True)
        self.OutputLabel_4.setFont(font10)
        self.OutputLabel_4.setCursor(QCursor(Qt.IBeamCursor))
        self.OutputLabel_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.OutputLabel_4.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.SixButton_3 = QPushButton(self.currency)
        self.SixButton_3.setObjectName(u"SixButton_3")
        self.SixButton_3.setGeometry(QRect(296, 430, 145, 65))
        self.SixButton_3.setFont(font2)
        self.SixButton_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	border-right: 3px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.ZeroButton_3 = QPushButton(self.currency)
        self.ZeroButton_3.setObjectName(u"ZeroButton_3")
        self.ZeroButton_3.setGeometry(QRect(148, 566, 145, 65))
        self.ZeroButton_3.setFont(font2)
        self.ZeroButton_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	border-bottom: 3px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.ThreeButton_3 = QPushButton(self.currency)
        self.ThreeButton_3.setObjectName(u"ThreeButton_3")
        self.ThreeButton_3.setGeometry(QRect(296, 498, 145, 65))
        self.ThreeButton_3.setFont(font2)
        self.ThreeButton_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	border-right: 3px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.EightButton_3 = QPushButton(self.currency)
        self.EightButton_3.setObjectName(u"EightButton_3")
        self.EightButton_3.setGeometry(QRect(148, 362, 145, 65))
        self.EightButton_3.setFont(font2)
        self.EightButton_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.FourButton_3 = QPushButton(self.currency)
        self.FourButton_3.setObjectName(u"FourButton_3")
        self.FourButton_3.setGeometry(QRect(0, 430, 145, 65))
        self.FourButton_3.setFont(font2)
        self.FourButton_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.NineButton_3 = QPushButton(self.currency)
        self.NineButton_3.setObjectName(u"NineButton_3")
        self.NineButton_3.setGeometry(QRect(296, 362, 145, 65))
        self.NineButton_3.setFont(font2)
        self.NineButton_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	border-right: 3px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.TwoButton_3 = QPushButton(self.currency)
        self.TwoButton_3.setObjectName(u"TwoButton_3")
        self.TwoButton_3.setGeometry(QRect(148, 498, 145, 65))
        self.TwoButton_3.setFont(font2)
        self.TwoButton_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.SevenButton_3 = QPushButton(self.currency)
        self.SevenButton_3.setObjectName(u"SevenButton_3")
        self.SevenButton_3.setGeometry(QRect(0, 362, 145, 65))
        self.SevenButton_3.setFont(font2)
        self.SevenButton_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.DotButton_3 = QPushButton(self.currency)
        self.DotButton_3.setObjectName(u"DotButton_3")
        self.DotButton_3.setGeometry(QRect(296, 566, 145, 65))
        self.DotButton_3.setFont(font2)
        self.DotButton_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	border-right: 3px solid rgb(44, 44, 44);\n"
"	border-bottom: 3px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.FiveButton_3 = QPushButton(self.currency)
        self.FiveButton_3.setObjectName(u"FiveButton_3")
        self.FiveButton_3.setGeometry(QRect(148, 430, 145, 65))
        self.FiveButton_3.setFont(font2)
        self.FiveButton_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.OneButton_3 = QPushButton(self.currency)
        self.OneButton_3.setObjectName(u"OneButton_3")
        self.OneButton_3.setGeometry(QRect(0, 498, 145, 65))
        self.OneButton_3.setFont(font2)
        self.OneButton_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.BackButton_3 = QPushButton(self.currency)
        self.BackButton_3.setObjectName(u"BackButton_3")
        self.BackButton_3.setGeometry(QRect(296, 294, 145, 65))
        self.BackButton_3.setFont(font2)
        self.BackButton_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"	border-right: 3px solid rgb(44, 44, 44)\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.CButton_3 = QPushButton(self.currency)
        self.CButton_3.setObjectName(u"CButton_3")
        self.CButton_3.setGeometry(QRect(148, 294, 145, 65))
        self.CButton_3.setFont(font4)
        self.CButton_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        self.currency_label2 = QLabel(self.currency)
        self.currency_label2.setObjectName(u"currency_label2")
        self.currency_label2.setGeometry(QRect(0, 125, 31, 81))
        font11 = QFont()
        font11.setPointSize(24)
        self.currency_label2.setFont(font11)
        self.currency_label2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.currency_label2.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.OutputLabel_3 = QLabel(self.currency)
        self.OutputLabel_3.setObjectName(u"OutputLabel_3")
        self.OutputLabel_3.setGeometry(QRect(40, 130, 431, 71))
        self.OutputLabel_3.setFont(font10)
        self.OutputLabel_3.setCursor(QCursor(Qt.IBeamCursor))
        self.OutputLabel_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.OutputLabel_3.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.currency_label = QLabel(self.currency)
        self.currency_label.setObjectName(u"currency_label")
        self.currency_label.setGeometry(QRect(0, 29, 31, 91))
        self.currency_label.setFont(font11)
        self.currency_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.currency_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.comboBox = QComboBox(self.currency)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(0, 109, 161, 31))
        self.comboBox.setStyleSheet(u"")
        self.comboBox_2 = QComboBox(self.currency)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(0, 194, 161, 31))
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setStyleSheet(u"")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setIconSize(QSize(10, 10))
        self.update_btn = QPushButton(self.currency)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setGeometry(QRect(10, 225, 91, 24))
        font12 = QFont()
        font12.setBold(True)
        font12.setUnderline(True)
        self.update_btn.setFont(font12)
        self.update_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	text-decoration: underline;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(148, 148, 148);\n"
"}")
        self.update_lbl = QLabel(self.currency)
        self.update_lbl.setObjectName(u"update_lbl")
        self.update_lbl.setGeometry(QRect(10, 245, 421, 41))
        font13 = QFont()
        font13.setFamilies([u"Segoe UI Semibold"])
        font13.setPointSize(9)
        font13.setBold(True)
        self.update_lbl.setFont(font13)
        self.update_lbl.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.currency)
        self.SixButton_3.raise_()
        self.ZeroButton_3.raise_()
        self.ThreeButton_3.raise_()
        self.EightButton_3.raise_()
        self.FourButton_3.raise_()
        self.NineButton_3.raise_()
        self.TwoButton_3.raise_()
        self.SevenButton_3.raise_()
        self.DotButton_3.raise_()
        self.FiveButton_3.raise_()
        self.OneButton_3.raise_()
        self.BackButton_3.raise_()
        self.currency_label2.raise_()
        self.OutputLabel_3.raise_()
        self.currency_label.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.page_label_3.raise_()
        self.OutputLabel_4.raise_()
        self.CButton_3.raise_()
        self.update_btn.raise_()
        self.update_lbl.raise_()
        self.side_bar = QFrame(self.centralwidget)
        self.side_bar.setObjectName(u"side_bar")
        self.side_bar.setGeometry(QRect(0, 0, 0, 671))
        sizePolicy1.setHeightForWidth(self.side_bar.sizePolicy().hasHeightForWidth())
        self.side_bar.setSizePolicy(sizePolicy1)
        self.side_bar.setMinimumSize(QSize(0, 0))
        self.side_bar.setMaximumSize(QSize(151, 16777215))
        self.side_bar.setFont(font)
        self.side_bar.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.side_bar.setFrameShape(QFrame.StyledPanel)
        self.side_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.side_bar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_cont = QFrame(self.side_bar)
        self.side_cont.setObjectName(u"side_cont")
        self.side_cont.setMinimumSize(QSize(0, 81))
        self.side_cont.setMaximumSize(QSize(16777215, 81))
        self.side_cont.setStyleSheet(u"border: none;")
        self.side_cont.setFrameShape(QFrame.StyledPanel)
        self.side_cont.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.side_cont)

        self.frame_3 = QFrame(self.side_bar)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border: none;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 106, 584))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setFont(font13)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;")

        self.verticalLayout_3.addWidget(self.label_3)

        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.standard_btn = QPushButton(self.frame)
        self.standard_btn.setObjectName(u"standard_btn")
        self.standard_btn.setMinimumSize(QSize(0, 50))
        font14 = QFont()
        font14.setFamilies([u"Segoe UI Semibold"])
        font14.setBold(True)
        self.standard_btn.setFont(font14)
        self.standard_btn.setLayoutDirection(Qt.LeftToRight)
        self.standard_btn.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u"resources/standard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.standard_btn.setIcon(icon1)
        self.standard_btn.setIconSize(QSize(38, 38))

        self.verticalLayout_4.addWidget(self.standard_btn)

        self.Scientific_btn = QPushButton(self.frame)
        self.Scientific_btn.setObjectName(u"Scientific_btn")
        self.Scientific_btn.setMinimumSize(QSize(0, 50))
        self.Scientific_btn.setFont(font14)
        self.Scientific_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	text-align:left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"resources/sci.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Scientific_btn.setIcon(icon2)
        self.Scientific_btn.setIconSize(QSize(22, 22))

        self.verticalLayout_4.addWidget(self.Scientific_btn)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setFont(font13)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;")

        self.verticalLayout_4.addWidget(self.label)

        self.Currency_btn = QPushButton(self.frame)
        self.Currency_btn.setObjectName(u"Currency_btn")
        self.Currency_btn.setMinimumSize(QSize(0, 50))
        self.Currency_btn.setFont(font14)
        self.Currency_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	text-align:left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"resources/Currency.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.Currency_btn.setIcon(icon3)
        self.Currency_btn.setIconSize(QSize(22, 22))

        self.verticalLayout_4.addWidget(self.Currency_btn)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 51))
        self.frame_4.setStyleSheet(u"border:none;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.about_btn = QPushButton(self.frame_4)
        self.about_btn.setObjectName(u"about_btn")
        self.about_btn.setMinimumSize(QSize(0, 50))
        self.about_btn.setFont(font14)
        self.about_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	text-align:left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"resources/About.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.about_btn.setIcon(icon4)
        self.about_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.about_btn)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.frame_3)

        self.menu_btn = QPushButton(self.centralwidget)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setGeometry(QRect(0, 33, 41, 41))
        self.menu_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid rgb(44, 44, 44);\n"
"	padding-top: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"resources/icon_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon5)
        self.menu_btn.setIconSize(QSize(18, 18))
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(0, 0, 441, 33))
        self.header.setStyleSheet(u"")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.header)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 101, 30))
        self.label_4.setFont(font14)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.minimize = QPushButton(self.header)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setGeometry(QRect(352, 0, 45, 33))
        font15 = QFont()
        font15.setPointSize(22)
        self.minimize.setFont(font15)
        self.minimize.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: none;\n"
"	padding-top: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(93, 93, 93);\n"
"}r")
        icon6 = QIcon()
        icon6.addFile(u"resources/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize.setIcon(icon6)
        self.minimize.setIconSize(QSize(22, 22))
        self.Exit = QPushButton(self.header)
        self.Exit.setObjectName(u"Exit")
        self.Exit.setGeometry(QRect(397, 0, 45, 33))
        self.Exit.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: none;\n"
"	padding-top: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(216, 0, 0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"resources/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Exit.setIcon(icon7)
        self.Exit.setIconSize(QSize(22, 22))
        self.about = QFrame(self.centralwidget)
        self.about.setObjectName(u"about")
        self.about.setGeometry(QRect(0, 439, 431, 0))
        self.about.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 1px solid rgb(0, 0, 0)\n"
"}\n"
"#about .QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}\n"
"")
        self.about.setFrameShape(QFrame.StyledPanel)
        self.about.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.about)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 10, 111, 61))
        font16 = QFont()
        font16.setPointSize(16)
        font16.setBold(True)
        self.label_5.setFont(font16)
        self.label_5.setStyleSheet(u"")
        self.label_6 = QLabel(self.about)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 60, 401, 51))
        font17 = QFont()
        font17.setPointSize(11)
        self.label_6.setFont(font17)
        self.Licence = QLabel(self.about)
        self.Licence.setObjectName(u"Licence")
        self.Licence.setGeometry(QRect(20, 130, 191, 31))
        self.Licence.setTextFormat(Qt.RichText)
        self.Licence.setOpenExternalLinks(True)
        self.label_5.raise_()
        self.Licence.raise_()
        self.label_6.raise_()
        self.history_btn = QPushButton(self.centralwidget)
        self.history_btn.setObjectName(u"history_btn")
        self.history_btn.setGeometry(QRect(400, 33, 41, 41))
        self.history_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 1px solid rgb(44, 44, 44);\n"
"	padding-top: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"resources/history_32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.history_btn.setIcon(icon8)
        self.history_btn.setIconSize(QSize(22, 22))
        self.history_scrl = QScrollArea(self.centralwidget)
        self.history_scrl.setObjectName(u"history_scrl")
        self.history_scrl.setGeometry(QRect(0, 250, 441, 0))
        self.history_scrl.setStyleSheet(u"background-color: rgb(29, 29, 29);")
        self.history_scrl.setFrameShape(QFrame.NoFrame)
        self.history_scrl.setFrameShadow(QFrame.Plain)
        self.history_scrl.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 437, 32))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.history_lbl = QLabel(self.scrollAreaWidgetContents)
        self.history_lbl.setObjectName(u"history_lbl")
        self.history_lbl.setFont(font4)
        self.history_lbl.setCursor(QCursor(Qt.IBeamCursor))
        self.history_lbl.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-right: 10px\n"
"")
        self.history_lbl.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.history_lbl.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.history_lbl)

        self.history_scrl.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.stackedWidget.raise_()
        self.history_btn.raise_()
        self.history_scrl.raise_()
        self.side_bar.raise_()
        self.header.raise_()
        self.menu_btn.raise_()
        self.about.raise_()
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.CButton.setDefault(False)
        self.comboBox.setCurrentIndex(1)
        self.comboBox_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator ", None))
        self.actionNornal.setText(QCoreApplication.translate("MainWindow", u"Nornal", None))
        self.actionScientific.setText(QCoreApplication.translate("MainWindow", u"Scientific", None))
        self.stackedWidget.setStyleSheet(QCoreApplication.translate("MainWindow", u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(147, 147, 147);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 131, 131);\n"
"}", None))
        self.TwoButton.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.TwoButton.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.EightButton.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.EightButton.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.ThreeButton.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.ThreeButton.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.SevenButton.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.SevenButton.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.MultiplyButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
#if QT_CONFIG(shortcut)
        self.MultiplyButton.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.ZeroButton.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.ZeroButton.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.OneButton.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.OneButton.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.BackButton.setText(QCoreApplication.translate("MainWindow", u"<<", None))
#if QT_CONFIG(shortcut)
        self.BackButton.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.NegateButton.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.AddButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.AddButton.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.FourButton.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.FourButton.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.MinusButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.MinusButton.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.PercentButton.setText(QCoreApplication.translate("MainWindow", u"%", None))
#if QT_CONFIG(shortcut)
        self.PercentButton.setShortcut(QCoreApplication.translate("MainWindow", u"%", None))
#endif // QT_CONFIG(shortcut)
        self.NineButton.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.NineButton.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.EqualToButton.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.EqualToButton.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.DotButton.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.DotButton.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.SixButton.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.SixButton.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.DivideButton.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
#if QT_CONFIG(shortcut)
        self.DivideButton.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.SqRootButton.setText(QCoreApplication.translate("MainWindow", u"\u221aX", None))
        self.FiveButton.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.FiveButton.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.CrootButton.setText(QCoreApplication.translate("MainWindow", u"3\u221a", None))
        self.SqButton.setText(QCoreApplication.translate("MainWindow", u"X\u00b2", None))
        self.CButton.setText(QCoreApplication.translate("MainWindow", u"C", None))
#if QT_CONFIG(shortcut)
        self.CButton.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.DivideByOneButton.setText(QCoreApplication.translate("MainWindow", u"\u215fx", None))
        self.page_label.setText(QCoreApplication.translate("MainWindow", u"Standard", None))
        self.OutputLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ques_label.setText("")
        self.sqr_button_2.setText(QCoreApplication.translate("MainWindow", u"X\u00b2", None))
        self.back_button_2.setText(QCoreApplication.translate("MainWindow", u"<<", None))
#if QT_CONFIG(shortcut)
        self.back_button_2.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.clear_button_2.setText(QCoreApplication.translate("MainWindow", u"C", None))
#if QT_CONFIG(shortcut)
        self.clear_button_2.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.e_button.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.pi_button.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
        self.exp_button.setText(QCoreApplication.translate("MainWindow", u"exp", None))
        self.mod_button_2.setText(QCoreApplication.translate("MainWindow", u"mod", None))
        self.mod_button.setText(QCoreApplication.translate("MainWindow", u"|x|", None))
        self.inverse_button_2.setText(QCoreApplication.translate("MainWindow", u"\u215fx", None))
        self.croot_button_2.setText(QCoreApplication.translate("MainWindow", u"3\u221aX", None))
        self.divide_button_2.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.divide_button_2.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.close_bracket_button.setText(QCoreApplication.translate("MainWindow", u")", None))
#if QT_CONFIG(shortcut)
        self.close_bracket_button.setShortcut(QCoreApplication.translate("MainWindow", u")", None))
#endif // QT_CONFIG(shortcut)
        self.fact_button.setText(QCoreApplication.translate("MainWindow", u"n!", None))
#if QT_CONFIG(shortcut)
        self.fact_button.setShortcut(QCoreApplication.translate("MainWindow", u"!", None))
#endif // QT_CONFIG(shortcut)
        self.sqrt_button_2.setText(QCoreApplication.translate("MainWindow", u"\u221aX", None))
        self.open_bracket_button.setText(QCoreApplication.translate("MainWindow", u"(", None))
#if QT_CONFIG(shortcut)
        self.open_bracket_button.setShortcut(QCoreApplication.translate("MainWindow", u"(", None))
#endif // QT_CONFIG(shortcut)
        self.NineButton_4.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.NineButton_4.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.TwoButton_4.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.TwoButton_4.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.NegateButton_4.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.SixButton_4.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.SixButton_4.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.DotButton_4.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.DotButton_4.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.EightButton_4.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.EightButton_4.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.SevenButton_4.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.SevenButton_4.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.FiveButton_4.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.FiveButton_4.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.FourButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.FourButton_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.OneButton_4.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.OneButton_4.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.ZeroButton_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.ZeroButton_4.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.ThreeButton_4.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.ThreeButton_4.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.sub_button_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.sub_button_2.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.multiply_button_2.setText(QCoreApplication.translate("MainWindow", u"X", None))
#if QT_CONFIG(shortcut)
        self.multiply_button_2.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.add_button_2.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.add_button_2.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.equal_button_2.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.equal_button_2.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.log_button.setText(QCoreApplication.translate("MainWindow", u"log", None))
        self.ln_button.setText(QCoreApplication.translate("MainWindow", u"ln", None))
        self.power_of_ten.setText(QCoreApplication.translate("MainWindow", u"10^x", None))
        self.power_button.setText(QCoreApplication.translate("MainWindow", u"x^y", None))
#if QT_CONFIG(shortcut)
        self.power_button.setShortcut(QCoreApplication.translate("MainWindow", u"^", None))
#endif // QT_CONFIG(shortcut)
        self.page_label_2.setText(QCoreApplication.translate("MainWindow", u"Scientific", None))
        self.OutputLabel_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ques_label2.setText("")
        self.page_label_3.setText(QCoreApplication.translate("MainWindow", u"Currency", None))
        self.OutputLabel_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.SixButton_3.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.SixButton_3.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.ZeroButton_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.ZeroButton_3.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.ThreeButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.ThreeButton_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.EightButton_3.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.EightButton_3.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.FourButton_3.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.FourButton_3.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.NineButton_3.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.NineButton_3.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.TwoButton_3.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.TwoButton_3.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.SevenButton_3.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.SevenButton_3.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.DotButton_3.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.DotButton_3.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.FiveButton_3.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.FiveButton_3.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.OneButton_3.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.OneButton_3.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.BackButton_3.setText(QCoreApplication.translate("MainWindow", u"<<", None))
#if QT_CONFIG(shortcut)
        self.BackButton_3.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.CButton_3.setText(QCoreApplication.translate("MainWindow", u"C", None))
#if QT_CONFIG(shortcut)
        self.CButton_3.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.currency_label2.setText(QCoreApplication.translate("MainWindow", u" \u20b9", None))
        self.OutputLabel_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.currency_label.setText(QCoreApplication.translate("MainWindow", u" $", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"India - Rupee", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"United States - Dollar", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Europe - Euro", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"India - Rupee", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"United States - Dollar", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Europe - Euro", None))

        self.comboBox_2.setCurrentText(QCoreApplication.translate("MainWindow", u"India - Rupee", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"Update Rates", None))
        self.update_lbl.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Calculator", None))
#if QT_CONFIG(tooltip)
        self.standard_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.standard_btn.setText(QCoreApplication.translate("MainWindow", u"Standard", None))
#if QT_CONFIG(tooltip)
        self.Scientific_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Scientific_btn.setText(QCoreApplication.translate("MainWindow", u"Scientific", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Convertor", None))
#if QT_CONFIG(tooltip)
        self.Currency_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Currency_btn.setText(QCoreApplication.translate("MainWindow", u"Currency", None))
#if QT_CONFIG(tooltip)
        self.about_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.about_btn.setText(QCoreApplication.translate("MainWindow", u" About", None))
#if QT_CONFIG(tooltip)
        self.menu_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Navigation", None))
#endif // QT_CONFIG(tooltip)
        self.menu_btn.setText("")
#if QT_CONFIG(shortcut)
        self.menu_btn.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"   Calculator", None))
#if QT_CONFIG(tooltip)
        self.minimize.setToolTip(QCoreApplication.translate("MainWindow", u"minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize.setText("")
#if QT_CONFIG(tooltip)
        self.Exit.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.Exit.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Calculator 3.69.420\n"
"\u00a9 2021 Anubhav. All copyrights reserved under LGPL License.", None))
        self.Licence.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://doc.qt.io/qt-5/lgpl.html\"><span style=\" font-size:10pt; color:#0078d7; text-decoration:none;\">Qt Licence Terms</span></a></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.history_btn.setToolTip(QCoreApplication.translate("MainWindow", u"History", None))
#endif // QT_CONFIG(tooltip)
        self.history_btn.setText("")
        self.history_lbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>", None))
    # retranslateUi

