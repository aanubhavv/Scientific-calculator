from main import MainWindow
from ui_Calc import *
from functions.page_func import *
from functions.menu_func import *
from rates import *
#####################################################
import math
from random import choice
import csv
#####################################################

font = QFont()
font.setFamilies([u"Segoe UI Semibold"])
font.setPointSize(27)
font.setBold(True)

font2 = QFont()
font2.setFamilies([u"Segoe UI Semibold"])
font2.setPointSize(36)
font2.setBold(True)

operators = ["+", "-", "x", "÷", "^"]

class UIFunc(MainWindow):
    def Croot(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            try:
                eva = eval(self.ui.OutputLabel.text().replace("x", "*"))
                x = float(eva)
                sol = str(round(math.pow(x, 1/3), 14))
                split = sol.split(".")
                if split[1] == "0":
                    if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                        self.ui.history_lbl.setText("")
                    self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">3√{self.ui.OutputLabel.text()}=</span></p><p><span style=\" font-size:20pt;\">{split[0]}</span></p></body></html>")
                    self.ui.OutputLabel.setText(split[0])
                else:
                    if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                            self.ui.history_lbl.setText("")
                    self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">3√{self.ui.OutputLabel_2.text()}=</span></p><p><span style=\" font-size:20pt;\">{sol}</span></p></body></html>")
                    self.ui.OutputLabel.setText(sol)
            except:
                self.ui.OutputLabel.setText("ERROR!")
        else:
            try:
                eva = eval(self.ui.OutputLabel_2.text().replace("x", "*"))
                x = float(eva)
                sol = str(round(math.pow(x, 1/3), 11))
                split = sol.split(".")
                if split[1] == "0":
                    self.ui.OutputLabel_2.setText(split[0])
                else:
                    self.ui.OutputLabel_2.setText(sol)
            except:
                self.ui.OutputLabel_2.setText("ERROR!")

    def inverse(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            try:
                screen = self.ui.OutputLabel
                x = float(screen.text())
                sol = str(round(1 / x, 10))
                if "." in sol:
                    split = sol.split(".")
                    if split[-1] == "0":
                        if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                            self.ui.history_lbl.setText("")
                        self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">1/{self.ui.OutputLabel.text()}=</span></p><p><span style=\" font-size:20pt;\">{split[0]}</span></p></body></html>")
                        self.ui.OutputLabel.setText(str(split[0]))
                    else:
                        if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                            self.ui.history_lbl.setText("")
                        self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">1/{self.ui.OutputLabel.text()}=</span></p><p><span style=\" font-size:20pt;\">{sol}</span></p></body></html>")
                        self.ui.OutputLabel.setText(str(sol))
                else:
                    if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                        self.ui.history_lbl.setText("")
                    self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">1/{self.ui.OutputLabel.text()}=</span></p><p><span style=\" font-size:20pt;\">{sol}</span></p></body></html>")
                    self.ui.OutputLabel.setText(str(sol))
            except:
                self.ui.OutputLabel.setText("Undefined or ∞")
        else:
            try:
                screen = self.ui.OutputLabel_2
                x = float(screen.text())
                sol = str(round(1 / x, 10))
                if "." in sol:
                    split = sol.split(".")
                    if split[-1] == "0":
                        if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                            self.ui.history_lbl.setText("")
                        self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">1/{self.ui.OutputLabel_2.text()}=</span></p><p><span style=\" font-size:20pt;\">{split[0]}</span></p></body></html>")
                        self.ui.OutputLabel_2.setText(str(split[0]))
                    else:
                        if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                            self.ui.history_lbl.setText("")
                        self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">1/{self.ui.OutputLabel_2.text()}=</span></p><p><span style=\" font-size:20pt;\">{sol}</span></p></body></html>")
                        self.ui.OutputLabel_2.setText(str(sol))
                else:
                    if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                        self.ui.history_lbl.setText("")
                    self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">1/{self.ui.OutputLabel_2.text()}=</span></p><p><span style=\" font-size:20pt;\">{sol}</span></p></body></html>")
                    self.ui.OutputLabel_2.setText(str(sol))
            except:
                self.ui.OutputLabel.setText("Undefined or ∞")

    def percent(self):
        try:
            x = float(self.ui.OutputLabel.text())
            sol = x / 100 
            if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                self.ui.history_lbl.setText("")
            self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">{self.ui.OutputLabel.text()}%=</span></p><p><span style=\" font-size:20pt;\">{sol}</span></p></body></html>")
            self.ui.OutputLabel.setText(str(sol))
        except ValueError:
            pass


    def sqr(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            try:
                screen = self.ui.OutputLabel.text()
                sol = str(round(eval(f'{screen}**2'), 6))
                if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                    self.ui.history_lbl.setText("")
                self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">{self.ui.OutputLabel.text()}^2=</span></p><p><span style=\" font-size:20pt;\">{sol}</span></p></body></html>")
                self.ui.OutputLabel.setText(str(sol))
            except:
                self.ui.OutputLabel.setText("ERROR!")
        else:
            try:
                screen = self.ui.OutputLabel_2.text()
                sol = str(round(eval(f'{screen}**2'), 6))
                if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                    self.ui.history_lbl.setText("")
                self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">{self.ui.OutputLabel_2.text()}^2=</span></p><p><span style=\" font-size:20pt;\">{sol}</span></p></body></html>")
                self.ui.OutputLabel_2.setText(str(sol))
            except:
                self.ui.OutputLabel_2.setText("ERROR!")

    def sqrt(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            try:
                eva = eval(self.ui.OutputLabel.text().replace("x", "*"))
                n = float(eva)
                sol = str(round(math.sqrt(n), 14))
                split = sol.split(".")
                if split[1] == "0":
                    if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                        self.ui.history_lbl.setText("")
                    self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">√{self.ui.OutputLabel.text()}=</span></p><p><span style=\" font-size:20pt;\">{split[0]}</span></p></body></html>")
                    self.ui.OutputLabel.setText(str(split[0]))
                else:
                    if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                        self.ui.history_lbl.setText("")
                    self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">√{self.ui.OutputLabel.text()}=</span></p><p><span style=\" font-size:20pt;\">{sol}</span></p></body></html>")
                    self.ui.OutputLabel.setText(str(sol))
            except:
                self.ui.OutputLabel.setText("ERROR!")
        else:
            try:
                eva = eval(self.ui.OutputLabel_2.text().replace("x", "*"))
                n = float(eva)
                sol = str(round(math.sqrt(n), 14))
                split = sol.split(".")
                if split[1] == "0":
                    if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                        self.ui.history_lbl.setText("")
                    self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">√{self.ui.OutputLabel_2.text()}=</span></p><p><span style=\" font-size:20pt;\">{split[0]}</span></p></body></html>")
                    self.ui.OutputLabel_2.setText(str(split[0]))
                else:
                    if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                        self.ui.history_lbl.setText("")
                    self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">√{self.ui.OutputLabel_2.text()}=</span></p><p><span style=\" font-size:20pt;\">{sol}</span></p></body></html>")
                    self.ui.OutputLabel_2.setText(str(sol))
            except:
                self.ui.OutputLabel_2.setText("ERROR!")

    def back(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            try:
                screen = self.ui.OutputLabel.text()[:-1]
                self.ui.OutputLabel.setText(screen)
                if screen == "":
                    self.ui.OutputLabel.setFont(font2)
                    self.ui.OutputLabel.setText("0")
                    self.ui.ques_label.setText("")
            except:
                self.ui.OutputLabel.setText("ERROR!")
        elif self.ui.stackedWidget.currentIndex() == 1:
            try:
                screen = self.ui.OutputLabel_2.text()[:-1]
                self.ui.OutputLabel_2.setText(screen)
                if screen == "":
                    self.ui.OutputLabel_2.setFont(font2)
                    self.ui.OutputLabel_2.setText("0")
                    self.ui.ques_label2.setText("")
            except:
                self.ui.OutputLabel_2.setText("ERROR!")
        elif self.ui.stackedWidget.currentIndex() == 2:
            try:
                f = open("data\Exchange_Rates.csv", "r")
                csv_r = csv.reader(f)
                csv_rows = []
                for row in csv_r:
                    csv_rows.append(row)
                csv_rows.pop(0)
                f.close()

                r2d = csv_rows[0][1]
                r2e = csv_rows[1][1]
                d2r = csv_rows[2][1]
                e2r = csv_rows[3][1]
                d2e = csv_rows[4][1]
                e2d = csv_rows[5][1] 
                screen1 = self.ui.OutputLabel_4
                screen2 = self.ui.OutputLabel_3
                screen = self.ui.OutputLabel_4.text()[:-1]
                
                if screen == "":
                    self.ui.OutputLabel_4.setText("0")
                    self.ui.OutputLabel_3.setText("0")
                else:
                    if screen1.text() == "0" or screen1.text() == "ERROR!":
                        self.ui.OutputLabel_4.setText("0")
                    strp = screen1.text().replace("," , "")
                    strp1 = strp[:-1]
                    if "." in strp1:
                        strp2 = str("{:,}".format(float(strp1)))
                    else:
                        strp2 = str("{:,}".format(int(strp1)))
                    if "." in screen1.text():
                        screen1.setText(screen)
                    else:
                        screen1.setText(strp2)
                    screen = self.ui.OutputLabel_4.text().replace("," , "")
                    combo1 = self.ui.comboBox
                    combo2 = self.ui.comboBox_2
                    if combo1.currentIndex() == 0 and combo2.currentIndex() == 1:
                        sol = str(round(eval(f"{screen} * {str(r2d)}"), 2))
                    elif combo1.currentIndex() == 0 and combo2.currentIndex() == 2:
                        sol = str(round(eval(f"{screen} * {str(r2e)}"), 2))
                    elif combo1.currentIndex() == 1 and combo2.currentIndex() == 0:
                        sol = str(round(eval(f"{screen} * {str(d2r)}"), 2))
                    elif combo1.currentIndex() == 1 and combo2.currentIndex() == 2:
                        sol = str(round(eval(f"{screen} * {str(d2e)}"), 2))
                    elif combo1.currentIndex() == 2 and combo2.currentIndex() == 0:
                        sol = str(round(eval(f"{screen} * {str(e2r)}"), 2))
                    elif combo1.currentIndex() == 2 and combo2.currentIndex() == 1:
                        sol = str(round(eval(f"{screen} * {str(e2d)}"), 2))
                    if sol[-2] == "." and sol[-1] == "0":
                        self.ui.OutputLabel_3.setText(str("{:,.0f}".format(float(sol[0:-2]))))
                    else:
                        self.ui.OutputLabel_3.setText(str("{:,.2f}".format(float(sol))))
            except Exception as e:
                self.ui.OutputLabel_4.setText("ERROR!")
                self.ui.OutputLabel_3.setText("ERROR!")
                print(e)
                print(type(e))

    def equal(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            try:
                screen = self.ui.OutputLabel.text() 
                sol = str(round(eval(screen.replace("x", "*").replace("^", "**").replace("÷", "/")), 14))
                if "." in sol:
                    split = sol.split(".")
                    if split[1] == "0":
                        if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                            self.ui.history_lbl.setText("")
                        self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">{self.ui.OutputLabel.text()}=</span></p><p><span style=\" font-size:20pt;\">{split[0]}</span></p></body></html>")
                        self.ui.ques_label.setText(f"{screen}=")
                        self.ui.OutputLabel.setText(split[0])
                    else:
                        if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                            self.ui.history_lbl.setText("")
                        self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">{self.ui.OutputLabel.text()}=</span></p><p><span style=\" font-size:20pt;\">{sol}</span></p></body></html>")
                        self.ui.ques_label.setText(f"{screen}=")
                        self.ui.OutputLabel.setText(sol)
                else:
                    if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                        self.ui.history_lbl.setText("")
                    self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">{self.ui.OutputLabel.text()}=</span></p><p><span style=\" font-size:20pt;\">{sol}</span></p></body></html>")
                    self.ui.ques_label.setText(f"{screen}=")
                    self.ui.OutputLabel.setText(sol)
                 
            except:
                self.ui.OutputLabel.setText("ERROR!")
        elif self.ui.stackedWidget.currentIndex() == 1:
            try:
                screen = self.ui.OutputLabel_2.text()
                sol = str(round(eval(screen.replace("x", "*").replace("^", "**").replace("mod","%").replace("÷", "/")), 14))
                if "." in sol:
                    split = sol.split(".")
                    if split[1] == "0":
                        if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                            self.ui.history_lbl.setText("")
                        self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">{self.ui.OutputLabel_2.text()}=</span></p><p><span style=\" font-size:20pt;\">{split[0]}</span></p></body></html>")
                        self.ui.ques_label2.setText(f"{screen}=")
                        self.ui.OutputLabel_2.setText(split[0])
                    else:
                        if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                            self.ui.history_lbl.setText("")
                        self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">{self.ui.OutputLabel_2.text()}=</span></p><p><span style=\" font-size:20pt;\">{sol}</span></p></body></html>")
                        self.ui.ques_label2.setText(f"{screen}=")
                        self.ui.OutputLabel_2.setText(sol)
                else:
                    if self.ui.history_lbl.text() == "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">There's no history yet</span></p></body></html>":
                            self.ui.history_lbl.setText("")
                    self.ui.history_lbl.setText(f"{self.ui.history_lbl.text()}<html><head/><body><p><span style=\" color:#b8b8b8;\">{self.ui.OutputLabel_2.text()}=</span></p><p><span style=\" font-size:20pt;\">{sol}</span></p></body></html>")
                    self.ui.ques_label2.setText(f"{screen}=")
                    self.ui.OutputLabel_2.setText(sol)   
            except:
                self.ui.OutputLabel_2.setText("ERROR!")

        


    def negate(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            try:
                screen = self.ui.OutputLabel.text()
                if "-" in screen[0]:
                    self.ui.OutputLabel.setText(screen.replace("-", ""))
                elif screen == "0":
                    pass
                else:
                    self.ui.OutputLabel.setText(f"-{screen}")
            except:
                self.ui.OutputLabel.setText("ERROR!")
        else:
            try:
                screen = self.ui.OutputLabel_2.text()
                if "-" in screen[0]:
                    self.ui.OutputLabel_2.setText(screen.replace("-", ""))
                elif screen == "0":
                    pass
                else:
                    self.ui.OutputLabel_2.setText(f"-{screen}")
            except:
                self.ui.OutputLabel_2.setText("ERROR!")

    def clear(self):
            if self.ui.stackedWidget.currentIndex() == 0:
                self.ui.OutputLabel.setFont(font2)
                self.ui.OutputLabel.setText("0")
                self.ui.ques_label.setText("")
                
            elif self.ui.stackedWidget.currentIndex() == 1:
                self.ui.OutputLabel_2.setFont(font2)
                self.ui.OutputLabel_2.setText("0")
                self.ui.ques_label2.setText("")
                
            elif self.ui.stackedWidget.currentIndex() == 2:
                self.ui.OutputLabel_4.setText("0")
                self.ui.OutputLabel_3.setText("0")
            
    def press_it(self, pressed):
        if self.ui.stackedWidget.currentIndex() == 0:
            try:
                screen = self.ui.OutputLabel.text()
                if pressed == ".":
                    if screen == "ERROR!":
                            self.ui.OutputLabel.setText("")
                    if "." in screen:
                        if "+" in screen:
                            split = screen.split("+")
                            if "." in split[1]:
                                pass
                            else:
                                self.ui.OutputLabel.setText((f'{self.ui.OutputLabel.text()}.'))
                        else:
                            pass
                        if "-" in screen:
                            split = screen.split("-")
                            if "." in split[1]:
                                pass
                            else:
                                self.ui.OutputLabel.setText((f'{self.ui.OutputLabel.text()}.'))
                        else:
                            pass
                        if "x" in screen:
                            split = screen.split("x")
                            if "." in split[1]:
                                pass
                            else:
                                self.ui.OutputLabel.setText((f'{self.ui.OutputLabel.text()}.'))
                        else:
                            pass
                        if "÷" in screen:
                            split = screen.split("÷")
                            if "." in split[1]:
                                pass
                            else:
                                self.ui.OutputLabel.setText((f'{self.ui.OutputLabel.text()}.'))
                        else:
                            pass
                    else:
                        self.ui.OutputLabel.setText((f'{self.ui.OutputLabel.text()}.'))

                elif pressed == "-":
                    for i in operators:
                        if screen[-1] == i:
                            break
                    else:
                        self.ui.OutputLabel.setText(f'{screen}-')
                    
                elif pressed == "+":
                    for i in operators:
                        if screen[-1] == i:
                            break
                    else:
                        self.ui.OutputLabel.setText(f'{screen}+')
                elif pressed == "x":
                    for i in operators:
                        if screen[-1] == i:
                            break
                    else:
                        self.ui.OutputLabel.setText(f'{screen}x')
                elif pressed == "÷":
                    for i in operators:
                        if screen[-1] == i:
                            break
                    else:
                        self.ui.OutputLabel.setText(f'{screen}÷')
                else:
                    screen = self.ui.OutputLabel
                    if screen.text() == "0" or screen.text() == "ERROR!":
                        self.ui.OutputLabel.setText("")
                    screen.setText(f'{self.ui.OutputLabel.text()}{pressed}')
            except:
                self.ui.OutputLabel.setText("ERROR!")
            
        elif self.ui.stackedWidget.currentIndex() == 1:
            try:
                screen = self.ui.OutputLabel_2.text()
                if pressed == ".":
                    if screen == "ERROR!":
                            self.ui.OutputLabel_2.setText("")
                    if "." in screen:
                        if "+" in screen:
                            split = screen.split("+")
                            if "." in split[1]:
                                pass
                            else:
                                self.ui.OutputLabel_2.setText((f'{screen}.'))
                        else:
                            pass
                        if "-" in screen:
                            split = screen.split("-")
                            if "." in split[1]:
                                pass
                            else:
                                self.ui.OutputLabel_2.setText((f'{screen}.'))
                        else:
                            pass
                        if "x" in screen:
                            split = screen.split("x")
                            if "." in split[1]:
                                pass
                            else:
                                self.ui.OutputLabel_2.setText((f'{screen}.'))
                        else:
                            pass
                        if "÷" in screen:
                            split = screen.split("÷")
                            if "." in split[1]:
                                pass
                            else:
                                self.ui.OutputLabel_2.setText((f'{screen}.'))
                        else:
                            pass
                    else:
                        self.ui.OutputLabel_2.setText((f'{screen}.'))
        
                elif pressed == "-":

                    for i in operators[0:-1]:
                        if screen[-1] == i:
                            break
                    else:
                        self.ui.OutputLabel_2.setText(f'{screen}-')   
                elif pressed == "+":

                    for i in operators:
                        if screen[-1] == i:
                            break
                    else:
                        self.ui.OutputLabel_2.setText(f'{screen}+')
                elif pressed == "x":

                    for i in operators:
                        if screen[-1] == i:
                            break
                    else:
                        self.ui.OutputLabel_2.setText(f'{screen}x')
                elif pressed == "÷":

                    for i in operators:
                        if screen[-1] == i:
                            break
                    else:
                        self.ui.OutputLabel_2.setText(f'{screen}÷')

                elif pressed == "^":
                    if screen == "ERROR!":
                        self.ui.OutputLabel_2.setText("")
                        self.ui.OutputLabel_2.setText(f'{screen}0^')
                    else:
    
                        for i in operators:
                            if screen[-1] == i:
                                break
                        else:
                            self.ui.OutputLabel_2.setText(f'{screen}^')
                else:
                    if screen == "0" or screen == "ERROR!" or screen == "Memory Exceeded!":
                        self.ui.OutputLabel_2.setText("")
                    self.ui.OutputLabel_2.setText(f'{self.ui.OutputLabel_2.text()}{pressed}')
            except:
                self.ui.OutputLabel_2.setText("ERROR!")
        elif self.ui.stackedWidget.currentIndex() == 2:
            try:
                f = open("data\Exchange_Rates.csv", "r")
                csv_r = csv.reader(f)
                csv_rows = []
                for row in csv_r:
                    csv_rows.append(row)
                csv_rows.pop(0)
                f.close()

                r2d = csv_rows[0][1]
                r2e = csv_rows[1][1]
                d2r = csv_rows[2][1]
                e2r = csv_rows[3][1]
                d2e = csv_rows[4][1]
                e2d = csv_rows[5][1] 
                screen1 = self.ui.OutputLabel_4
                screen2 = self.ui.OutputLabel_3
                if pressed == ".":
                    if screen1.text() == "ERROR!":
                            self.ui.OutputLabel_4.setText("")
                    elif "." in screen1.text():
                        pass
                    else:
                        screen1.setText((f'{screen1.text()}.'))
                
                else:
                    if screen1.text() == "0" or screen1.text() == "ERROR!":
                        self.ui.OutputLabel_4.setText("")
                    if screen1.text() != "∞":
                        if "." in screen1.text():
                            self.ui.OutputLabel_4.setText(f'{self.ui.OutputLabel_4.text()}{pressed}')
                        else:
                            self.ui.OutputLabel_4.setText(f'{self.ui.OutputLabel_4.text()}{pressed}')
                            inpt = str("{:,}". format(float(self.ui.OutputLabel_4.text().replace(",", ""))))
                            split = inpt.split(".")
        
                            if split[-1] == "0":
                                self.ui.OutputLabel_4.setText(str("{:,.0f}". format(float(self.ui.OutputLabel_4.text().replace(",", "")))))
                            else:
                                self.ui.OutputLabel_4.setText(inpt)
                    else:
                        pass
                    
                    screen = self.ui.OutputLabel_4.text().replace("," , "")
                    combo1 = self.ui.comboBox
                    combo2 = self.ui.comboBox_2
                    if combo1.currentIndex() == 0 and combo2.currentIndex() == 1:
                        sol = str(round(eval(f"{screen} * {str(r2d)}"), 2))
                    elif combo1.currentIndex() == 0 and combo2.currentIndex() == 2:
                        sol = str(round(eval(f"{screen} * {str(r2e)}"), 2))
                    elif combo1.currentIndex() == 1 and combo2.currentIndex() == 0:
                        sol = str(round(eval(f"{screen} * {str(d2r)}"), 2))
                    elif combo1.currentIndex() == 1 and combo2.currentIndex() == 2:
                        sol = str(round(eval(f"{screen} * {str(d2e)}"), 2))
                    elif combo1.currentIndex() == 2 and combo2.currentIndex() == 0:
                        sol = str(round(eval(f"{screen} * {str(e2r)}"), 2))
                    elif combo1.currentIndex() == 2 and combo2.currentIndex() == 1:
                        sol = str(round(eval(f"{screen} * {str(e2d)}"), 2))
                    if sol[-2] == "." and sol[-1] == "0":
                        self.ui.OutputLabel_3.setText(str("{:,.0f}".format(float(sol[0:-2]))))
                    else:
                        self.ui.OutputLabel_3.setText(str("{:,.2f}".format(float(sol))))
                                                        
            except Exception as e:
                self.ui.OutputLabel_3.setText("ERROR!")
                self.ui.OutputLabel_4.setText("ERROR!")
                print(e)
                print(type(e))
    
    
    def pi(self):
        try:
            self.ui.OutputLabel_2.setText(str(round(math.pi, 14)))
        except:
            self.ui.OutputLabel_2.setText("ERROR!")
    
    def euler(self): 
        try:
            self.ui.OutputLabel_2.setText(str(round(math.e, 14)))
        except:
            self.ui.OutputLabel_2.setText("ERROR!")

    def mod(self):
        try:
            self.ui.OutputLabel_2.setText(f'{self.ui.OutputLabel_2.text()} mod ')
        except:
            self.ui.OutputLabel_2.setText("ERROR!")
    
    def exp(self):
        try:
            screen = self.ui.OutputLabel_2.text()
            x = math.exp(float(screen))
            self.ui.OutputLabel_2.setText(str(round (x, 7)))
        except:
            self.ui.OutputLabel_2.setText("ERROR!")
    
    def abs(self):
        try:
            screen = self.ui.OutputLabel_2.text()
            if "." in screen:
                x = abs(float(screen))
            else:
                x = abs(int(screen))
            self.ui.OutputLabel_2.setText(str(x))
        except:
            self.ui.OutputLabel_2.setText("ERROR!")

    def fact(self):
        try:
            screen = self.ui.OutputLabel_2.text()
            x = float(screen)
            sol = str(round(math.gamma(x + 1), 7))
            split = sol.split(".")
            if split[1] == "0":
                self.ui.OutputLabel_2.setText(split[0])
            else:
                if len(sol) > 15:
                    self.ui.OutputLabel_2.setFont(font)
                    self.ui.OutputLabel_2.setText(sol)
                else:
                    self.ui.OutputLabel_2.setText(sol)
        except:
            self.ui.OutputLabel_2.setText("ERROR!")

    def ten_power(self):
        screen = self.ui.OutputLabel_2.text()
        if len(screen) < 6:
            self.ui.OutputLabel_2.setText(str(round(eval(f"10 ** {screen}"), 8)))
        else:
            self.ui.OutputLabel_2.setText("Memory Exceeded!") 

    def log(self):
        screen = self.ui.OutputLabel_2.text()
        x = float(screen)
        sol = str(round(math.log10(x), 11))
        split = sol.split(".")
        if split[1] == "0":
            self.ui.OutputLabel_2.setText(split[0])
        else:
            self.ui.OutputLabel_2.setText(sol)

    def ln(self):
        screen = self.ui.OutputLabel_2.text()
        x = float(screen)
        sol = str(round(math.log1p(x - 1), 14))
        split = sol.split(".")  
        if split[1] == "0":
            self.ui.OutputLabel_2.setText(split[0])
        else:
            self.ui.OutputLabel_2.setText(sol)

    def change(self):
        combo1 = self.ui.comboBox
        combo2 = self.ui.comboBox_2
        cur1 = self.ui.currency_label
        cur2 = self.ui.currency_label2
 
        if combo1.currentIndex() == 0:
            cur1.setText(" ₹")
        elif combo1.currentIndex() == 1:
            cur1.setText(" $")
        elif combo1.currentIndex() == 2:
            cur1.setText(" €")
        self.ui.OutputLabel_3.setText("0")
        self.ui.OutputLabel_4.setText("0")

        if combo1.currentIndex() == combo2.currentIndex():   
            if combo1.currentIndex() == 0:
                combo2.setCurrentIndex(choice([1,2]))
            elif combo1.currentIndex() == 1:
                combo2.setCurrentIndex(choice([0,2]))
            elif combo1.currentIndex() == 2:
                combo2.setCurrentIndex(choice([0,1]))
            if combo2.currentIndex() == 0:
                cur2.setText(" ₹")
            elif combo2.currentIndex() == 1:
                cur2.setText(" $")
            elif combo2.currentIndex() == 2:
                cur2.setText(" €")
            self.ui.OutputLabel_3.setText("0")
            self.ui.OutputLabel_4.setText("0")

    def change2(self):
        combo1 = self.ui.comboBox
        combo2 = self.ui.comboBox_2
        cur1 = self.ui.currency_label
        cur2 = self.ui.currency_label2
 
        if combo2.currentIndex() == 0:
            cur2.setText(" ₹")
        elif combo2.currentIndex() == 1:
            cur2.setText(" $")
        elif combo2.currentIndex() == 2:
            cur2.setText(" €")
        self.ui.OutputLabel_3.setText("0")
        self.ui.OutputLabel_4.setText("0")


        if combo1.currentIndex() == combo2.currentIndex():   
            if combo2.currentIndex() == 0:
                combo1.setCurrentIndex(choice([1,2]))
            elif combo2.currentIndex() == 1:
                combo1.setCurrentIndex(choice([0,2]))
            elif combo2.currentIndex() == 2:
                combo1.setCurrentIndex(choice([0,1]))
            if combo1.currentIndex() == 0:
                cur1.setText(" ₹")
            elif combo1.currentIndex() == 1:
                cur1.setText(" $")
            elif combo1.currentIndex() == 2:
                cur1.setText(" €")
            self.ui.OutputLabel_3.setText("0")
            self.ui.OutputLabel_4.setText("0")


    def history(self):
        btn = self.ui.history_btn
        lbl = self.ui.history_scrl
        if lbl.height() == 0:
            lbl.setFixedHeight(421)
        else:
            lbl.setFixedHeight(0)

