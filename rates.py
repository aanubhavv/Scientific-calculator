import csv
from main import MainWindow
from ui_Calc import *

#############################################################

from forex_python.converter import CurrencyRates
import datetime as d 

#############################################################

t_date = d.date.today()
time = d.datetime.today().strftime("%I:%M %p")
date = t_date.strftime("%b-%d-%Y")

class ratesFunc(MainWindow):
    def update_rates(self):
        screen = self.ui.update_lbl
        screen.setText("Updating...")
        self.ui.OutputLabel_3.setText("0")
        self.ui.OutputLabel_4.setText("0")
        if screen.text() == "Updating...":
            try:
                print("updating...")
                c = CurrencyRates()
                exc_r2d = str(c.convert('INR','USD', 1))
                exc_r2e = str(c.convert('INR','EUR', 1))
                exc_d2r = str(c.convert('USD','INR', 1))
                exc_e2r = str(c.convert('EUR','INR', 1))
                exc_d2e = str(c.convert('USD','EUR', 1))
                exc_e2d = str(c.convert('EUR','USD', 1))
                fields = ['Currency', 'Rates']
                rows = [['exc_r2d', exc_r2d], 
                        ['exc_r2e', exc_r2e], 
                        ['exc_d2r', exc_d2r], 
                        ['exc_e2r', exc_e2r], 
                        ['exc_d2e', exc_d2e], 
                        ['exc_e2d', exc_e2d]]
                with open("data\Exchange_Rates.csv", "w", newline="") as f:
                    csv_w = csv.writer(f)
                    csv_w.writerow(fields)
                    for i in rows:
                        csv_w.writerow(i)
                    print("updated File!!")
                    d_t = f"Last Updated on:- {date} {time}"
                    self.ui.update_lbl.setText(d_t)
                    with open("data\data.txt", "w") as f:
                        f.write(d_t)
                        print("updated data!!")
            except:
                self.ui.update_lbl.setText("error!")

         

    





