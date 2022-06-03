# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mmet.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(339, 449)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.pb_s1 = QPushButton(self.groupBox)
        self.pb_s1.setObjectName(u"pb_s1")

        self.verticalLayout.addWidget(self.pb_s1)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.pb_s2 = QPushButton(self.groupBox_2)
        self.pb_s2.setObjectName(u"pb_s2")

        self.verticalLayout_2.addWidget(self.pb_s2)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.cb_s3_servers = QCheckBox(self.groupBox_3)
        self.cb_s3_servers.setObjectName(u"cb_s3_servers")

        self.gridLayout.addWidget(self.cb_s3_servers, 2, 0, 1, 1)

        self.cb_s3_saves = QCheckBox(self.groupBox_3)
        self.cb_s3_saves.setObjectName(u"cb_s3_saves")

        self.gridLayout.addWidget(self.cb_s3_saves, 1, 1, 1, 1)

        self.cb_s3_config = QCheckBox(self.groupBox_3)
        self.cb_s3_config.setObjectName(u"cb_s3_config")

        self.gridLayout.addWidget(self.cb_s3_config, 1, 0, 1, 1)

        self.cb_s3_mods = QCheckBox(self.groupBox_3)
        self.cb_s3_mods.setObjectName(u"cb_s3_mods")
        self.cb_s3_mods.setEnabled(False)
        self.cb_s3_mods.setChecked(True)
        self.cb_s3_mods.setTristate(False)

        self.gridLayout.addWidget(self.cb_s3_mods, 0, 0, 1, 1)

        self.cb_s3_shaderpacks = QCheckBox(self.groupBox_3)
        self.cb_s3_shaderpacks.setObjectName(u"cb_s3_shaderpacks")

        self.gridLayout.addWidget(self.cb_s3_shaderpacks, 2, 1, 1, 1)

        self.cb_s3_resourcepacks = QCheckBox(self.groupBox_3)
        self.cb_s3_resourcepacks.setObjectName(u"cb_s3_resourcepacks")

        self.gridLayout.addWidget(self.cb_s3_resourcepacks, 0, 1, 1, 1)

        self.cb_s3_options = QCheckBox(self.groupBox_3)
        self.cb_s3_options.setObjectName(u"cb_s3_options")

        self.gridLayout.addWidget(self.cb_s3_options, 3, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.line = QFrame(self.groupBox_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.cb_s3_all = QCheckBox(self.groupBox_3)
        self.cb_s3_all.setObjectName(u"cb_s3_all")

        self.verticalLayout_3.addWidget(self.cb_s3_all)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton = QPushButton(self.groupBox_4)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_5.addWidget(self.groupBox_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Minecraft\u6574\u5408\u5305\u5bfc\u51fa\u5de5\u5177", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u6b65", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4f60\u7684 versions \u6587\u4ef6\u5939\uff08\u8bf7\u5f00\u542f\u7248\u672c\u9694\u79bb\uff09", None))
        self.pb_s1.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u6b64\u5904", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e8c\u6b65", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4f60\u8981\u5bfc\u51fa\u7684\u6e38\u620f\u7248\u672c", None))
        self.pb_s2.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u6b64\u5904", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e09\u6b65", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u9644\u52a0\u5bfc\u51fa\u8bbe\u7f6e", None))
        self.cb_s3_servers.setText(QCoreApplication.translate("MainWindow", u"servers.dat \u670d\u52a1\u5668\u5217\u8868", None))
        self.cb_s3_saves.setText(QCoreApplication.translate("MainWindow", u"saves \u5b58\u6863", None))
        self.cb_s3_config.setText(QCoreApplication.translate("MainWindow", u"config \u914d\u7f6e\u6587\u4ef6", None))
        self.cb_s3_mods.setText(QCoreApplication.translate("MainWindow", u"mods", None))
        self.cb_s3_shaderpacks.setText(QCoreApplication.translate("MainWindow", u"shaderpacks \u5149\u5f71\u5305", None))
        self.cb_s3_resourcepacks.setText(QCoreApplication.translate("MainWindow", u"resourcepacks \u8d44\u6e90\u5305", None))
        self.cb_s3_options.setText(QCoreApplication.translate("MainWindow", u"options.txt \u6e38\u620f\u8bbe\u7f6e", None))
        self.cb_s3_all.setText(QCoreApplication.translate("MainWindow", u"* \u9644\u5e26\u6587\u4ef6\u5939\u4e0b\u6240\u6709\u5185\u5bb9\uff08\u7279\u6b8a\u6574\u5408\u5305\u53ef\u80fd\u9700\u8981\uff09", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u56db\u6b65", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\uff01", None))
    # retranslateUi

