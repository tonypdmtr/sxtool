# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/gui/ui_form_insert_row_value.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormInsertRowValue(object):
    def setupUi(self, FormInsertRowValue):
        FormInsertRowValue.setObjectName('FormInsertRowValue')
        FormInsertRowValue.resize(545, 371)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(FormInsertRowValue)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName('verticalLayout_3')
        self.groupFormat_2 = QtWidgets.QGroupBox(FormInsertRowValue)
        self.groupFormat_2.setObjectName('groupFormat_2')
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupFormat_2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.spinNbLines = QtWidgets.QSpinBox(self.groupFormat_2)
        self.spinNbLines.setMinimum(1)
        self.spinNbLines.setObjectName('spinNbLines')
        self.horizontalLayout_2.addWidget(self.spinNbLines)
        spacerItem = QtWidgets.QSpacerItem(461, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.groupFormat_2)
        self.groupFormat = QtWidgets.QGroupBox(FormInsertRowValue)
        self.groupFormat.setObjectName('groupFormat')
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupFormat)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.checkBoxFormat = QtWidgets.QCheckBox(self.groupFormat)
        self.checkBoxFormat.setChecked(True)
        self.checkBoxFormat.setObjectName('checkBoxFormat')
        self.horizontalLayout.addWidget(self.checkBoxFormat)
        self.comboBoxFormat = QtWidgets.QComboBox(self.groupFormat)
        self.comboBoxFormat.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily('Courier New')
        self.comboBoxFormat.setFont(font)
        self.comboBoxFormat.setMaxCount(5)
        self.comboBoxFormat.setDuplicatesEnabled(False)
        self.comboBoxFormat.setObjectName('comboBoxFormat')
        self.comboBoxFormat.addItem('')
        self.comboBoxFormat.addItem('')
        self.comboBoxFormat.addItem('')
        self.horizontalLayout.addWidget(self.comboBoxFormat)
        self.verticalLayout_3.addWidget(self.groupFormat)
        self.buttonGroupAddress = QtWidgets.QGroupBox(FormInsertRowValue)
        self.buttonGroupAddress.setObjectName('buttonGroupAddress')
        self.gridLayout = QtWidgets.QGridLayout(self.buttonGroupAddress)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName('gridLayout')
        self.radioPrevContinuity = QtWidgets.QRadioButton(self.buttonGroupAddress)
        self.radioPrevContinuity.setChecked(True)
        self.radioPrevContinuity.setObjectName('radioPrevContinuity')
        self.gridLayout.addWidget(self.radioPrevContinuity, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(163, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(162, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.radioNextContinuity = QtWidgets.QRadioButton(self.buttonGroupAddress)
        self.radioNextContinuity.setObjectName('radioNextContinuity')
        self.gridLayout.addWidget(self.radioNextContinuity, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(163, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(162, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 2, 1, 1)
        self.radioExplicitAddr = QtWidgets.QRadioButton(self.buttonGroupAddress)
        self.radioExplicitAddr.setObjectName('radioExplicitAddr')
        self.gridLayout.addWidget(self.radioExplicitAddr, 2, 0, 1, 1)
        self.lineAddrStart = QtWidgets.QLineEdit(self.buttonGroupAddress)
        self.lineAddrStart.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily('Courier New')
        self.lineAddrStart.setFont(font)
        self.lineAddrStart.setMaxLength(4)
        self.lineAddrStart.setAlignment(QtCore.Qt.AlignRight)
        self.lineAddrStart.setObjectName('lineAddrStart')
        self.gridLayout.addWidget(self.lineAddrStart, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(162, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.buttonGroupAddress)
        self.groupData = QtWidgets.QGroupBox(FormInsertRowValue)
        self.groupData.setObjectName('groupData')
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupData)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName('horizontalLayout_4')
        self.label = QtWidgets.QLabel(self.groupData)
        self.label.setObjectName('label')
        self.horizontalLayout_4.addWidget(self.label)
        self.spinRowSize = QtWidgets.QSpinBox(self.groupData)
        self.spinRowSize.setMinimum(1)
        self.spinRowSize.setProperty('value', 16)
        self.spinRowSize.setObjectName('spinRowSize')
        self.horizontalLayout_4.addWidget(self.spinRowSize)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName('horizontalLayout_6')
        self.label_2 = QtWidgets.QLabel(self.groupData)
        self.label_2.setObjectName('label_2')
        self.horizontalLayout_6.addWidget(self.label_2)
        self.lineEditData = QtWidgets.QLineEdit(self.groupData)
        font = QtGui.QFont()
        font.setFamily('Courier New')
        self.lineEditData.setFont(font)
        self.lineEditData.setMaxLength(256)
        self.lineEditData.setAlignment(QtCore.Qt.AlignRight)
        self.lineEditData.setObjectName('lineEditData')
        self.horizontalLayout_6.addWidget(self.lineEditData)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addWidget(self.groupData)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName('horizontalLayout_5')
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.pushButtonOK = QtWidgets.QPushButton(FormInsertRowValue)
        self.pushButtonOK.setObjectName('pushButtonOK')
        self.horizontalLayout_5.addWidget(self.pushButtonOK)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.pushButtonCancel = QtWidgets.QPushButton(FormInsertRowValue)
        self.pushButtonCancel.setObjectName('pushButtonCancel')
        self.horizontalLayout_5.addWidget(self.pushButtonCancel)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.retranslateUi(FormInsertRowValue)
        self.pushButtonOK.clicked.connect(FormInsertRowValue.accept)
        self.pushButtonCancel.clicked.connect(FormInsertRowValue.reject)
        self.checkBoxFormat.toggled['bool'].connect(self.comboBoxFormat.setDisabled)
        self.radioPrevContinuity.toggled['bool'].connect(self.lineAddrStart.setDisabled)
        self.comboBoxFormat.activated['QString'].connect(FormInsertRowValue.slotUpdateAddressesLength)
        self.checkBoxFormat.toggled['bool'].connect(FormInsertRowValue.slotAutoFormatToggled)
        self.radioNextContinuity.toggled['bool'].connect(self.lineAddrStart.setDisabled)
        self.radioExplicitAddr.toggled['bool'].connect(self.lineAddrStart.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(FormInsertRowValue)

    def retranslateUi(self, FormInsertRowValue):
        _translate = QtCore.QCoreApplication.translate
        FormInsertRowValue.setWindowTitle(_translate('FormInsertRowValue', 'Value for rows'))
        self.groupFormat_2.setTitle(_translate('FormInsertRowValue', 'Number of lines to insert'))
        self.groupFormat.setTitle(_translate('FormInsertRowValue', 'Line format'))
        self.checkBoxFormat.setText(_translate('FormInsertRowValue', 'Auto'))
        self.comboBoxFormat.setItemText(0, _translate('FormInsertRowValue', 'S19'))
        self.comboBoxFormat.setItemText(1, _translate('FormInsertRowValue', 'S28'))
        self.comboBoxFormat.setItemText(2, _translate('FormInsertRowValue', 'S37'))
        self.buttonGroupAddress.setTitle(_translate('FormInsertRowValue', 'Addresses'))
        self.radioPrevContinuity.setText(_translate('FormInsertRowValue', 'Continuity with previous data'))
        self.radioNextContinuity.setText(_translate('FormInsertRowValue', 'Continuity with next data'))
        self.radioExplicitAddr.setText(_translate('FormInsertRowValue', 'Set base address'))
        self.lineAddrStart.setText(_translate('FormInsertRowValue', '0000'))
        self.groupData.setTitle(_translate('FormInsertRowValue', 'Row default data'))
        self.label.setText(_translate('FormInsertRowValue', 'Data length (bytes)'))
        self.label_2.setText(_translate('FormInsertRowValue', 'Data content'))
        self.lineEditData.setText(_translate('FormInsertRowValue', '00000000000000000000000000000000'))
        self.pushButtonOK.setText(_translate('FormInsertRowValue', 'Ok'))
        self.pushButtonCancel.setText(_translate('FormInsertRowValue', 'Cancel'))
