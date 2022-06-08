'''
This is the main file that loads and initializes all components for this
applications.

'''

import logging
import csv
import datetime
import os
import sys
import time
import cv2
from PIL import Image
import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox, \
    QMainWindow, QApplication, qApp, QFileDialog, QTableWidgetItem, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor, QStandardItemModel, QStandardItem, QPixmap, QIntValidator
import sqlite3
from splash_screen import Ui_SplashScreen
from welcome import Ui_WelcomeWindow
from login_screen import Ui_LoginWindow
from signup_screen import Ui_CreateAccountWindow
from main_app import Ui_MainWindowSystem

logging.basicConfig(filename='Attendance.log', level=logging.INFO, format='%(message)s',
                    datefmt='%Y-%m-%d %H:%M')


# developer infomation

class Developer(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setFixedWidth(500)
        self.setFixedHeight(250)

        btn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(btn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.accepted.connect(self.reject)

        layout = QVBoxLayout()

        self.setWindowTitle('About')
        title = QLabel('Facial Recognition Software')
        font = title.font()
        font.setPointSize(22)
        title.setFont(font)

        layout.addWidget(title)
        layout.addWidget(QLabel('Version 1.0'))
        layout.addWidget(QLabel('Copyright 2021'))
        layout.addWidget(QLabel('Licence'))

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


class Manual(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setFixedWidth(500)
        self.setFixedHeight(250)

        btn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(btn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.accepted.connect(self.reject)

        layout = QVBoxLayout()

        self.setWindowTitle('Manual')
        title = QLabel('Facial Recognition Software')
        font = title.font()
        font.setPointSize(28)
        title.setFont(font)

        layout.addWidget(title)
        layout.addWidget(QLabel('Version 1.0'))
        layout.addWidget(QLabel(
            'Welcome to the Facial Recognition Software manual \n'
            '1. Add data to the database by filling the form \n'
            '2. Press the add button, which will automatically initialize the camera\n'
            '3. Make sure there is enough light to take images with higher quality\n'
            '4. Closely look at the camera, wait as it takes sample images from the user face\n'
            '5. After successful collection of sample images and saving data to database, \n '
            'click on Train Dataset tab\n'
            '6. Wait as the system trains the recognizer algorithm using the images collected\n'
            '7. Click on Face Recognition tab to start live stream\n'
            '8. The camera will now identify people and display their name and save the record\n'

        ))

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Delete")

        self.setWindowTitle("Delete Student")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.delete_stud)
        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText("ID.")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

        self.delete_stud()

    def delete_stud(self):

        stud_id = self.deleteinput.text()
        if stud_id == '':
            QMessageBox.warning(QMessageBox(), 'Warning!', 'Enter a valid student ID!')
            print('Enter a valid student id')

        elif stud_id != int:
            QMessageBox.warning(QMessageBox(), 'Warning!', 'ID must be a number.')
            print('ID must be a number!')
        else:

            try:
                conn = sqlite3.connect("schooldb.db")
                with conn:
                    cur = conn.cursor()

                    cur.execute("""DELETE from Students WHERE id =?""", stud_id,)
                    conn.commit()
                    QMessageBox.information(QMessageBox(), 'Successful', 'Record deleted Successfully')
                    self.close()
            except Exception as e:
                print(e)

                QMessageBox.warning(QMessageBox(), 'Error', 'Could not Delete student from the database.')


# create main application
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindowSystem()
        self.ui.setupUi(self)

        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
        day, month, year = date.split("-")

        mont = {'01': 'January',
                '02': 'February',
                '03': 'March',
                '04': 'April',
                '05': 'May',
                '06': 'June',
                '07': 'July',
                '08': 'August',
                '09': 'September',
                '10': 'October',
                '11': 'November',
                '12': 'December'
                }

        self.ui.label_6_time.setText(day + '-' + mont[month] + '-' + year + ' | ')

        self.ui_changes()
        self.handle_buttons()

        self.modal = QStandardItemModel()

        # set layout reference
        self.ui.comboBox_Level.setModel(self.modal)
        self.ui.comboBox_Course.setModel(self.modal)

        self.search = self.ui.lineEdit_4_search
        self.search.textChanged.connect(self.search_student)

        # dynamically update combobox items based on selected items
        for k, v in data1.items():
            level = QStandardItem(k)
            self.modal.appendRow(level)
            for value in v:
                course = QStandardItem(value)
                level.appendRow(course)

        self.ui.comboBox_Level.currentIndexChanged.connect(self.update_comboItems_one)
        self.update_comboItems_one(0)

    def update_comboItems_one(self, index):
        indx = self.modal.index(index, 0, self.ui.comboBox_Level.rootModelIndex())
        self.ui.comboBox_Course.setRootModelIndex(indx)
        self.ui.comboBox_Course.setCurrentIndex(0)

    # function to display MainWindow
    def show_main_app(self):
        self.show()

    def ui_changes(self):
        self.ui.tabWidget.tabBar().setVisible(False)

    def handle_buttons(self):
        try:
            self.ui.pushButton_manage.clicked.connect(self.show_manage_students)
            self.ui.pushButton_dataset.clicked.connect(self.show_train_dataset)
            self.ui.pushButton_3_face.clicked.connect(self.show_face_recognizer)
            self.ui.pushButton_4_attendance.clicked.connect(self.show_attendance)
            # self.ui.pushButton_5_images.clicked.connect(self.show_images)
            self.ui.pushButton_6_developer.clicked.connect(self.about)

            self.ui.pushButton_7.clicked.connect(QApplication.instance().quit)
            self.ui.actionQuit.triggered.connect(qApp.quit)
            self.ui.actionDeveloper.triggered.connect(self.about)
            self.ui.actionManual_usage.triggered.connect(self.manual)

            self.ui.pushButton_add_student.clicked.connect(self.add_student)
            self.ui.pushButton_10_update.clicked.connect(self.update_student)
            self.ui.pushButton_show_all.clicked.connect(self.show_all_students)
            # self.ui.pushButton_13_search.clicked.connect(self.search_student)
            self.ui.pushButton_clear.clicked.connect(self.clear_student)
            self.ui.pushButton_delete.clicked.connect(self.delete_student)
            self.ui.pushButton_start_face.clicked.connect(self.start_face_recognizer)
            self.ui.pushButton_stat_training.clicked.connect(self.train_dataset)
        except Exception as e:
            QMessageBox.warning(QMessageBox(), 'Warning!',
                                e)

    def show_manage_students(self):
        self.ui.tabWidget.setCurrentIndex(0)

    def show_train_dataset(self):
        self.ui.tabWidget.setCurrentIndex(1)

    def show_face_recognizer(self):
        self.ui.tabWidget.setCurrentIndex(2)

    def show_attendance(self):
        self.ui.tabWidget.setCurrentIndex(3)

    def about(self):
        dlg = Developer()
        dlg.exec_()

    def manual(self):
        dlg = Manual()
        dlg.exec_()

    def closeEvent(self, event):
        response = QMessageBox.question(self, 'Message', "Are you sure you want to quit? ",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if response == QMessageBox.Yes:
            event.accept()

        else:
            event.ignore()

    # =================== manage students tab ==============================

    
    def add_student(self):
        '''
        this function captures the student details including the images
        :return: Student details
        :param: *args, *kwargs,
        :type: str,numeric, Null=False
        '''
        try:

            name = self.ui.lineEdit_fullname.text()
            reg_no = self.ui.lineEdit_2_reg_no.text()
            contact_no = self.ui.lineEdit_contacts.text()
            academic_level = self.ui.comboBox_Level.currentText()
            academic_course = self.ui.comboBox_Course.currentText()
            academic_school = self.ui.comboBox_School.currentText()
            gender = self.ui.comboBox_gender.currentText()
            dob = self.ui.dateEdit_dob.text()

            if len(name) == 0 or len(reg_no) == 0 or len(contact_no) == 0:
                self.ui.label_6_input_error.setText('All fields are required')
                QMessageBox.warning(QMessageBox(), 'Warning!',
                                    ' Fields missing, please ensure that that all fields are populated with '
                                    'data before proceeding!')

            else:

                conn = sqlite3.connect('schooldb.db')

                if not os.path.exists('./Dataset'):
                    os.makedirs('./Dataset')

                columns = ['SERIAL NO. ', 'ID', '', 'NAME']
                serial = 0
                exists = os.path.isfile('./StudentDetails/StudentDetails.csv')

                if not os.path.exists('./StudentDetails'):
                    os.makedirs('./StudentDetails')
                if exists:
                    with open('StudentDetails/StudentDetails.csv', 'r') as csv_file:
                        reader1 = csv.reader(csv_file)

                        for l in reader1:
                            serial = serial + 1
                    serial = (serial // 2)
                    csv_file.close()
                else:
                    with open('StudentDetails/StudentDetails.csv', 'a+') as csv_file:
                        writer = csv.writer(csv_file)
                        writer.writerow(columns)
                        serial = 1
                    csv_file.close()
                with conn:
                    cur = conn.cursor()

                    faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

                    # create a camera cap object to
                    cap = cv2.VideoCapture(0)
                    cur.execute(
                        """INSERT INTO Students (fullname, regno,contacts, level, course, school, gender, dob) VALUES(?,?,?,?,?,?,?,?)""",
                        (name, reg_no, contact_no, academic_level, academic_course, academic_school, gender, dob))
                    uid = cur.lastrowid

                    sampleImages = 0
                    while True:
                        ret, img = cap.read()
                        img = cv2.flip(img, 1)
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

                        for (x, y, w, h) in faces:
                            sampleImages += 1
                            cv2.imshow('Image Tracking in progress...', img)
                            cv2.imwrite('Dataset/User.' + str(uid) + '.' + str(sampleImages) + '.jpg',
                                        gray[y:y + h, x: x + w])

                            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                        elif sampleImages > 89:

                            QMessageBox.information(QMessageBox(), 'Successful',
                                                    f'Sample images for {name} has been collected successfully! ')

                            print('\n [INFO] : Exiting the program...')
                            break
                    cap.release()
                    conn.commit()
                    cv2.destroyAllWindows()
                    result = f'Images saved for ID: {uid} and name: {name} '
                    print(result)
                    row = [serial, '', uid, '', name, '']

                    with open('StudentDetails/StudentDetails.csv', 'a+') as csv_file:
                        writer = csv.writer(csv_file)
                        writer.writerow(row)
                    csv_file.close()

                    self.ui.label_6_input_error.clear()

                    QMessageBox.information(QMessageBox(), 'Successful',
                                            f'Student record for {name} has been created successfully! ')
                    self.statusBar().showMessage(f'Student record for {name} has been created successfully!')


        except Exception as e:
            print(e)

    def update_student(self):
        try:
            id = ''
            name = self.ui.lineEdit_fullname.text()
            reg_no = self.ui.lineEdit_2_reg_no.text()
            contact_no = self.ui.lineEdit_contacts.text()
            academic_level = self.ui.comboBox_Level.currentText()
            academic_course = self.ui.comboBox_Course.currentText()
            academic_school = self.ui.comboBox_School.currentText()
            gender = self.ui.comboBox_gender.currentText()
            dob = self.ui.dateEdit_dob.text()

            if len(name) == 0 or len(reg_no) == 0 or len(contact_no) == 0:
                self.ui.label_6_input_error.setText('All fields are required')
                QMessageBox.warning(QMessageBox(), 'Warning!',
                                    'Cannot update empty records to database. Please enter valid details!'
                                    )

            else:
                conn = sqlite3.connect('schooldb.db')
                with conn:
                    cur = conn.cursor()
                    cur.execute(
                        """UPDATE Students SET fullname=?, regno=?,contacts=?, level=?, course=?, school=?, gender=?, dob=? WHERE id=?""",
                        (name, reg_no, contact_no, academic_level, academic_course, academic_school, gender, dob))
                    conn.commit()
                    self.ui.label_6_input_error.clear()

                    QMessageBox.information(QMessageBox(), 'Successful',
                                            f'Student record for {name} has been updated successfully! ')
                    self.statusBar().showMessage(f'Student record for {name} has been updated successfully!')

        except Exception as e:
            print(e)

    def delete_student(self):
        del_dialog = DeleteDialog()
        del_dialog.exec_()

    def clear_student(self):

        self.ui.lineEdit_fullname.clear()
        self.ui.lineEdit_2_reg_no.clear()
        self.ui.lineEdit_contacts.clear()

        # self.ui.label_pix_img.clear()

    def search_student(self, s):
        try:

            items = self.ui.tableWidget_student_data.findItems(s, Qt.MatchContains)
            if items:
                item = items[0]  # take the first item

                self.ui.tableWidget_student_data.setCurrentItem(item)

        except Exception as e:
            print(e)

            QMessageBox.critical(QMessageBox(), 'Fatal Error',
                                 f'An error occurred while trying to pass string literal to search view! ')

    def show_all_students(self):
        try:

            conn = sqlite3.connect('schooldb.db')
            with conn:
                cur = conn.cursor()

                cur.execute("""SELECT fullname,regno,contacts, level, course, school, gender, dob FROM Students """)
                data = cur.fetchall()

                if data:
                    # self.ui.tableWidget_student_data.setRowCount(0)
                    self.ui.tableWidget_student_data.insertRow(0)
                    for row, form in enumerate(data):
                        for col, item in enumerate(form):
                            self.ui.tableWidget_student_data.setItem(row, col, QTableWidgetItem(str(item)))
                            col += 1

                            # add a new row

                            row_pos = self.ui.tableWidget_student_data.rowCount()
                            self.ui.tableWidget_student_data.insertRow(row_pos)
                else:

                    QMessageBox.warning(QMessageBox(), 'No Data Found',
                                        'There are no current added record in the database!')

        except Exception as e:
            print(e)

    # ====================== the dataset tab ===================================================

    def train_dataset(self):
        ''' this function uses the LBPHFaceRecognizer_create to create and
        train the system to recognize the captured images
        :param: dataset
        :return: YML FILE
        '''
        try:

            recognizer = cv2.face.LBPHFaceRecognizer_create()

            path = 'Dataset'

            if not os.path.exists('./Recognizer'):
                os.makedirs('./Recognizer')

            ''' a fucntion to load our images with id'''

            def getImagesWithId(path):

                imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

                faces = []
                IDs = []
                for imagePath in imagePaths:
                    face_img = Image.open(imagePath).convert('L')
                    faceNp = np.array(face_img, 'uint8')

                    ID = int(os.path.split(imagePath)[-1].split('.')[1])
                    faces.append(faceNp)
                    IDs.append(ID)

                    cv2.imshow('Training', faceNp)

                    cv2.waitKey(10)
                return np.array(IDs), faces

            IDs, faces = getImagesWithId(path)
            # self.ui.label_6_training_progress
            print('Training in progress..')
            recognizer.train(faces, IDs)

            recognizer.save('Recognizer/trained.yml')
            print('Trained Successfully!')

            cv2.destroyAllWindows()
        except Exception as e:
            ''' this will return none if path does not exist and the system has not yet been trained.
                the system will close and exit without crashing the program.
            '''

            QMessageBox.warning(QMessageBox(), 'Warning', 'No images found in the path provided!')
            exit(0)

    # ====================== the facial recognition tab ========================================

    def start_face_recognizer(self):
        try:
            conn = sqlite3.connect('schooldb.db')

            cur = conn.cursor()

            fname = 'Recognizer/trained.yml'

            if not os.path.isfile(fname):
                QMessageBox.warning(QMessageBox(), 'AN ERROR OCCURRED ', 'Please ensure that there are records in the '
                                                                         'database and the dataset has been trained!'
                                                                         'Click OK to safely close the program!')
                print('Please train the data first')

                exit(0)

            faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

            cap = cv2.VideoCapture(0)

            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.read(fname)

            while True:
                ret, self.ui.label_6_camera = cap.read()
                self.ui.label_6_camera = cv2.flip(self.ui.label_6_camera, 1)
                gray = cv2.cvtColor(self.ui.label_6_camera, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:
                    cv2.rectangle(self.ui.label_6_camera, (x, y), (x + w, y + h), (0, 255, 0), 3)

                    ids, confidence = recognizer.predict(gray[y:y + h, x:x + w])

                    cur.execute('''SELECT fullname FROM Students WHERE id=(?) ''', (ids,))

                    result = cur.fetchall()

                    name = result[0][0] + ', Present'
                    if confidence < 50:

                        cv2.putText(self.ui.label_6_camera, name, (x + 2, y + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 2,
                                    (150, 255, 0), 2)
                    else:

                        cv2.putText(self.ui.label_6_camera, 'No Match Found!', (x + 2, y + h - 5),
                                    cv2.FONT_HERSHEY_SIMPLEX, 2,
                                    (150, 255, 0),
                                    2)

                        logging.info(name)
                        print(name)
                cv2.imshow('Face Recognizer Taking Attendance', self.ui.label_6_camera)

                k = cv2.waitKey(30) & 0xFF
                if k == 27:
                    break
            # log attendance info
            with open('Attendance.log') as file:
                lines = file.read().splitlines()
                lines = [lines[x:x + 1] for x in range(0, len(lines), 1)]
                print(lines)
            # convert log file to a python list
            filename = 'Attendance.log'
            with open(filename) as file:
                content = file.read().splitlines()
            # convert python list to a set to remove duplicates

            attendance1 = set(content)
            # convert the set back to python list
            attendance2 = list(attendance1)

            print('attendance2: ', attendance2)
            main_attendance = [attendance2, ]

            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')

            # save attendance to a csv file using the list
            if not os.path.exists('./StudentAttendance'):
                os.makedirs('./StudentAttendance')
            with open('StudentAttendance/MainAttendance_' + date + '.csv', 'a+', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"')
                csv_writer.writerow(['Name', 'Value'])
                csv_writer.writerows([main_attendance])

            cap.release()
            cv2.destroyAllWindows()
        except Exception as e:

            QMessageBox.warning(QMessageBox(), 'Warning', e)

    # ====================== the attendance tab ================================================
    def mark_attendance(self):
        pass

    def view_attendance(self):
        pass

    def delete_attendance(self):
        pass

    def export_attendance(self):
        pass

    def print_attendance(self):
        pass


data1 = {
    'Certificate': ['Certificate in Community Health & Development', 'Certificate in HIV Management',
                    'Certificate in Business Information Technology', 'Certificate in Information Technology',

                    ],
    'Diploma': ['Diploma in Business Management', 'Diploma in HIV Management',
                'Diploma in Community Health & Development', 'Diploma in Clinical Medicine & Surgery',
                'Diploma in Health Information Management & Informatics',

                ],
    'Degree': ['Bachelor of Business Information Technology', 'Bachelor of Commerce',
               'Bachelor of Science in Human Resource Management',
               'Bachelor of Science in Entrepreneurship',
               'Bachelor of Procurement and Supplies Management',
               'Bachelor of Economics',

               'Bachelor of Economics and Mathematics',
               'Bachelor of Economics and Finance',
               'Bachelor of Economics and Statistics',

               ],
    'Master': ['Masters of Business Administration', 'Doctor of Philosophy in Business Administration'

               ]

}


# create account window
class CreateAccountScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_CreateAccountWindow()
        self.ui.setupUi(self)

        self.ui.signup_btn.clicked.connect(self.create_Account)

        self.ui.lineEdit_password_1_reg.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.lineEdit_password_2_reg.setEchoMode(QtWidgets.QLineEdit.Password)

    # function to create account and direct the user to the login screen
    def create_Account(self):

        try:
            username = self.ui.lineEdit_username.text()
            password1 = self.ui.lineEdit_password_1_reg.text()
            password2 = self.ui.lineEdit_password_2_reg.text()

            if len(username) == 0 or len(password1) == 0 or len(password2) == 0:
                QMessageBox.warning(QMessageBox(), 'Warning!',
                                    'All fields are required!')
                self.ui.label_error.setText('All fields are required')

            elif password1 != password2:

                self.ui.lineEdit_password_1_reg.setText('')
                self.ui.lineEdit_password_2_reg.setText('')
                QMessageBox.warning(QMessageBox(), 'Warning!',
                                    'Passwords did not match!')
                self.ui.label_error.setText('Passwords did not match!')
            elif len(password1) < 4:

                self.ui.lineEdit_password_1_reg.setText('')
                self.ui.lineEdit_password_2_reg.setText('')
                QMessageBox.warning(QMessageBox(), 'Warning!',
                                    'Password is too short! min characters is 4')
                self.ui.label_error.setText('Password is too short! min characters is 4 !')


            else:
                conn = sqlite3.connect('schooldb.db')
                cur = conn.cursor()
                user_info = [username, password1]
                cur.execute("""
                INSERT INTO Users (username, password) VALUES (?,?)
                """, user_info)
                conn.commit()
                conn.close()
                QMessageBox.information(QMessageBox(), 'Successful',
                                        f'Account for {username} created successfully.')

                # self.statusBar().showMessage(f'Account for {username} created successfully!')

                self.ui.lineEdit_username.setText('')
                self.ui.lineEdit_password_1_reg.setText('')
                self.ui.lineEdit_password_2_reg.setText('')

                self.close()
                self.login = LoginScreen()
                self.login.show_login()
        except Exception as e:
            print(e)

    # function to display CreateAccountScreen
    def show_create_acc(self):
        self.show()


# login screen
class LoginScreen(QMainWindow):
    ''' this class holds all the metadata required for login '''

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.ui.signin_btn.clicked.connect(self.login)

    def login(self):
        ''' this function captures the users (admin) login details and matches them
        against the database
        the input accepts only valid username and password.
        '''
        try:
            user = self.ui.lineEdit_username.text()
            passwd = self.ui.lineEdit_password.text()

            if len(user) == 0 or len(passwd) == 0:
                self.ui.label_error.setText('All fields are required!')
            else:

                conn = sqlite3.connect('schooldb.db')
                cur = conn.cursor()

                cur.execute('SELECT * FROM Users WHERE username =? AND password=?', (user, passwd))

                if cur.fetchall():
                    self.close()
                    self.window = MainWindow()
                    self.window.show_main_app()

                else:

                    self.ui.lineEdit_username.setText('')
                    self.ui.lineEdit_password.setText('')
                    QMessageBox.warning(QMessageBox(), 'Authentication Failed!',
                                        'Invalid username or password!')
                    self.ui.label_error.setText('Invalid username or password')

                conn.commit()
                conn.close()

        except Exception as e:
            print(e)

    def show_login(self):
        '''this function loads the login screen after pressing the login button from the welcome screen'''
        self.show()


# welcome screen
class WelcomeScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_WelcomeWindow()
        self.ui.setupUi(self)

        # show greeting depending on time of the day
        currentTime = datetime.datetime.now()
        currentTime.hour

        if currentTime.hour < 12:
            self.ui.label_greeting.setText('Good Morning!')
        elif 12 <= currentTime.hour < 18:
            self.ui.label_greeting.setText('Good Afternoon!')
        else:
            self.ui.label_greeting.setText('Good Evening!')

        self.ui.login_btn.clicked.connect(self.show_login_screen)
        self.ui.account_btn.clicked.connect(self.show_create_acc_screen)

    # function to load in the login screen
    def show_login_screen(self):
        self.close()
        self.login = LoginScreen()
        self.login.show_login()
        print('login successful')

    # function to load in the account screen
    def show_create_acc_screen(self):
        self.close()
        self.account = CreateAccountScreen()

        self.account.show_create_acc()
        print('create_acc successful')


# main splash_screen welcome QMainWindow
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # interface design
        # remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.shadowFrame.setGraphicsEffect(self.shadow)

        # QTimer start

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(45)

        # initail text
        self.ui.label_description.setText('<strong>Loading </strong> setup files..')

        # change description
        QtCore.QTimer.singleShot(2000,
                                 lambda: self.ui.label_description.setText('<strong>Initializing</strong> database...'))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText(
            '<strong>Running</strong> configuration settings...'))

        self.show()

    def progress(self):
        global COUNTER
        # set value to the progress bar
        self.ui.progressBar.setValue(COUNTER)

        # close the splash screen upon reaching 100%

        if COUNTER > 100:
            # stop the timer
            self.timer.stop()

            # show Welcome screen
            self.welcome = WelcomeScreen()
            self.welcome.show()

            # close the splash screen
            self.close()

            # add counter
        COUNTER += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = SplashScreen()
    screen.show()
    sys.exit(app.exec_())
