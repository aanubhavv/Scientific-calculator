import sys
from PySide6 import QtCore, QtGui
from ui_Calc import *
from functions.ui_func import *
import warnings

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.PercentButton.clicked.connect(lambda: UIFunc.percent(self))
        self.ui.DivideByOneButton.clicked.connect(lambda: UIFunc.inverse(self))
        self.ui.CrootButton.clicked.connect(lambda: UIFunc.Croot(self))
        self.ui.SqButton.clicked.connect(lambda: UIFunc.sqr(self))
        self.ui.SqRootButton.clicked.connect(lambda: UIFunc.sqrt(self))
        self.ui.BackButton.clicked.connect(lambda: UIFunc.back(self))
        self.ui.BackButton_3.clicked.connect(lambda: UIFunc.back(self))
        self.ui.EqualToButton.clicked.connect(lambda: UIFunc.equal(self))
        self.ui.NegateButton.clicked.connect(lambda: UIFunc.negate(self))
        self.ui.ZeroButton.clicked.connect(lambda: UIFunc.press_it(self, pressed = "0"))
        self.ui.OneButton.clicked.connect(lambda: UIFunc.press_it(self, pressed = "1"))
        self.ui.TwoButton.clicked.connect(lambda: UIFunc.press_it(self, pressed = "2"))
        self.ui.ThreeButton.clicked.connect(lambda: UIFunc.press_it(self, pressed = "3"))
        self.ui.FourButton.clicked.connect(lambda: UIFunc.press_it(self, pressed = "4"))
        self.ui.FiveButton.clicked.connect(lambda: UIFunc.press_it(self, pressed = "5"))
        self.ui.SixButton.clicked.connect(lambda: UIFunc.press_it(self, pressed = "6"))
        self.ui.SevenButton.clicked.connect(lambda: UIFunc.press_it(self, pressed = "7"))   
        self.ui.EightButton.clicked.connect(lambda: UIFunc.press_it(self, pressed = "8"))
        self.ui.NineButton.clicked.connect(lambda: UIFunc.press_it(self, pressed = "9"))
        self.ui.DivideButton.clicked.connect(lambda: UIFunc.press_it(self, pressed = "÷"))
        self.ui.MultiplyButton.clicked.connect(lambda: UIFunc.press_it(self, pressed = "x"))
        self.ui.ZeroButton_3.clicked.connect(lambda: UIFunc.press_it(self, pressed = "0"))
        self.ui.OneButton_3.clicked.connect(lambda: UIFunc.press_it(self, pressed = "1"))
        self.ui.TwoButton_3.clicked.connect(lambda: UIFunc.press_it(self, pressed = "2"))
        self.ui.ThreeButton_3.clicked.connect(lambda: UIFunc.press_it(self, pressed = "3"))
        self.ui.FourButton_3.clicked.connect(lambda: UIFunc.press_it(self, pressed = "4"))
        self.ui.FiveButton_3.clicked.connect(lambda: UIFunc.press_it(self, pressed = "5"))
        self.ui.SixButton_3.clicked.connect(lambda: UIFunc.press_it(self, pressed = "6"))
        self.ui.SevenButton_3.clicked.connect(lambda: UIFunc.press_it(self, pressed = "7"))
        self.ui.EightButton_3.clicked.connect(lambda: UIFunc.press_it(self, pressed = "8"))
        self.ui.NineButton_3.clicked.connect(lambda: UIFunc.press_it(self, pressed = "9"))
        self.ui.AddButton.clicked.connect(lambda: UIFunc.press_it(self, pressed = "+"))
        self.ui.MinusButton.clicked.connect(lambda: UIFunc.press_it(self, pressed = "-"))
        self.ui.DotButton.clicked.connect(lambda: UIFunc.press_it(self, pressed = "."))
        self.ui.CButton.clicked.connect(lambda: UIFunc.clear(self))
        self.ui.CButton_3.clicked.connect(lambda: UIFunc.clear(self))
        self.ui.clear_button_2.clicked.connect(lambda: UIFunc.clear(self))
        self.ui.ZeroButton_4.clicked.connect(lambda: UIFunc.press_it(self, pressed = "0"))
        self.ui.OneButton_4.clicked.connect(lambda: UIFunc.press_it(self, pressed = "1"))
        self.ui.TwoButton_4.clicked.connect(lambda: UIFunc.press_it(self, pressed = "2"))   
        self.ui.ThreeButton_4.clicked.connect(lambda: UIFunc.press_it(self, pressed = "3"))
        self.ui.FourButton_4.clicked.connect(lambda: UIFunc.press_it(self, pressed = "4"))
        self.ui.FiveButton_4.clicked.connect(lambda: UIFunc.press_it(self, pressed = "5"))
        self.ui.SixButton_4.clicked.connect(lambda: UIFunc.press_it(self, pressed = "6"))
        self.ui.SevenButton_4.clicked.connect(lambda: UIFunc.press_it(self, pressed = "7"))
        self.ui.EightButton_4.clicked.connect(lambda: UIFunc.press_it(self, pressed = "8"))
        self.ui.NineButton_4.clicked.connect(lambda: UIFunc.press_it(self, pressed = "9"))
        self.ui.add_button_2.clicked.connect(lambda: UIFunc.press_it(self, pressed = "+" ))
        self.ui.sub_button_2.clicked.connect(lambda: UIFunc.press_it(self, pressed = "-" ))
        self.ui.multiply_button_2.clicked.connect(lambda: UIFunc.press_it(self, pressed = "x" ))
        self.ui.divide_button_2.clicked.connect(lambda: UIFunc.press_it(self, pressed = "÷" ))
        self.ui.DotButton_4.clicked.connect(lambda: UIFunc.press_it(self, pressed = "." ))
        self.ui.DotButton_3.clicked.connect(lambda: UIFunc.press_it(self, pressed = "." ))
        self.ui.open_bracket_button.clicked.connect(lambda: UIFunc.press_it(self, pressed = "(" ))
        self.ui.close_bracket_button.clicked.connect(lambda: UIFunc.press_it(self, pressed = ")" ))
        self.ui.power_button.clicked.connect(lambda: UIFunc.press_it(self, pressed = "^" ))
        self.ui.NegateButton_4.clicked.connect(lambda: UIFunc.negate(self))
        self.ui.back_button_2.clicked.connect(lambda: UIFunc.back(self))
        self.ui.pi_button.clicked.connect(lambda: UIFunc.pi(self))
        self.ui.e_button.clicked.connect(lambda: UIFunc.euler(self))
        self.ui.sqr_button_2.clicked.connect(lambda: UIFunc.sqr(self))
        self.ui.equal_button_2.clicked.connect(lambda: UIFunc.equal(self))
        self.ui.croot_button_2.clicked.connect(lambda: UIFunc.Croot(self))
        self.ui.inverse_button_2.clicked.connect(lambda: UIFunc.inverse(self))
        self.ui.mod_button_2.clicked.connect(lambda: UIFunc.mod(self))
        self.ui.exp_button.clicked.connect(lambda: UIFunc.exp(self))
        self.ui.mod_button.clicked.connect(lambda: UIFunc.abs(self))
        self.ui.sqrt_button_2.clicked.connect(lambda: UIFunc.sqrt(self))
        self.ui.fact_button.clicked.connect(lambda: UIFunc.fact(self))
        self.ui.power_of_ten.clicked.connect(lambda: UIFunc.ten_power(self))
        self.ui.log_button.clicked.connect(lambda: UIFunc.log(self))
        self.ui.ln_button.clicked.connect(lambda: UIFunc.ln(self))
        self.ui.standard_btn.clicked.connect(lambda: pageFunc.stacked1(self))
        self.ui.Scientific_btn.clicked.connect(lambda: pageFunc.stacked2(self))
        self.ui.about_btn.clicked.connect(lambda: pageFunc.about(self))
        self.ui.Currency_btn.clicked.connect(lambda: pageFunc.stacked3(self))
        self.ui.menu_btn.clicked.connect(lambda: menufunc.togglemenu(self, True))
        self.ui.update_btn.clicked.connect(lambda: ratesFunc.update_rates(self))
        self.ui.history_btn.clicked.connect(lambda: UIFunc.history(self))
        self.ui.comboBox.activated.connect(lambda: UIFunc.change(self))
        self.ui.comboBox_2.activated.connect(lambda: UIFunc.change2(self))
        self.ui.Exit.clicked.connect(lambda: self.close())
        self.ui.minimize.clicked.connect(lambda: self.showMinimized())

        
        self.show()

        def moveWindow(e):
            if self.isMaximized() == False: 
                if e.buttons() == Qt.LeftButton:  
                    #Move window 
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        
        self.ui.header.mouseMoveEvent = moveWindow


    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def keyPressEvent(self, event):
        text = QApplication.clipboard().text()
        if event.matches(QtGui.QKeySequence.Paste):
            try:
                text2 = float(text)
                if self.ui.stackedWidget.currentIndex() == 0:
                    if self.ui.OutputLabel.text() == "0" or self.ui.OutputLabel.text() == "ERROR!":
                        self.ui.OutputLabel.setText("")
                    self.ui.OutputLabel.setText(f"{self.ui.OutputLabel.text()}{text}")
                elif self.ui.stackedWidget.currentIndex() == 1:
                    if self.ui.OutputLabel_2.text() == "0" or self.ui.OutputLabel_2.text() == "ERROR!":
                        self.ui.OutputLabel_2.setText("")
                    self.ui.OutputLabel_2.setText(f"{self.ui.OutputLabel_2.text()}{text}")
            except:
                pass

            
warnings.filterwarnings("ignore")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

