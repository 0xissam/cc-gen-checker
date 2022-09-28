from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMessageBox
import random
import string
import requests
import os
import termcolor

cc_card_list = []
valid_cc = []
died_cc =[]

class CreditCard:
        # Main Method
        @staticmethod
        def main(args):
                for number in cc_card_list: 
                        number = int(number)
                        #print(str(number) + " is " + ("valid" if CreditCard.isValid(number) else "invalid"))
                        if CreditCard.isValid(number):
                                valid_cc.append(number)
                                #print(f"is valid {number}")
                        else:
                                died_cc.append(number)
                                #print(f"is invalid {number}")
                                #print(valid_cc)

                
        # Return true if the card number is valid
        @staticmethod
        def isValid(number):
                return (CreditCard.getSize(number) >= 13 and CreditCard.getSize(number) <= 16) and (CreditCard.prefixMatched(number, 4) or CreditCard.prefixMatched(number, 5) or CreditCard.prefixMatched(number, 37) or CreditCard.prefixMatched(number, 6)) and ((CreditCard.sumOfDoubleEvenPlace(number) + CreditCard.sumOfOddPlace(number)) % 10 == 0)
        
        # Get the result from Step 2
        @staticmethod
        def sumOfDoubleEvenPlace(number):
                sum = 0
                num = str(number) + ""
                i = CreditCard.getSize(number) - 2
                while (i >= 0):
                        sum += CreditCard.getDigit(int(str(num[i]) + "") * 2)
                        i -= 2
                return sum
        
        # Return this number if it is a single digit, otherwise,
        # return the sum of the two digits
        @staticmethod
        def getDigit(number):
                if (number < 9):
                        return number
                return int(number / 10) + number % 10
        
        # Return sum of odd-place digits in number
        @staticmethod
        def sumOfOddPlace(number):
                sum = 0
                num = str(number) + ""
                i = CreditCard.getSize(number) - 1
                while (i >= 0):
                        sum += int(str(num[i]) + "")
                        i -= 2
                return sum
        
        # Return true if the digit d is a prefix for number
        @staticmethod
        def prefixMatched(number, d):
                return CreditCard.getPrefix(number, CreditCard.getSize(d)) == d
        
        # Return the number of digits in d
        @staticmethod
        def getSize(d):
                num = str(d) + ""
                return len(num)
        
        # Return the first k number of digits from
        # number. If the number of digits in number
        # is less than k, return number.
        @staticmethod
        def getPrefix(number, k):
                if (CreditCard.getSize(number) > k):
                        num = str(number) + ""
                        return int(num[0:k])
                return number



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('carding.ico'))
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:#000000;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Heebo")
        font.setPointSize(41)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("font-family: \'Heebo\', sans-serif;\n"
"font-size: 2.9375rem;\n"
"font-weight: 600;\n"
"letter-spacing: 0.075rem;\n"
"font-style: normal;\n"
"text-transform: uppercase;\n"
"color: #000000;\n"
"background-color: #29ff74;\n"
"border-radius: 1.0625rem;\n"
"-webkit-border-radius: 1.0625rem;\n"
"-moz-border-radius: 1.0625rem;\n"
"padding: 1.0625rem 1.125rem;\n"
"border-style: solid;\n"
"border-width: 0.375rem;\n"
"border-color: #000000;\n"
"-webkit-box-shadow: none;\n"
"-moz-box-shadow: none;\n"
"-box-shadow: none;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Heebo")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font-family: \'Heebo\', sans-serif;\n"
"font-size: 2.9375rem;\n"
"font-weight: 600;\n"
"letter-spacing: 0.075rem;\n"
"font-style: normal;\n"
"text-transform: uppercase;\n"
"color: #000000;\n"
"background-color: #29ff74;\n"
"border-radius: 1.0625rem;\n"
"-webkit-border-radius: 1.0625rem;\n"
"-moz-border-radius: 1.0625rem;\n"
"padding: 1.0625rem 1.125rem;\n"
"border-style: solid;\n"
"border-width: 0.375rem;\n"
"border-color: #000000;\n"
"-webkit-box-shadow: none;\n"
"-moz-box-shadow: none;\n"
"-box-shadow: none;\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-family: \'Poppins\', sans-serif;\n"
"font-size: 0.9375rem;\n"
"font-weight: 700;\n"
"letter-spacing: 0.045rem;\n"
"font-style: normal;\n"
"text-transform: uppercase;\n"
"color: #000000;\n"
"background-color: #65f53d;\n"
"border-radius: 0.6875rem;\n"
"-webkit-border-radius: 0.6875rem;\n"
"-moz-border-radius: 0.6875rem;\n"
"padding: 0.4375rem 1.25rem;\n"
"border-style: solid;\n"
"border-width: 0.1875rem;\n"
"border-color: #000000;\n"
"-webkit-box-shadow: none;\n"
"-moz-box-shadow: none;\n"
"-box-shadow: none;")
        self.label_2.setLineWidth(2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setIndent(2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_bin = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_bin.sizePolicy().hasHeightForWidth())
        self.lineEdit_bin.setSizePolicy(sizePolicy)
        self.lineEdit_bin.setMaximumSize(QtCore.QSize(16777207, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_bin.setFont(font)
        self.lineEdit_bin.setStyleSheet(" padding: 3px;\n"
"     font-size: 16px;\n"
"     border-width: 2px;\n"
"     border-color: #cccccc;\n"
"     background-color: #ffffff;\n"
"     color: #000000;\n"
"     border-style: groove;\n"
"     border-radius: 27px;\n"
"     box-shadow: 0px 0px 5px rgba(66,66,66,.75);\n"
"     text-shadow: 0px 0px 5px rgba(66,66,66,.75);")
        self.lineEdit_bin.setInputMask("")
        self.lineEdit_bin.setText("")
        self.lineEdit_bin.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_bin.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_bin.setDragEnabled(False)
        self.lineEdit_bin.setClearButtonEnabled(False)
        self.lineEdit_bin.setObjectName("lineEdit_bin")
        self.horizontalLayout.addWidget(self.lineEdit_bin)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-family: \'Poppins\', sans-serif;\n"
"font-size: 0.9375rem;\n"
"font-weight: 700;\n"
"letter-spacing: 0.045rem;\n"
"font-style: normal;\n"
"text-transform: uppercase;\n"
"color: #000000;\n"
"background-color: #65f53d;\n"
"border-radius: 0.6875rem;\n"
"-webkit-border-radius: 0.6875rem;\n"
"-moz-border-radius: 0.6875rem;\n"
"padding: 0.4375rem 1.25rem;\n"
"border-style: solid;\n"
"border-width: 0.1875rem;\n"
"border-color: #000000;\n"
"-webkit-box-shadow: none;\n"
"-moz-box-shadow: none;\n"
"-box-shadow: none;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setIndent(10)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_month = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_month.sizePolicy().hasHeightForWidth())
        self.lineEdit_month.setSizePolicy(sizePolicy)
        self.lineEdit_month.setStyleSheet(" padding: 3px;\n"
"     font-size: 16px;\n"
"     border-width: 2px;\n"
"     border-color: #cccccc;\n"
"     background-color: #ffffff;\n"
"     color: #000000;\n"
"     border-style: groove;\n"
"     border-radius: 27px;\n"
"     box-shadow: 0px 0px 5px rgba(66,66,66,.75);\n"
"     text-shadow: 0px 0px 5px rgba(66,66,66,.75);")
        self.lineEdit_month.setInputMask("")
        self.lineEdit_month.setObjectName("lineEdit_month")
        self.horizontalLayout_2.addWidget(self.lineEdit_month)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font-family: \'Poppins\', sans-serif;\n"
"font-size: 0.9375rem;\n"
"font-weight: 700;\n"
"letter-spacing: 0.045rem;\n"
"font-style: normal;\n"
"text-transform: uppercase;\n"
"color: #000000;\n"
"background-color: #65f53d;\n"
"border-radius: 0.6875rem;\n"
"-webkit-border-radius: 0.6875rem;\n"
"-moz-border-radius: 0.6875rem;\n"
"padding: 0.4375rem 1.25rem;\n"
"border-style: solid;\n"
"border-width: 0.1875rem;\n"
"border-color: #000000;\n"
"-webkit-box-shadow: none;\n"
"-moz-box-shadow: none;\n"
"-box-shadow: none;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_year = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_year.sizePolicy().hasHeightForWidth())
        self.lineEdit_year.setSizePolicy(sizePolicy)
        self.lineEdit_year.setStyleSheet(" padding: 3px;\n"
"     font-size: 16px;\n"
"     border-width: 2px;\n"
"     border-color: #cccccc;\n"
"     background-color: #ffffff;\n"
"     color: #000000;\n"
"     border-style: groove;\n"
"     border-radius: 27px;\n"
"     box-shadow: 0px 0px 5px rgba(66,66,66,.75);\n"
"     text-shadow: 0px 0px 5px rgba(66,66,66,.75);")
        self.lineEdit_year.setInputMask("")
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.horizontalLayout_3.addWidget(self.lineEdit_year)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font-family: \'Poppins\', sans-serif;\n"
"font-size: 0.9375rem;\n"
"font-weight: 700;\n"
"letter-spacing: 0.045rem;\n"
"font-style: normal;\n"
"text-transform: uppercase;\n"
"color: #000000;\n"
"background-color: #65f53d;\n"
"border-radius: 0.6875rem;\n"
"-webkit-border-radius: 0.6875rem;\n"
"-moz-border-radius: 0.6875rem;\n"
"padding: 0.4375rem 1.25rem;\n"
"border-style: solid;\n"
"border-width: 0.1875rem;\n"
"border-color: #000000;\n"
"-webkit-box-shadow: none;\n"
"-moz-box-shadow: none;\n"
"-box-shadow: none;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setIndent(5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lineEdit_amount = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_amount.sizePolicy().hasHeightForWidth())
        self.lineEdit_amount.setSizePolicy(sizePolicy)
        self.lineEdit_amount.setStyleSheet(" padding: 3px;\n"
"     font-size: 16px;\n"
"     border-width: 2px;\n"
"     border-color: #cccccc;\n"
"     background-color: #ffffff;\n"
"     color: #000000;\n"
"     border-style: groove;\n"
"     border-radius: 27px;\n"
"     box-shadow: 0px 0px 5px rgba(66,66,66,.75);\n"
"     text-shadow: 0px 0px 5px rgba(66,66,66,.75);")
        self.lineEdit_amount.setInputMask("")
        self.lineEdit_amount.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_amount.setObjectName("lineEdit_amount")
        self.horizontalLayout_6.addWidget(self.lineEdit_amount)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font-family: \'Poppins\', sans-serif;\n"
"font-size: 0.9375rem;\n"
"font-weight: 700;\n"
"letter-spacing: 0.045rem;\n"
"font-style: normal;\n"
"text-transform: uppercase;\n"
"color: #000000;\n"
"background-color: #65f53d;\n"
"border-radius: 0.6875rem;\n"
"-webkit-border-radius: 0.6875rem;\n"
"-moz-border-radius: 0.6875rem;\n"
"padding: 0.4375rem 1.25rem;\n"
"border-style: solid;\n"
"border-width: 0.1875rem;\n"
"border-color: #000000;\n"
"-webkit-box-shadow: none;\n"
"-moz-box-shadow: none;\n"
"-box-shadow: none;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setIndent(4)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font-family: \'Poppins\', sans-serif;\n"
"font-size: 0.9375rem;\n"
"font-weight: 700;\n"
"letter-spacing: 0.045rem;\n"
"font-style: normal;\n"
"text-transform: uppercase;\n"
"color: #000000;\n"
"background-color: #65f53d;\n"
"border-radius: 0.6875rem;\n"
"-webkit-border-radius: 0.6875rem;\n"
"-moz-border-radius: 0.6875rem;\n"
"padding: 0.4375rem 1.25rem;\n"
"border-style: solid;\n"
"border-width: 0.1875rem;\n"
"border-color: #000000;\n"
"-webkit-box-shadow: none;\n"
"-moz-box-shadow: none;\n"
"-box-shadow: none;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.textEdit_generated = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_generated.setStyleSheet("padding: 3px;\n"
"font-size: 16px;\n"
"border-width: 2px;\n"
"border-color: #29ff74;\n"
"background-color: #000000;\n"
"color: #ffffff;\n"
"border-style: groove;\n"
"border-radius: 0px;\n"
"box-shadow: 0px 0px 5px rgba(66,66,66,.75);\n"
"text-shadow: 0px 0px 5px rgba(66,66,66,.75);")
        self.textEdit_generated.setReadOnly(True)
        self.textEdit_generated.setPlaceholderText("")
        self.textEdit_generated.setObjectName("textEdit_generated")
        self.horizontalLayout_9.addWidget(self.textEdit_generated)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setStyleSheet("padding: 3px;\n"
"font-size: 16px;\n"
"border-width: 2px;\n"
"border-color: #29ff74;\n"
"background-color: #000000;\n"
"color: #ffffff;\n"
"border-style: groove;\n"
"border-radius: 0px;\n"
"box-shadow: 0px 0px 5px rgba(66,66,66,.75);\n"
"text-shadow: 0px 0px 5px rgba(66,66,66,.75);")
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_9.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_generate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_generate.clicked.connect(self.generate)
        self.pushButton_generate.setStyleSheet(".QPushButton {\n"
"   background-color: #65f53d;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    color: #000000;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"  transition: 1s ease-in-out;\n"
"  background: #5cd65c;\n"
"}\n"
"")
        self.pushButton_generate.setObjectName("pushButton_generate")
        self.horizontalLayout_5.addWidget(self.pushButton_generate)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.delete)
        self.pushButton.setStyleSheet(".QPushButton {\n"
"   background-color: #65f53d;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    color: #000000;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"  transition: 1s ease-in-out;\n"
"  background: #5cd65c;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CC Gen Checker"))
        self.label.setText(_translate("MainWindow", "CC gen cheker"))
        self.label_6.setText(_translate("MainWindow", "developed by issam_thr"))
        self.label_2.setText(_translate("MainWindow", "The Bin Code"))
        self.lineEdit_bin.setPlaceholderText(_translate("MainWindow", "468005603027xxxx"))
        self.label_3.setText(_translate("MainWindow", "Expiration MONTH"))
        self.lineEdit_month.setPlaceholderText(_translate("MainWindow", "rand"))
        self.label_4.setText(_translate("MainWindow", "Expiration Year"))
        self.lineEdit_year.setPlaceholderText(_translate("MainWindow", "rand"))
        self.label_5.setText(_translate("MainWindow", "Amount of cards to generate"))
        self.lineEdit_amount.setPlaceholderText(_translate("MainWindow", "rand 10"))
        self.label_8.setText(_translate("MainWindow", "generated cc"))
        self.label_7.setText(_translate("MainWindow", "checked cc"))
        self.pushButton_generate.setText(_translate("MainWindow", "Generate And Check"))
        self.pushButton.setText(_translate("MainWindow", "Clear"))

    def message_worninig(self, sms):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('CC Gen Checker')
            msg.setText(f"{sms}")
            msg.setWindowIcon(QtGui.QIcon('carding.ico'))
            msg.setStyleSheet(".QPushButton {\n"
                              "   background-color: #65f53d;\n"
                              "    border-style: outset;\n"
                              "    border-width: 0px;\n"
                              "    border-radius: 0px;\n"
                              "    color: #000000;\n"
                              "    border-color: beige;\n"
                              "    font: bold 14px;\n"
                              "    min-width: 10em;\n"
                              "    padding: 6px;\n"
                              "}\n"
                              "\n"
                              ".QPushButton:hover {\n"
                              "  transition: 1s ease-in-out;\n"
                              "  background: #f5473b;\n"
                              "}\n"
                              "")

            show = msg.exec_()

    def checke(self):
            cookies = {
                    '_ga': 'GA1.2.806246814.1663673087',
                    '_gid': 'GA1.2.982704913.1663673087',
            }

            headers = {
                    'authority': 'mmotools.net',
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9,fr;q=0.8,fr-FR;q=0.7,en-GB;q=0.6',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    # Requests sorts cookies= alphabetically
                    # 'cookie': '_ga=GA1.2.806246814.1663673087; _gid=GA1.2.982704913.1663673087',
                    'origin': 'https://mmotools.net',
                    'referer': 'https://mmotools.net/livedie0x9853c3367064dffcff2311ab5ae4f1e97cfce04f7210f6cd5f5b7b80ba636d15/',
                    'sec-ch-ua': '"Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42',
                    'x-requested-with': 'XMLHttpRequest',
            }

            live_list = []
            die_list = []
            unknown_list = []

            for i in cc_card_list:
                    data = {
                            'data': f'{i}',
                    }

                    response = requests.post(
                            'https://mmotools.net/livedie0x9853c3367064dffcff2311ab5ae4f1e97cfce04f7210f6cd5f5b7b80ba636d15/api.php',
                            cookies=cookies,
                            headers=headers, data=data)

                    if 'Live' in response.text:
                            live_list.append(i)
                    elif 'Die' in response.text:
                            die_list.append(i)
                    elif 'Unknown' in response.text:
                            unknown_list.append(i)

            # self.textEdit.setText('')
            live_list = [elem.replace('|', '') for elem in live_list]

            for i in live_list:
                    greenColor = QColor(0, 255, 0)
                    self.textEdit.setTextColor(greenColor)
                    self.textEdit.insertPlainText(f'[    Live    ]  {int(i)}\n')
                    self.textEdit.repaint()
            for i in die_list:
                    redColor = QColor(255, 0, 0)
                    self.textEdit.setTextColor(redColor)
                    self.textEdit.insertPlainText(f'[     Die    ]  {i}\n')
                    self.textEdit.repaint()
            for i in unknown_list:
                    yellowColor = QColor(255, 255, 0)
                    self.textEdit.setTextColor(yellowColor)
                    self.textEdit.insertPlainText(f'[Unknown]  {i}\n')
                    self.textEdit.repaint()

            return

    def generate(self):
            cc_card_list.clear()
            degits = string.digits
            months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
            yeras = ['2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']
            bin = self.lineEdit_bin.text().strip()
            if bin == '':
                    self.message_worninig(sms="Please Enter Bin Code !")
                    return

            if len(bin) < 16:
                    number_of_x = 16 - len(bin)
                    bin = bin + ('x' * number_of_x)
            else:
                    pass
            number_of_times = self.lineEdit_amount.text().strip()
            if number_of_times == '':
                    number_of_times = 10
            else:
                    pass

            month = self.lineEdit_month.text().strip()
            year = self.lineEdit_year.text().strip()

            for i in range(int(number_of_times)):
                    if month == '':
                            monttt = ''.join((random.choice(months)))
                    else:
                            monttt = month
                    if year == '':
                            yearttt = ''.join((random.choice(yeras)))
                    else:
                            yearttt = year
                    if "x" in bin:
                            conter_of_x = (bin.count("x"))
                            striped_cc = bin.strip('x')
                            last = ''.join((random.sample(degits, conter_of_x)))
                            cvv = ''.join((random.sample(degits, 3)))
                            cc_card = striped_cc + last  
                            #cc_card = striped_cc + last + "|" + monttt + "|" + yearttt + "|" + cvv
                            cc_card_list.append(cc_card)

            # self.textEdit_generated.setText('')
            for i in cc_card_list:
                    self.textEdit_generated.insertPlainText('[ + ]  ' + i + '\n')
                    self.textEdit_generated.repaint()

            #self.checke()
            CreditCard.main([])

            for i in valid_cc:
                    if month == '':
                            monttt = ''.join((random.choice(months)))
                    else:
                            monttt = month
                    if year == '':
                            yearttt = ''.join((random.choice(yeras)))
                    else:
                            yearttt = year
                    
                    cvv = ''.join((random.sample(degits, 3)))
                    greenColor = QColor(0, 255, 0)
                    self.textEdit.setTextColor(greenColor)
                    self.textEdit.insertPlainText(f'{i}|{monttt}|{yearttt}|{cvv}\n')   # [    Live    ]  
                    self.textEdit.repaint()

            for i in died_cc:
                if month == '':
                        monttt = ''.join((random.choice(months)))
                else:
                        monttt = month
                if year == '':
                        yearttt = ''.join((random.choice(yeras)))
                else:
                        yearttt = year
                    
                cvv = ''.join((random.sample(degits, 3)))

                redColor = QColor(255, 0, 0)
                self.textEdit.setTextColor(redColor)
                self.textEdit.insertPlainText(f'{i}|{monttt}|{yearttt}|{cvv}\n')
                self.textEdit.repaint()

            return

    def delete(self):
            cc_card_list.clear()
            self.lineEdit_bin.setText('')
            self.lineEdit_year.setText('')
            self.lineEdit_month.setText('')
            self.lineEdit_amount.setText('')

            self.textEdit_generated.clear()
            self.textEdit_generated.repaint()
            self.textEdit.clear()
            self.textEdit.repaint()
            return


if __name__ == "__main__":
        import sys

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
