# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
import secret_sharing_lagrange
import secret_sharing_newton
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import matplotlib
import numpy as np
matplotlib.use('qt5agg')
p = 2 ** 127 - 1
_PRIME = 2 ** 127 - 1
# Use the generated prime number as modulo
modulo = p

class Widget(QWidget):
    def __init__(self, parent=None):
        self.use_thread = True
        self.share_secret = secret_sharing_lagrange.share_secret
        self.reveal_secret = secret_sharing_lagrange.reveal_secret
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.prime.setText(str(_PRIME))
        self.ui.pushButton.clicked.connect(self.button_share_click)
        self.ui.pushButton_2.clicked.connect(self.button_reconst_click)
        self.ui.lagrange.clicked.connect(self.handle_lagrange_button)
        self.ui.newton.clicked.connect(self.handle_newton_button)
        self.ui.checkMultiThread.stateChanged.connect(self.thread_check_box_changed)
        self.fig = plt.Figure()
        self.canvas = matplotlib.backends.backend_qt5agg.FigureCanvas(self.fig)
        layout = QVBoxLayout(self.ui.graph)
        layout.addWidget(self.canvas)
        self.ax = self.fig.add_subplot()
    
    def button_share_click(self):
        _PRIME = int(self.ui.prime.text())
        p=_PRIME
        modulo=p
        secret_sharing_lagrange._PRIME = _PRIME
        secret_sharing_lagrange.p = _PRIME
        secret_sharing_lagrange.modulo = _PRIME

        secret_sharing_newton._PRIME = _PRIME
        secret_sharing_newton.p = _PRIME
        secret_sharing_newton.modulo = _PRIME
        count = self.ui.shareCount.text()
        secret = self.ui.secretShare.text()
        secrets, t, poly = self.share_secret(int(secret), int(count), int(count))
        self.ui.secretParts.setText(str(secrets))
        self.ui.timeShare.setText(str(t)+"ms")
        x = np.linspace(-1, 15, 100)
        y = [secret_sharing_lagrange._eval_at(poly, i, _PRIME) for i in x]
        
        
        self.ax.clear()
        self.ax.plot(x, y)
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_title('Polynomial Plot')
        self.canvas.draw()
        # Add code to create and customize the plot here

        

    
    def button_reconst_click(self):
        parts = self.ui.secretParts.toPlainText()
        parts = eval(parts)
        secret,t = self.reveal_secret(parts, self.use_thread)
        self.ui.secret.setText(str(secret))
        self.ui.timeReconst.setText(str(round(t, 3)) + "ms")
    
    def handle_lagrange_button(self):
        self.reveal_secret = secret_sharing_lagrange.reveal_secret

    def handle_newton_button(self):
        self.reveal_secret = secret_sharing_newton.reveal_secret

    def thread_check_box_changed(self, checked):
        if checked:
            self.use_thread = True
        else:
            self.use_thread = False
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())


