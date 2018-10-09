# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui_main_form.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(686, 572)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainForm.sizePolicy().hasHeightForWidth())
        MainForm.setSizePolicy(sizePolicy)
        MainForm.setBaseSize(QtCore.QSize(800, 600))
        MainForm.setWindowTitle("")
        MainForm.setProperty("usesTextLabel", True)
        MainForm.setProperty("opaqueMoving", True)
        self.widget = QtWidgets.QWidget(MainForm)
        self.widget.setObjectName("widget")
        MainForm.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(MainForm)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 686, 21))
        self.menubar.setObjectName("menubar")
        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.setObjectName("fileMenu")
        self.menuOpenRecent = QtWidgets.QMenu(self.fileMenu)
        self.menuOpenRecent.setObjectName("menuOpenRecent")
        self.editMenu = QtWidgets.QMenu(self.menubar)
        self.editMenu.setObjectName("editMenu")
        self.linesMenu = QtWidgets.QMenu(self.menubar)
        self.linesMenu.setObjectName("linesMenu")
        self.helpMenu = QtWidgets.QMenu(self.menubar)
        self.helpMenu.setObjectName("helpMenu")
        MainForm.setMenuBar(self.menubar)
        self.openAction = QtWidgets.QAction(MainForm)
        self.openAction.setProperty("name", "openAction")
        self.openAction.setObjectName("openAction")
        self.insertAction = QtWidgets.QAction(MainForm)
        self.insertAction.setEnabled(False)
        self.insertAction.setProperty("name", "insertAction")
        self.insertAction.setObjectName("insertAction")
        self.saveAction = QtWidgets.QAction(MainForm)
        self.saveAction.setEnabled(False)
        self.saveAction.setProperty("name", "saveAction")
        self.saveAction.setObjectName("saveAction")
        self.saveasAction = QtWidgets.QAction(MainForm)
        self.saveasAction.setEnabled(False)
        self.saveasAction.setProperty("name", "saveasAction")
        self.saveasAction.setObjectName("saveasAction")
        self.closeAction = QtWidgets.QAction(MainForm)
        self.closeAction.setEnabled(False)
        self.closeAction.setProperty("name", "closeAction")
        self.closeAction.setObjectName("closeAction")
        self.quitAction = QtWidgets.QAction(MainForm)
        self.quitAction.setProperty("name", "quitAction")
        self.quitAction.setObjectName("quitAction")
        self.copyAction = QtWidgets.QAction(MainForm)
        self.copyAction.setEnabled(False)
        self.copyAction.setProperty("name", "copyAction")
        self.copyAction.setObjectName("copyAction")
        self.cutAction = QtWidgets.QAction(MainForm)
        self.cutAction.setEnabled(False)
        self.cutAction.setProperty("name", "cutAction")
        self.cutAction.setObjectName("cutAction")
        self.pasteAction = QtWidgets.QAction(MainForm)
        self.pasteAction.setEnabled(False)
        self.pasteAction.setProperty("name", "pasteAction")
        self.pasteAction.setObjectName("pasteAction")
        self.deleteAction = QtWidgets.QAction(MainForm)
        self.deleteAction.setEnabled(False)
        self.deleteAction.setProperty("name", "deleteAction")
        self.deleteAction.setObjectName("deleteAction")
        self.selectallAction = QtWidgets.QAction(MainForm)
        self.selectallAction.setEnabled(False)
        self.selectallAction.setProperty("name", "selectallAction")
        self.selectallAction.setObjectName("selectallAction")
        self.convertToAction = QtWidgets.QAction(MainForm)
        self.convertToAction.setEnabled(False)
        self.convertToAction.setProperty("name", "convertToAction")
        self.convertToAction.setObjectName("convertToAction")
        self.insertRowAction = QtWidgets.QAction(MainForm)
        self.insertRowAction.setEnabled(False)
        self.insertRowAction.setProperty("name", "insertRowAction")
        self.insertRowAction.setObjectName("insertRowAction")
        self.deleteRowAction = QtWidgets.QAction(MainForm)
        self.deleteRowAction.setEnabled(False)
        self.deleteRowAction.setProperty("name", "deleteRowAction")
        self.deleteRowAction.setObjectName("deleteRowAction")
        self.editDataAction = QtWidgets.QAction(MainForm)
        self.editDataAction.setEnabled(False)
        self.editDataAction.setProperty("name", "editDataAction")
        self.editDataAction.setObjectName("editDataAction")
        self.convertToS19Action = QtWidgets.QAction(MainForm)
        self.convertToS19Action.setEnabled(False)
        self.convertToS19Action.setProperty("name", "convertToS19Action")
        self.convertToS19Action.setObjectName("convertToS19Action")
        self.convertToS28Action = QtWidgets.QAction(MainForm)
        self.convertToS28Action.setEnabled(False)
        self.convertToS28Action.setProperty("name", "convertToS28Action")
        self.convertToS28Action.setObjectName("convertToS28Action")
        self.convertToS37Action = QtWidgets.QAction(MainForm)
        self.convertToS37Action.setEnabled(False)
        self.convertToS37Action.setProperty("name", "convertToS37Action")
        self.convertToS37Action.setObjectName("convertToS37Action")
        self.applyOffsetAction = QtWidgets.QAction(MainForm)
        self.applyOffsetAction.setEnabled(False)
        self.applyOffsetAction.setProperty("name", "applyOffsetAction")
        self.applyOffsetAction.setObjectName("applyOffsetAction")
        self.helpAboutAction = QtWidgets.QAction(MainForm)
        self.helpAboutAction.setProperty("name", "helpAboutAction")
        self.helpAboutAction.setObjectName("helpAboutAction")
        self.splitRowAction = QtWidgets.QAction(MainForm)
        self.splitRowAction.setChecked(False)
        self.splitRowAction.setEnabled(False)
        self.splitRowAction.setProperty("name", "splitRowAction")
        self.splitRowAction.setObjectName("splitRowAction")
        self.mergeRowsAction = QtWidgets.QAction(MainForm)
        self.mergeRowsAction.setEnabled(False)
        self.mergeRowsAction.setProperty("name", "mergeRowsAction")
        self.mergeRowsAction.setObjectName("mergeRowsAction")
        self.setRowSizeAction = QtWidgets.QAction(MainForm)
        self.setRowSizeAction.setEnabled(False)
        self.setRowSizeAction.setProperty("name", "setRowSizeAction")
        self.setRowSizeAction.setObjectName("setRowSizeAction")
        self.action = QtWidgets.QAction(MainForm)
        self.action.setText("")
        self.action.setObjectName("action")
        self.xorRowAction = QtWidgets.QAction(MainForm)
        self.xorRowAction.setEnabled(False)
        self.xorRowAction.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.xorRowAction.setObjectName("xorRowAction")
        self.flipBitsAction = QtWidgets.QAction(MainForm)
        self.flipBitsAction.setEnabled(False)
        self.flipBitsAction.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.flipBitsAction.setObjectName("flipBitsAction")
        self.recalculateChecksumAction = QtWidgets.QAction(MainForm)
        self.recalculateChecksumAction.setObjectName("recalculateChecksumAction")
        self.verifyChecksumAction = QtWidgets.QAction(MainForm)
        self.verifyChecksumAction.setObjectName("verifyChecksumAction")
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.menuOpenRecent.menuAction())
        self.fileMenu.addAction(self.insertAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.saveasAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.quitAction)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.cutAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addAction(self.deleteAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.selectallAction)
        self.linesMenu.addAction(self.convertToS19Action)
        self.linesMenu.addAction(self.convertToS28Action)
        self.linesMenu.addAction(self.convertToS37Action)
        self.linesMenu.addAction(self.insertRowAction)
        self.linesMenu.addAction(self.deleteRowAction)
        self.linesMenu.addAction(self.editDataAction)
        self.linesMenu.addAction(self.applyOffsetAction)
        self.linesMenu.addAction(self.verifyChecksumAction)
        self.linesMenu.addAction(self.recalculateChecksumAction)
        self.linesMenu.addAction(self.splitRowAction)
        self.linesMenu.addAction(self.mergeRowsAction)
        self.linesMenu.addAction(self.setRowSizeAction)
        self.linesMenu.addAction(self.xorRowAction)
        self.linesMenu.addAction(self.flipBitsAction)
        self.helpMenu.addAction(self.helpAboutAction)
        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.editMenu.menuAction())
        self.menubar.addAction(self.linesMenu.menuAction())
        self.menubar.addAction(self.helpMenu.menuAction())

        self.retranslateUi(MainForm)
        self.openAction.triggered.connect(MainForm.slotOpen)
        self.insertAction.triggered.connect(MainForm.slotInsert)
        self.saveAction.triggered.connect(MainForm.slotSave)
        self.saveasAction.triggered.connect(MainForm.slotSaveAs)
        self.quitAction.triggered.connect(MainForm.slotQuit)
        self.copyAction.triggered.connect(MainForm.slotCopy)
        self.cutAction.triggered.connect(MainForm.slotCut)
        self.pasteAction.triggered.connect(MainForm.slotPaste)
        self.deleteAction.triggered.connect(MainForm.slotDelete)
        self.selectallAction.triggered.connect(MainForm.slotSelectAll)
        self.deleteRowAction.triggered.connect(MainForm.slotDeleteRow)
        self.editDataAction.triggered.connect(MainForm.slotEditData)
        self.applyOffsetAction.triggered.connect(MainForm.slotApplyOffset)
        self.convertToS19Action.triggered.connect(MainForm.slotConvertToS19)
        self.convertToS28Action.triggered.connect(MainForm.slotConvertToS28)
        self.convertToS37Action.triggered.connect(MainForm.slotConvertToS37)
        self.insertRowAction.triggered.connect(MainForm.slotInsertRow)
        self.helpAboutAction.triggered.connect(MainForm.slotAbout)
        self.setRowSizeAction.triggered.connect(MainForm.slotSetRowSize)
        self.splitRowAction.triggered.connect(MainForm.slotSplitRow)
        self.mergeRowsAction.triggered.connect(MainForm.slotMergeRows)
        self.xorRowAction.triggered.connect(MainForm.slotXorRow)
        self.flipBitsAction.triggered.connect(MainForm.slotFlipBits)
        self.verifyChecksumAction.triggered.connect(MainForm.slotVerifyChecksum)
        self.recalculateChecksumAction.triggered.connect(MainForm.slotRecalculateChecksum)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        self.fileMenu.setTitle(_translate("MainForm", "File"))
        self.menuOpenRecent.setTitle(_translate("MainForm", "Open Recent"))
        self.editMenu.setTitle(_translate("MainForm", "Edit"))
        self.linesMenu.setTitle(_translate("MainForm", "Lines"))
        self.helpMenu.setTitle(_translate("MainForm", "About"))
        self.openAction.setText(_translate("MainForm", "Open"))
        self.openAction.setIconText(_translate("MainForm", "Open"))
        self.openAction.setShortcut(_translate("MainForm", "Ctrl+Shift+O"))
        self.insertAction.setText(_translate("MainForm", "Insert"))
        self.insertAction.setIconText(_translate("MainForm", "Insert"))
        self.saveAction.setText(_translate("MainForm", "Save"))
        self.saveAction.setIconText(_translate("MainForm", "Save"))
        self.saveAction.setShortcut(_translate("MainForm", "Ctrl+S"))
        self.saveasAction.setText(_translate("MainForm", "Save As"))
        self.saveasAction.setIconText(_translate("MainForm", "Save As"))
        self.saveasAction.setShortcut(_translate("MainForm", "Ctrl+Shift+S"))
        self.closeAction.setText(_translate("MainForm", "Close"))
        self.closeAction.setIconText(_translate("MainForm", "Close"))
        self.closeAction.setShortcut(_translate("MainForm", "Ctrl+W"))
        self.quitAction.setText(_translate("MainForm", "Quit"))
        self.quitAction.setIconText(_translate("MainForm", "Quit"))
        self.quitAction.setShortcut(_translate("MainForm", "Ctrl+Q"))
        self.copyAction.setText(_translate("MainForm", "Copy"))
        self.copyAction.setIconText(_translate("MainForm", "Copy"))
        self.copyAction.setShortcut(_translate("MainForm", "Ctrl+C"))
        self.cutAction.setText(_translate("MainForm", "Cut"))
        self.cutAction.setIconText(_translate("MainForm", "Cut"))
        self.cutAction.setShortcut(_translate("MainForm", "Ctrl+X"))
        self.pasteAction.setText(_translate("MainForm", "Paste"))
        self.pasteAction.setIconText(_translate("MainForm", "Paste"))
        self.pasteAction.setShortcut(_translate("MainForm", "Ctrl+V"))
        self.deleteAction.setText(_translate("MainForm", "Delete"))
        self.deleteAction.setIconText(_translate("MainForm", "Delete"))
        self.selectallAction.setText(_translate("MainForm", "Select All"))
        self.selectallAction.setIconText(_translate("MainForm", "Select All"))
        self.selectallAction.setShortcut(_translate("MainForm", "Ctrl+A"))
        self.convertToAction.setText(_translate("MainForm", "Convert to ..."))
        self.convertToAction.setIconText(_translate("MainForm", "Convert to ..."))
        self.convertToAction.setShortcut(_translate("MainForm", "Ctrl+T"))
        self.insertRowAction.setText(_translate("MainForm", "Insert row"))
        self.insertRowAction.setIconText(_translate("MainForm", "Insert row"))
        self.insertRowAction.setShortcut(_translate("MainForm", "Ctrl+I"))
        self.deleteRowAction.setText(_translate("MainForm", "Delete Row"))
        self.deleteRowAction.setIconText(_translate("MainForm", "Delete Row"))
        self.deleteRowAction.setShortcut(_translate("MainForm", "Del"))
        self.editDataAction.setText(_translate("MainForm", "Edit data"))
        self.editDataAction.setIconText(_translate("MainForm", "Edit data"))
        self.editDataAction.setShortcut(_translate("MainForm", "Ctrl+E"))
        self.convertToS19Action.setIconText(_translate("MainForm", "convert to S19"))
        self.convertToS19Action.setToolTip(_translate("MainForm", "Convert selected lines to format S19"))
        self.convertToS19Action.setShortcut(_translate("MainForm", "Ctrl+1"))
        self.convertToS28Action.setIconText(_translate("MainForm", "convert to S28"))
        self.convertToS28Action.setToolTip(_translate("MainForm", "Convert selected lines to format S28"))
        self.convertToS28Action.setShortcut(_translate("MainForm", "Ctrl+Shift+2"))
        self.convertToS37Action.setIconText(_translate("MainForm", "convert to S37"))
        self.convertToS37Action.setToolTip(_translate("MainForm", "Convert selected lines to format S37"))
        self.convertToS37Action.setShortcut(_translate("MainForm", "Ctrl+3"))
        self.applyOffsetAction.setIconText(_translate("MainForm", "Apply offset on addresses"))
        self.applyOffsetAction.setToolTip(_translate("MainForm", "Apply offset on addresses of lines selected"))
        self.applyOffsetAction.setShortcut(_translate("MainForm", "Ctrl+O"))
        self.helpAboutAction.setIconText(_translate("MainForm", "About"))
        self.splitRowAction.setIconText(_translate("MainForm", "Split Row"))
        self.splitRowAction.setShortcut(_translate("MainForm", "Ctrl+D"))
        self.mergeRowsAction.setIconText(_translate("MainForm", "Merge Rows"))
        self.mergeRowsAction.setShortcut(_translate("MainForm", "Ctrl+M"))
        self.setRowSizeAction.setIconText(_translate("MainForm", "Set Row Size"))
        self.setRowSizeAction.setShortcut(_translate("MainForm", "Ctrl+R"))
        self.xorRowAction.setText(_translate("MainForm", "XOR Row(s)"))
        self.xorRowAction.setShortcut(_translate("MainForm", "Ctrl+X"))
        self.flipBitsAction.setText(_translate("MainForm", "Flip Bits"))
        self.flipBitsAction.setShortcut(_translate("MainForm", "Ctrl+F"))
        self.recalculateChecksumAction.setText(_translate("MainForm", "Recalculate Checksum"))
        self.recalculateChecksumAction.setShortcut(_translate("MainForm", "Ctrl+Shift+C"))
        self.verifyChecksumAction.setText(_translate("MainForm", "Verify Checksum"))
        self.verifyChecksumAction.setShortcut(_translate("MainForm", "Ctrl+Shift+V"))

