

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowSystem(object):
    def setupUi(self, MainWindowSystem):
        MainWindowSystem.setObjectName("MainWindowSystem")
        MainWindowSystem.resize(1326, 668)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindowSystem.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/video_call_32px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowSystem.setWindowIcon(icon)
        MainWindowSystem.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindowSystem)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_manage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_manage.setGeometry(QtCore.QRect(20, 60, 101, 41))
        self.pushButton_manage.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/people_64px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_manage.setIcon(icon1)
        self.pushButton_manage.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_manage.setObjectName("pushButton_manage")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 101, 16))
        self.label.setObjectName("label")
        self.pushButton_dataset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dataset.setGeometry(QtCore.QRect(20, 130, 101, 41))
        self.pushButton_dataset.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/settings_64px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_dataset.setIcon(icon2)
        self.pushButton_dataset.setIconSize(QtCore.QSize(39, 39))
        self.pushButton_dataset.setObjectName("pushButton_dataset")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 101, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_3_face = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3_face.setGeometry(QtCore.QRect(20, 210, 101, 41))
        self.pushButton_3_face.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/face_id_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3_face.setIcon(icon3)
        self.pushButton_3_face.setIconSize(QtCore.QSize(39, 39))
        self.pushButton_3_face.setObjectName("pushButton_3_face")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 101, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_4_attendance = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4_attendance.setGeometry(QtCore.QRect(20, 280, 101, 41))
        self.pushButton_4_attendance.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/microsoft_excel_26px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4_attendance.setIcon(icon4)
        self.pushButton_4_attendance.setIconSize(QtCore.QSize(39, 39))
        self.pushButton_4_attendance.setObjectName("pushButton_4_attendance")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 260, 101, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_6_developer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6_developer.setGeometry(QtCore.QRect(20, 350, 101, 41))
        self.pushButton_6_developer.setObjectName("pushButton_6_developer")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 420, 101, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(150, 40, 1151, 611))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 451, 531))
        self.groupBox.setMaximumSize(QtCore.QSize(16777194, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_fullname = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_fullname.setGeometry(QtCore.QRect(120, 20, 281, 20))
        self.lineEdit_fullname.setObjectName("lineEdit_fullname")
        self.lineEdit_2_reg_no = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2_reg_no.setGeometry(QtCore.QRect(120, 70, 281, 20))
        self.lineEdit_2_reg_no.setObjectName("lineEdit_2_reg_no")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_contacts = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_contacts.setGeometry(QtCore.QRect(120, 120, 281, 20))
        self.lineEdit_contacts.setObjectName("lineEdit_contacts")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 120, 101, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 220, 101, 21))
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(10, 270, 101, 21))
        self.label_13.setObjectName("label_13")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(10, 320, 101, 21))
        self.label_15.setObjectName("label_15")
        self.comboBox_Course = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_Course.setGeometry(QtCore.QRect(120, 220, 281, 22))
        self.comboBox_Course.setObjectName("comboBox_Course")
        self.comboBox_School = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_School.setGeometry(QtCore.QRect(120, 270, 281, 22))
        self.comboBox_School.setObjectName("comboBox_School")
        self.comboBox_School.addItem("")
        self.comboBox_School.addItem("")
        self.comboBox_School.addItem("")
        self.comboBox_School.addItem("")
        self.comboBox_School.addItem("")
        self.comboBox_gender = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_gender.setGeometry(QtCore.QRect(120, 320, 281, 22))
        self.comboBox_gender.setObjectName("comboBox_gender")
        self.comboBox_gender.addItem("")
        self.comboBox_gender.addItem("")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(10, 410, 101, 21))
        self.label_16.setObjectName("label_16")
        self.pushButton_load_images = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_load_images.setGeometry(QtCore.QRect(120, 410, 111, 23))
        self.pushButton_load_images.setObjectName("pushButton_load_images")
        self.label_27 = QtWidgets.QLabel(self.groupBox)
        self.label_27.setGeometry(QtCore.QRect(11, 370, 101, 21))
        self.label_27.setObjectName("label_27")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 170, 101, 21))
        self.label_12.setObjectName("label_12")
        self.comboBox_Level = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_Level.setGeometry(QtCore.QRect(120, 170, 281, 22))
        self.comboBox_Level.setObjectName("comboBox_Level")
        self.dateEdit_dob = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit_dob.setGeometry(QtCore.QRect(120, 370, 281, 22))
        self.dateEdit_dob.setObjectName("dateEdit_dob")
        self.label_pix_img = QtWidgets.QLabel(self.groupBox)
        self.label_pix_img.setGeometry(QtCore.QRect(250, 410, 171, 91))
        self.label_pix_img.setMaximumSize(QtCore.QSize(200, 200))
        self.label_pix_img.setText("")
        self.label_pix_img.setObjectName("label_pix_img")
        self.label_6_input_error = QtWidgets.QLabel(self.groupBox)
        self.label_6_input_error.setGeometry(QtCore.QRect(20, 510, 361, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_6_input_error.setFont(font)
        self.label_6_input_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_6_input_error.setText("")
        self.label_6_input_error.setObjectName("label_6_input_error")
        self.pushButton_add_student = QtWidgets.QPushButton(self.tab)
        self.pushButton_add_student.setGeometry(QtCore.QRect(10, 550, 71, 31))
        self.pushButton_add_student.setObjectName("pushButton_add_student")
        self.pushButton_10_update = QtWidgets.QPushButton(self.tab)
        self.pushButton_10_update.setGeometry(QtCore.QRect(130, 550, 71, 31))
        self.pushButton_10_update.setObjectName("pushButton_10_update")
        self.pushButton_delete = QtWidgets.QPushButton(self.tab)
        self.pushButton_delete.setGeometry(QtCore.QRect(250, 550, 71, 31))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_clear = QtWidgets.QPushButton(self.tab)
        self.pushButton_clear.setGeometry(QtCore.QRect(370, 550, 71, 31))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(480, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.lineEdit_4_search = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4_search.setGeometry(QtCore.QRect(602, 30, 251, 31))
        self.lineEdit_4_search.setObjectName("lineEdit_4_search")
        self.pushButton_show_all = QtWidgets.QPushButton(self.tab)
        self.pushButton_show_all.setGeometry(QtCore.QRect(890, 30, 121, 31))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/refresh_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_show_all.setIcon(icon5)
        self.pushButton_show_all.setObjectName("pushButton_show_all")
        self.tableWidget_student_data = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_student_data.setGeometry(QtCore.QRect(450, 80, 741, 501))
        self.tableWidget_student_data.setObjectName("tableWidget_student_data")
        self.tableWidget_student_data.setColumnCount(8)
        self.tableWidget_student_data.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_student_data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_student_data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_student_data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_student_data.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_student_data.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_student_data.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_student_data.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_student_data.setHorizontalHeaderItem(7, item)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(20, 10, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.pushButton_stat_training = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_stat_training.setGeometry(QtCore.QRect(30, 170, 91, 23))
        self.pushButton_stat_training.setObjectName("pushButton_stat_training")
        self.label_6_training_progress = QtWidgets.QLabel(self.tab_2)
        self.label_6_training_progress.setGeometry(QtCore.QRect(30, 230, 401, 16))
        self.label_6_training_progress.setStyleSheet("color: rgb(85, 255, 0);")
        self.label_6_training_progress.setText("")
        self.label_6_training_progress.setObjectName("label_6_training_progress")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(30, 20, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_6_camera = QtWidgets.QLabel(self.tab_3)
        self.label_6_camera.setGeometry(QtCore.QRect(30, 70, 541, 401))
        self.label_6_camera.setText("")
        self.label_6_camera.setObjectName("label_6_camera")
        self.pushButton_start_face = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_start_face.setGeometry(QtCore.QRect(30, 500, 111, 31))
        self.pushButton_start_face.setObjectName("pushButton_start_face")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(170, 500, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 321, 511))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(10, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(10, 120, 101, 16))
        self.label_21.setObjectName("label_21")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 70, 151, 20))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.label_22.setObjectName("label_22")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(160, 170, 151, 20))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setGeometry(QtCore.QRect(10, 170, 101, 16))
        self.label_23.setObjectName("label_23")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 120, 151, 20))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_16.setGeometry(QtCore.QRect(200, 230, 71, 31))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_17.setGeometry(QtCore.QRect(10, 230, 71, 31))
        self.pushButton_17.setObjectName("pushButton_17")
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        self.label_24.setGeometry(QtCore.QRect(10, 290, 151, 31))
        self.label_24.setObjectName("label_24")
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_18.setGeometry(QtCore.QRect(10, 330, 71, 31))
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_25 = QtWidgets.QLabel(self.groupBox_2)
        self.label_25.setGeometry(QtCore.QRect(10, 390, 151, 31))
        self.label_25.setObjectName("label_25")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_19.setGeometry(QtCore.QRect(10, 430, 71, 31))
        self.pushButton_19.setObjectName("pushButton_19")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(502, 10, 181, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_26 = QtWidgets.QLabel(self.tab_4)
        self.label_26.setGeometry(QtCore.QRect(380, 20, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_20.setGeometry(QtCore.QRect(700, 10, 75, 31))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_21.setGeometry(QtCore.QRect(820, 10, 75, 31))
        self.pushButton_21.setObjectName("pushButton_21")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_2.setGeometry(QtCore.QRect(380, 60, 701, 461))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.label_6_time = QtWidgets.QLabel(self.centralwidget)
        self.label_6_time.setGeometry(QtCore.QRect(410, 0, 291, 31))
        self.label_6_time.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_6_time.setText("")
        self.label_6_time.setObjectName("label_6_time")
        self.label_6_time_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_6_time_2.setGeometry(QtCore.QRect(760, 0, 291, 31))
        self.label_6_time_2.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_6_time_2.setText("")
        self.label_6_time_2.setObjectName("label_6_time_2")
        MainWindowSystem.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowSystem)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1326, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindowSystem.setMenuBar(self.menubar)
        self.actionView_Attendance = QtWidgets.QAction(MainWindowSystem)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/report_file_32px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionView_Attendance.setIcon(icon6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.actionView_Attendance.setFont(font)
        self.actionView_Attendance.setObjectName("actionView_Attendance")
        self.actionExport_to_Excel = QtWidgets.QAction(MainWindowSystem)
        self.actionExport_to_Excel.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.actionExport_to_Excel.setFont(font)
        self.actionExport_to_Excel.setObjectName("actionExport_to_Excel")
        self.actionExport_to_CSV = QtWidgets.QAction(MainWindowSystem)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/csv_40px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport_to_CSV.setIcon(icon7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.actionExport_to_CSV.setFont(font)
        self.actionExport_to_CSV.setObjectName("actionExport_to_CSV")
        self.actionPrint = QtWidgets.QAction(MainWindowSystem)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/print_32px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon8)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.actionPrint.setFont(font)
        self.actionPrint.setObjectName("actionPrint")
        self.actionQuit = QtWidgets.QAction(MainWindowSystem)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/exit_32px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.actionQuit.setFont(font)
        self.actionQuit.setObjectName("actionQuit")
        self.actionShow_all_data = QtWidgets.QAction(MainWindowSystem)
        self.actionShow_all_data.setObjectName("actionShow_all_data")
        self.actionToolbars = QtWidgets.QAction(MainWindowSystem)
        self.actionToolbars.setCheckable(True)
        self.actionToolbars.setObjectName("actionToolbars")
        self.actionReport_a_bug = QtWidgets.QAction(MainWindowSystem)
        self.actionReport_a_bug.setObjectName("actionReport_a_bug")
        self.actionMake_Suggestions = QtWidgets.QAction(MainWindowSystem)
        self.actionMake_Suggestions.setObjectName("actionMake_Suggestions")
        self.actionFacial_Recognition_Software = QtWidgets.QAction(MainWindowSystem)
        self.actionFacial_Recognition_Software.setObjectName("actionFacial_Recognition_Software")
        self.actionDeveloper = QtWidgets.QAction(MainWindowSystem)
        self.actionDeveloper.setObjectName("actionDeveloper")
        self.actionManual_usage = QtWidgets.QAction(MainWindowSystem)
        self.actionManual_usage.setObjectName("actionManual_usage")
        self.menuFile.addAction(self.actionView_Attendance)
        self.menuFile.addAction(self.actionExport_to_Excel)
        self.menuFile.addAction(self.actionExport_to_CSV)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionQuit)
        self.menuView.addAction(self.actionShow_all_data)
        self.menuView.addAction(self.actionToolbars)
        self.menuAbout.addAction(self.actionFacial_Recognition_Software)
        self.menuAbout.addAction(self.actionDeveloper)
        self.menuHelp.addAction(self.actionReport_a_bug)
        self.menuHelp.addAction(self.actionMake_Suggestions)
        self.menuHelp.addAction(self.actionManual_usage)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindowSystem)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindowSystem)

    def retranslateUi(self, MainWindowSystem):
        _translate = QtCore.QCoreApplication.translate
        MainWindowSystem.setWindowTitle(_translate("MainWindowSystem", "Mirrorlane"))
        self.label.setText(_translate("MainWindowSystem", "Manage Students"))
        self.label_2.setText(_translate("MainWindowSystem", "Train Dataset"))
        self.label_3.setText(_translate("MainWindowSystem", "Facial Recognition"))
        self.label_4.setText(_translate("MainWindowSystem", "Attendance Report"))
        self.pushButton_6_developer.setText(_translate("MainWindowSystem", "Developer"))
        self.pushButton_7.setText(_translate("MainWindowSystem", "Exit"))
        self.groupBox.setTitle(_translate("MainWindowSystem", "ADD STUDENTS"))
        self.label_8.setText(_translate("MainWindowSystem", "FullName"))
        self.lineEdit_fullname.setPlaceholderText(_translate("MainWindowSystem", "Fullname.."))
        self.lineEdit_2_reg_no.setPlaceholderText(_translate("MainWindowSystem", "CT100/G/0000/17"))
        self.label_9.setText(_translate("MainWindowSystem", "Reg No"))
        self.lineEdit_contacts.setPlaceholderText(_translate("MainWindowSystem", "Mobile No"))
        self.label_10.setText(_translate("MainWindowSystem", "Contactas"))
        self.label_11.setText(_translate("MainWindowSystem", "Course"))
        self.label_13.setText(_translate("MainWindowSystem", "School"))
        self.label_15.setText(_translate("MainWindowSystem", "Gender"))
        self.comboBox_School.setItemText(0, _translate("MainWindowSystem", "School of Business And Economics"))
        self.comboBox_School.setItemText(1, _translate("MainWindowSystem", "School of Health Sciences"))
        self.comboBox_School.setItemText(2, _translate("MainWindowSystem", "School of Pure And Applied Sciences"))
        self.comboBox_School.setItemText(3, _translate("MainWindowSystem", "School of Engineering And Built Environment"))
        self.comboBox_School.setItemText(4, _translate("MainWindowSystem", "School of Hospitality and Textile Technology"))
        self.comboBox_gender.setItemText(0, _translate("MainWindowSystem", "Male"))
        self.comboBox_gender.setItemText(1, _translate("MainWindowSystem", "Female"))
        self.label_16.setText(_translate("MainWindowSystem", "Images"))
        self.pushButton_load_images.setText(_translate("MainWindowSystem", "Load Images"))
        self.label_27.setText(_translate("MainWindowSystem", "Dob"))
        self.label_12.setText(_translate("MainWindowSystem", "Level"))
        self.pushButton_add_student.setText(_translate("MainWindowSystem", "Add"))
        self.pushButton_10_update.setText(_translate("MainWindowSystem", "Update"))
        self.pushButton_delete.setText(_translate("MainWindowSystem", "Delete"))
        self.pushButton_clear.setText(_translate("MainWindowSystem", "Clear"))
        self.label_17.setText(_translate("MainWindowSystem", "Search Student"))
        self.lineEdit_4_search.setPlaceholderText(_translate("MainWindowSystem", "RegNo...."))
        self.pushButton_show_all.setText(_translate("MainWindowSystem", "Show All"))
        item = self.tableWidget_student_data.horizontalHeaderItem(0)
        item.setText(_translate("MainWindowSystem", "Fullname"))
        item = self.tableWidget_student_data.horizontalHeaderItem(1)
        item.setText(_translate("MainWindowSystem", "RegNo"))
        item = self.tableWidget_student_data.horizontalHeaderItem(2)
        item.setText(_translate("MainWindowSystem", "Contacts"))
        item = self.tableWidget_student_data.horizontalHeaderItem(3)
        item.setText(_translate("MainWindowSystem", "Level"))
        item = self.tableWidget_student_data.horizontalHeaderItem(4)
        item.setText(_translate("MainWindowSystem", "Course"))
        item = self.tableWidget_student_data.horizontalHeaderItem(5)
        item.setText(_translate("MainWindowSystem", "School"))
        item = self.tableWidget_student_data.horizontalHeaderItem(6)
        item.setText(_translate("MainWindowSystem", "Gender"))
        item = self.tableWidget_student_data.horizontalHeaderItem(7)
        item.setText(_translate("MainWindowSystem", "DOB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindowSystem", "Tab 1"))
        self.label_18.setText(_translate("MainWindowSystem", "Train the system"))
        self.pushButton_stat_training.setText(_translate("MainWindowSystem", "Start Training"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindowSystem", "Tab 2"))
        self.label_19.setText(_translate("MainWindowSystem", "Load Recognizer"))
        self.pushButton_start_face.setText(_translate("MainWindowSystem", "start"))
        self.pushButton.setText(_translate("MainWindowSystem", "cool btn"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindowSystem", "Page"))
        self.groupBox_2.setTitle(_translate("MainWindowSystem", "Attendance Info"))
        self.label_20.setText(_translate("MainWindowSystem", "View and Update Attendance"))
        self.label_21.setText(_translate("MainWindowSystem", "Reg No"))
        self.label_22.setText(_translate("MainWindowSystem", "FullName"))
        self.label_23.setText(_translate("MainWindowSystem", "Status"))
        self.pushButton_16.setText(_translate("MainWindowSystem", "Clear"))
        self.pushButton_17.setText(_translate("MainWindowSystem", "Update"))
        self.label_24.setText(_translate("MainWindowSystem", "Export to Excel"))
        self.pushButton_18.setText(_translate("MainWindowSystem", "Export"))
        self.label_25.setText(_translate("MainWindowSystem", "Delete Attendance"))
        self.pushButton_19.setText(_translate("MainWindowSystem", "Delete"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindowSystem", "Student Reg No"))
        self.label_26.setText(_translate("MainWindowSystem", "Search Student"))
        self.pushButton_20.setText(_translate("MainWindowSystem", "Search"))
        self.pushButton_21.setText(_translate("MainWindowSystem", "Show All"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindowSystem", "Fullname"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindowSystem", "RegNo"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindowSystem", "Contacts"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindowSystem", "School"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindowSystem", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindowSystem", "Course"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindowSystem", "Gender"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindowSystem", "Dob"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindowSystem", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindowSystem", "Page"))
        self.menuFile.setTitle(_translate("MainWindowSystem", "File"))
        self.menuView.setTitle(_translate("MainWindowSystem", "View"))
        self.menuAbout.setTitle(_translate("MainWindowSystem", "About"))
        self.menuHelp.setTitle(_translate("MainWindowSystem", "Help"))
        self.actionView_Attendance.setText(_translate("MainWindowSystem", "View Attendance"))
        self.actionView_Attendance.setToolTip(_translate("MainWindowSystem", "Preview attendance list"))
        self.actionView_Attendance.setShortcut(_translate("MainWindowSystem", "Ctrl+Shift+A"))
        self.actionExport_to_Excel.setText(_translate("MainWindowSystem", "Export to Excel"))
        self.actionExport_to_Excel.setShortcut(_translate("MainWindowSystem", "Ctrl+E"))
        self.actionExport_to_CSV.setText(_translate("MainWindowSystem", "Export to CSV"))
        self.actionExport_to_CSV.setShortcut(_translate("MainWindowSystem", "Ctrl+R"))
        self.actionPrint.setText(_translate("MainWindowSystem", "Print"))
        self.actionPrint.setShortcut(_translate("MainWindowSystem", "Ctrl+P"))
        self.actionQuit.setText(_translate("MainWindowSystem", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindowSystem", "Ctrl+Q"))
        self.actionShow_all_data.setText(_translate("MainWindowSystem", "Show all data"))
        self.actionToolbars.setText(_translate("MainWindowSystem", "Toolbars"))
        self.actionReport_a_bug.setText(_translate("MainWindowSystem", "Report a bug"))
        self.actionMake_Suggestions.setText(_translate("MainWindowSystem", "Make Suggestions"))
        self.actionFacial_Recognition_Software.setText(_translate("MainWindowSystem", "Facial Recognition Software"))
        self.actionDeveloper.setText(_translate("MainWindowSystem", "Developer"))
        self.actionManual_usage.setText(_translate("MainWindowSystem", "Manual usage"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowSystem = QtWidgets.QMainWindow()
    ui = Ui_MainWindowSystem()
    ui.setupUi(MainWindowSystem)
    MainWindowSystem.show()
    sys.exit(app.exec_())
