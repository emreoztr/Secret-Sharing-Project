# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 80, 141, 31))
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(440, 80, 221, 31))
        self.label_2.setFont(font)
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 140, 81, 21))
        self.secretShare = QLineEdit(Widget)
        self.secretShare.setObjectName(u"secretShare")
        self.secretShare.setGeometry(QRect(120, 180, 131, 31))
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 180, 81, 21))
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 340, 58, 16))
        self.timeShare = QLabel(Widget)
        self.timeShare.setObjectName(u"timeShare")
        self.timeShare.setGeometry(QRect(70, 340, 121, 16))
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 270, 161, 51))
        self.secretParts = QTextEdit(Widget)
        self.secretParts.setObjectName(u"secretParts")
        self.secretParts.setGeometry(QRect(440, 180, 131, 401))
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(600, 170, 141, 151))
        self.lagrange = QRadioButton(self.groupBox)
        self.lagrange.setObjectName(u"lagrange")
        self.lagrange.setGeometry(QRect(20, 30, 99, 20))
        self.newton = QRadioButton(self.groupBox)
        self.newton.setObjectName(u"newton")
        self.newton.setGeometry(QRect(20, 60, 99, 20))
        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(600, 140, 141, 31))
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(600, 350, 131, 51))
        self.label_8 = QLabel(Widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(600, 420, 58, 16))
        self.secret = QLabel(Widget)
        self.secret.setObjectName(u"secret")
        self.secret.setGeometry(QRect(650, 420, 58, 16))
        self.timeReconst = QLabel(Widget)
        self.timeReconst.setObjectName(u"timeReconst")
        self.timeReconst.setGeometry(QRect(640, 450, 101, 16))
        self.label_11 = QLabel(Widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(600, 450, 58, 16))
        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(440, 150, 91, 16))
        self.label_9 = QLabel(Widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(180, 20, 411, 31))
        font1 = QFont()
        font1.setPointSize(36)
        self.label_9.setFont(font1)
        self.graph = QWidget(Widget)
        self.graph.setObjectName(u"graph")
        self.graph.setGeometry(QRect(10, 370, 401, 221))
        self.shareCount = QLineEdit(Widget)
        self.shareCount.setObjectName(u"shareCount")
        self.shareCount.setGeometry(QRect(120, 130, 131, 31))
        self.label_10 = QLabel(Widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 230, 81, 21))
        self.prime = QLineEdit(Widget)
        self.prime.setObjectName(u"prime")
        self.prime.setGeometry(QRect(120, 230, 131, 31))
        self.checkMultiThread = QCheckBox(Widget)
        self.checkMultiThread.setObjectName(u"checkMultiThread")
        self.checkMultiThread.setEnabled(True)
        self.checkMultiThread.setGeometry(QRect(600, 330, 121, 20))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"SHARING", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"RECONSTRUCT", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Share Count:", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Secret:", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Time:", None))
        self.timeShare.setText(QCoreApplication.translate("Widget", u"0ms", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Share", None))
        self.groupBox.setTitle("")
        self.lagrange.setText(QCoreApplication.translate("Widget", u"Lagrange", None))
        self.newton.setText(QCoreApplication.translate("Widget", u"Newton", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Interpolation Method:", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Reconstruct Secret", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"Secret:", None))
        self.secret.setText("")
        self.timeReconst.setText(QCoreApplication.translate("Widget", u"0ms", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"Time:", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Secret Parts:", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"SECRET SHARING DEMO", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"Prime:", None))
        self.checkMultiThread.setText(QCoreApplication.translate("Widget", u"Multi-Thread", None))
    # retranslateUi

