# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/luan/Code/python/grape/script/../app/views/qt4/screen/show.ui'
#
# Created: Tue May  3 18:01:06 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ScreenShow(object):
    def setupUi(self, ScreenShow):
        ScreenShow.setObjectName(_fromUtf8("ScreenShow"))
        ScreenShow.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/grape.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ScreenShow.setWindowIcon(icon)
        ScreenShow.setDocumentMode(False)
        ScreenShow.setDockNestingEnabled(False)
        ScreenShow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        ScreenShow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtGui.QWidget(ScreenShow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        ScreenShow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ScreenShow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTearOffEnabled(False)
        self.menuFile.setSeparatorsCollapsible(False)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        ScreenShow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ScreenShow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ScreenShow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(ScreenShow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        ScreenShow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(ScreenShow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/actions/24/gtk-open.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionNew = QtGui.QAction(ScreenShow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/actions/24/gtk-new.svg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionNew.setIcon(icon2)
        self.actionNew.setIconVisibleInMenu(True)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionSave = QtGui.QAction(ScreenShow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/actions/24/gtk-save.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setIconVisibleInMenu(True)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_as = QtGui.QAction(ScreenShow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/actions/24/gtk-save-as.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon4)
        self.actionSave_as.setIconVisibleInMenu(True)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionRever = QtGui.QAction(ScreenShow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/actions/24/gtk-revert-to-saved-rtl.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRever.setIcon(icon5)
        self.actionRever.setIconVisibleInMenu(True)
        self.actionRever.setObjectName(_fromUtf8("actionRever"))
        self.actionClose = QtGui.QAction(ScreenShow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/actions/24/gtk-close.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon6)
        self.actionClose.setIconVisibleInMenu(True)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionQuit = QtGui.QAction(ScreenShow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/actions/24/gtk-quit.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon7)
        self.actionQuit.setIconVisibleInMenu(True)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionUndo = QtGui.QAction(ScreenShow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/actions/24/gtk-undo-ltr.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon8)
        self.actionUndo.setIconVisibleInMenu(True)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionRedo = QtGui.QAction(ScreenShow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/actions/24/gtk-redo-ltr.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon9)
        self.actionRedo.setIconVisibleInMenu(True)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))
        self.actionAdd_vertex = QtGui.QAction(ScreenShow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/actions/24/gtk-add.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_vertex.setIcon(icon10)
        self.actionAdd_vertex.setIconVisibleInMenu(True)
        self.actionAdd_vertex.setObjectName(_fromUtf8("actionAdd_vertex"))
        self.actionRemove_vertex = QtGui.QAction(ScreenShow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/actions/24/gtk-remove.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove_vertex.setIcon(icon11)
        self.actionRemove_vertex.setIconVisibleInMenu(True)
        self.actionRemove_vertex.setObjectName(_fromUtf8("actionRemove_vertex"))
        self.actionAdd_edge = QtGui.QAction(ScreenShow)
        self.actionAdd_edge.setIcon(icon10)
        self.actionAdd_edge.setIconVisibleInMenu(True)
        self.actionAdd_edge.setObjectName(_fromUtf8("actionAdd_edge"))
        self.actionRemove_edge = QtGui.QAction(ScreenShow)
        self.actionRemove_edge.setIcon(icon11)
        self.actionRemove_edge.setIconVisibleInMenu(True)
        self.actionRemove_edge.setObjectName(_fromUtf8("actionRemove_edge"))
        self.actionAlign_vertically = QtGui.QAction(ScreenShow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/actions/24/object-flip-vertical.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlign_vertically.setIcon(icon12)
        self.actionAlign_vertically.setIconVisibleInMenu(True)
        self.actionAlign_vertically.setObjectName(_fromUtf8("actionAlign_vertically"))
        self.actionAlign_horizontally = QtGui.QAction(ScreenShow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/actions/24/object-flip-horizontal.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlign_horizontally.setIcon(icon13)
        self.actionAlign_horizontally.setIconVisibleInMenu(True)
        self.actionAlign_horizontally.setObjectName(_fromUtf8("actionAlign_horizontally"))
        self.actionZoom_in = QtGui.QAction(ScreenShow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/actions/24/gtk-zoom-in.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_in.setIcon(icon14)
        self.actionZoom_in.setIconVisibleInMenu(True)
        self.actionZoom_in.setObjectName(_fromUtf8("actionZoom_in"))
        self.actionZoom_out = QtGui.QAction(ScreenShow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/actions/24/gtk-zoom-out.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_out.setIcon(icon15)
        self.actionZoom_out.setIconVisibleInMenu(True)
        self.actionZoom_out.setObjectName(_fromUtf8("actionZoom_out"))
        self.actionNormal_size = QtGui.QAction(ScreenShow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/actions/24/gtk-zoom-100.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNormal_size.setIcon(icon16)
        self.actionNormal_size.setIconVisibleInMenu(True)
        self.actionNormal_size.setObjectName(_fromUtf8("actionNormal_size"))
        self.actionFullscreen = QtGui.QAction(ScreenShow)
        self.actionFullscreen.setCheckable(True)
        self.actionFullscreen.setIconVisibleInMenu(True)
        self.actionFullscreen.setObjectName(_fromUtf8("actionFullscreen"))
        self.actionAbout = QtGui.QAction(ScreenShow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/actions/24/gtk-about.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon17)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionRever)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionAdd_vertex)
        self.menuEdit.addAction(self.actionRemove_vertex)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionAdd_edge)
        self.menuEdit.addAction(self.actionRemove_edge)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionAlign_vertically)
        self.menuEdit.addAction(self.actionAlign_horizontally)
        self.menuView.addAction(self.actionZoom_in)
        self.menuView.addAction(self.actionZoom_out)
        self.menuView.addAction(self.actionNormal_size)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionFullscreen)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionZoom_in)
        self.toolBar.addAction(self.actionZoom_out)
        self.toolBar.addAction(self.actionNormal_size)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAlign_vertically)
        self.toolBar.addAction(self.actionAlign_horizontally)

        self.retranslateUi(ScreenShow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(ScreenShow)

    def retranslateUi(self, ScreenShow):
        ScreenShow.setWindowTitle(QtGui.QApplication.translate("ScreenShow", "Grape", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("ScreenShow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("ScreenShow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("ScreenShow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("ScreenShow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("ScreenShow", "Show toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("ScreenShow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("ScreenShow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("ScreenShow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("ScreenShow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("ScreenShow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("ScreenShow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("ScreenShow", "Save as...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setShortcut(QtGui.QApplication.translate("ScreenShow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRever.setText(QtGui.QApplication.translate("ScreenShow", "Revert", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("ScreenShow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setShortcut(QtGui.QApplication.translate("ScreenShow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("ScreenShow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("ScreenShow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setText(QtGui.QApplication.translate("ScreenShow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setShortcut(QtGui.QApplication.translate("ScreenShow", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setText(QtGui.QApplication.translate("ScreenShow", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setShortcut(QtGui.QApplication.translate("ScreenShow", "Ctrl+Y", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_vertex.setText(QtGui.QApplication.translate("ScreenShow", "Add vertex", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_vertex.setShortcut(QtGui.QApplication.translate("ScreenShow", "V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_vertex.setText(QtGui.QApplication.translate("ScreenShow", "Remove vertex", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_vertex.setShortcut(QtGui.QApplication.translate("ScreenShow", "Shift+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_edge.setText(QtGui.QApplication.translate("ScreenShow", "Add edge", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_edge.setShortcut(QtGui.QApplication.translate("ScreenShow", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_edge.setText(QtGui.QApplication.translate("ScreenShow", "Remove edge", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_edge.setShortcut(QtGui.QApplication.translate("ScreenShow", "Shift+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlign_vertically.setText(QtGui.QApplication.translate("ScreenShow", "Align vertically", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlign_horizontally.setText(QtGui.QApplication.translate("ScreenShow", "Align horizontally", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_in.setText(QtGui.QApplication.translate("ScreenShow", "Zoom in", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_in.setShortcut(QtGui.QApplication.translate("ScreenShow", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_out.setText(QtGui.QApplication.translate("ScreenShow", "Zoom out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_out.setShortcut(QtGui.QApplication.translate("ScreenShow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNormal_size.setText(QtGui.QApplication.translate("ScreenShow", "Normal size", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNormal_size.setShortcut(QtGui.QApplication.translate("ScreenShow", "Ctrl+0", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFullscreen.setText(QtGui.QApplication.translate("ScreenShow", "Fullscreen", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFullscreen.setShortcut(QtGui.QApplication.translate("ScreenShow", "F11", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("ScreenShow", "About", None, QtGui.QApplication.UnicodeUTF8))

import resources.grape_rc
