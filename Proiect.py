import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMainWindow, \
    QGraphicsDropShadowEffect, QLineEdit, QComboBox
class Upperbody(QMainWindow):
    def __init__(self, fereastra_upper=None):
        super().__init__()
        self.fereastra_upper = fereastra_upper
        self.setWindowTitle('Fitlog - UpperBody')
        self.resize(380, 720)
        self.setFixedHeight(720)
        self.setFixedWidth(380)
        widgetprincipal = QWidget()
        widgetprincipal.setObjectName('widgetprincipal')
        widgetprincipal.setStyleSheet(
            "#widgetprincipal{"
            "border-image:url(C:/Users/HP/Desktop/PCLPPython/pozabackground.jpeg);"
            "}"
        )
        widgetprincipal.setContentsMargins(40, 130, 40, 70)
        layout = QVBoxLayout(widgetprincipal)
        Titlul = QLabel("Upper Body")
        Titlul.setStyleSheet("color: white; font-size: 40px; font-weight: bold; font-family: Comic Sans MS;")
        layout.addWidget(Titlul, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addSpacing(40)
        Chest = QPushButton("Chest")
        Chest.setFixedHeight(50)
        Chest.setFixedWidth(200)
        Chest.setStyleSheet(
            "QPushButton{"
            "background-color: white;"
            "border: none;"
            "border-radius: 25px;"
            "font-size: 25px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QPushButton:hover{"
            "color: white;"
            "background-color: black;"
            "}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(85, 85, 85))
        Chest.setGraphicsEffect(shadow)
        layout.addWidget(Chest, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.addSpacing(20)

        Arms = QPushButton("Arms")
        Arms.setFixedHeight(50)
        Arms.setFixedWidth(200)
        Arms.setStyleSheet(
            "QPushButton{"
            "background-color: white;"
            "border: none;"
            "border-radius: 25px;"
            "font-size: 25px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QPushButton:hover{"
            "color: white;"
            "background-color: black;"
            "}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(85, 85, 85))
        Arms.setGraphicsEffect(shadow)
        layout.addWidget(Arms, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.addSpacing(20)
        Shoulders = QPushButton("Shoulders")
        Shoulders.setFixedHeight(50)
        Shoulders.setFixedWidth(200)
        Shoulders.setStyleSheet(
            "QPushButton{"
            "background-color: white;"
            "border: none;"
            "border-radius: 25px;"
            "font-size: 25px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QPushButton:hover{"
            "color: white;"
            "background-color: black;"
            "}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(85, 85, 85))
        Shoulders.setGraphicsEffect(shadow)
        layout.addWidget(Shoulders, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.addSpacing(20)
        Back= QPushButton("Back")
        Back.setFixedHeight(50)
        Back.setFixedWidth(200)
        Back.setStyleSheet(
            "QPushButton{"
            "background-color: white;"
            "border: none;"
            "border-radius: 25px;"
            "font-size: 25px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QPushButton:hover{"
            "color: white;"
            "background-color: black;"
            "}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(85, 85, 85))
        Back.setGraphicsEffect(shadow)
        layout.addWidget(Back, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.addSpacing(20)
        layout.addStretch()
        self.setCentralWidget(widgetprincipal)
class Lowerbody(QMainWindow):
    def __init__(self, fereastra_lower=None):
        super().__init__()
        self.fereastra_lower = fereastra_lower
        self.setWindowTitle('Fitlog - LowerBody')
        self.resize(380, 720)
        self.setFixedHeight(720)
        self.setFixedWidth(380)
        widgetprincipal = QWidget()
        widgetprincipal.setObjectName('widgetprincipal')
        widgetprincipal.setStyleSheet(
            "#widgetprincipal{"
            "border-image:url(C:/Users/HP/Desktop/PCLPPython/pozabackground.jpeg);"
            "}"
        )
        widgetprincipal.setContentsMargins(40, 160, 40, 70)
        layout = QVBoxLayout(widgetprincipal)
        Titlul = QLabel("Lower Body")
        Titlul.setStyleSheet("color: white; font-size: 40px; font-weight: bold; font-family: Comic Sans MS;")
        layout.addWidget(Titlul, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addSpacing(40)
        Glutes = QPushButton("Glutes")
        Glutes.setFixedHeight(50)
        Glutes.setFixedWidth(200)
        Glutes.setStyleSheet(
            "QPushButton{"
            "background-color: white;"
            "border: none;"
            "border-radius: 25px;"
            "font-size: 25px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QPushButton:hover{"
            "color: white;"
            "background-color: black;"
            "}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(85, 85, 85))
        Glutes.setGraphicsEffect(shadow)
        layout.addWidget(Glutes, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.addSpacing(20)

        Legs = QPushButton("Legs")
        Legs.setFixedHeight(50)
        Legs.setFixedWidth(200)
        Legs.setStyleSheet(
            "QPushButton{"
            "background-color: white;"
            "border: none;"
            "border-radius: 25px;"
            "font-size: 25px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QPushButton:hover{"
            "color: white;"
            "background-color: black;"
            "}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(85, 85, 85))
        Legs.setGraphicsEffect(shadow)
        layout.addWidget(Legs, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.addSpacing(20)

        layout.addStretch()
        self.setCentralWidget(widgetprincipal)
class sport(QMainWindow):
    def __init__(self, fereastra_sport=None):
        super().__init__()
        self.fereastra_sport = fereastra_sport
        self.setWindowTitle('Fitlog - Sport')
        self.resize(380, 720)
        self.setFixedHeight(720)
        self.setFixedWidth(380)
        widgetprincipal = QWidget()
        widgetprincipal.setObjectName('widgetprincipal')
        widgetprincipal.setStyleSheet(
            "#widgetprincipal{"
            "border-image:url(C:/Users/HP/Desktop/PCLPPython/pozabackground.jpeg);"
            "}"
        )
        widgetprincipal.setContentsMargins(40, 70, 40, 70)
        layout = QVBoxLayout(widgetprincipal)
        Question = QLabel(" What would \nyou like to do\n    today?")
        Question.setStyleSheet("color: white; font-size: 30px; font-weight: bold; font-family: Comic Sans MS;")
        layout.addWidget(Question, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addSpacing(40)
        UpperBody = QPushButton("UpperBody")
        UpperBody.setFixedHeight(50)
        UpperBody.setFixedWidth(200)
        UpperBody.setStyleSheet(
            "QPushButton{"
            "background-color: white;"
            "border: none;"
            "border-radius: 25px;"
            "font-size: 25px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QPushButton:hover{"
            "color: white;"
            "background-color: black;"
            "}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(85, 85, 85))
        UpperBody.setGraphicsEffect(shadow)
        layout.addWidget(UpperBody, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.addSpacing(20)

        LowerBody = QPushButton("LowerBody")
        LowerBody.setFixedHeight(50)
        LowerBody.setFixedWidth(200)
        LowerBody.setStyleSheet(
            "QPushButton{"
            "background-color: white;"
            "border: none;"
            "border-radius: 25px;"
            "font-size: 25px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QPushButton:hover{"
            "color: white;"
            "background-color: black;"
            "}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(85, 85, 85))
        LowerBody.setGraphicsEffect(shadow)
        layout.addWidget(LowerBody, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.addSpacing(20)
        Core = QPushButton("Core")
        Core.setFixedHeight(50)
        Core.setFixedWidth(200)
        Core.setStyleSheet(
            "QPushButton{"
            "background-color: white;"
            "border: none;"
            "border-radius: 25px;"
            "font-size: 25px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QPushButton:hover{"
            "color: white;"
            "background-color: black;"
            "}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(85, 85, 85))
        Core.setGraphicsEffect(shadow)
        layout.addWidget(Core, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.addSpacing(20)
        Cardio = QPushButton("Cardio")
        Cardio.setFixedHeight(50)
        Cardio.setFixedWidth(200)
        Cardio.setStyleSheet(
            "QPushButton{"
            "background-color: white;"
            "border: none;"
            "border-radius: 25px;"
            "font-size: 25px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QPushButton:hover{"
            "color: white;"
            "background-color: black;"
            "}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(85, 85, 85))
        Cardio.setGraphicsEffect(shadow)
        layout.addWidget(Cardio, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.addSpacing(20)
        layout.addStretch()
        UpperBody.clicked.connect(self.paginaupper)
        LowerBody.clicked.connect(self.paginalower)
        self.setCentralWidget(widgetprincipal)
    def paginaupper(self):
        self.fereastranoua=Upperbody(fereastra_upper=self)
        self.fereastranoua.show()
        self.hide()
    def paginalower(self):
        self.fereastranoua=Lowerbody(fereastra_lower=self)
        self.fereastranoua.show()
        self.hide()
class food(QMainWindow):
    def __init__(self, fereastra_food=None):
        super().__init__()
        self.fereastra_food = fereastra_food
        self.setWindowTitle('Fitlog - Food')
        self.resize(380, 720)
        self.setFixedHeight(720)
        self.setFixedWidth(380)
        widgetprincipal = QWidget()
        widgetprincipal.setObjectName('widgetprincipal')
        widgetprincipal.setStyleSheet(
            "#widgetprincipal{"
            "border-image:url(C:/Users/HP/Desktop/PCLPPython/pozabackground.jpeg);"
            "}"
        )
        widgetprincipal.setContentsMargins(40, 70, 40, 70)
        layout = QVBoxLayout(widgetprincipal)
        self.setCentralWidget(widgetprincipal)
class paginadestart(QMainWindow):
    def __init__(self, fereastra_alege=None):
        super().__init__()
        self.fereastra_alege = fereastra_alege
        self.setWindowTitle('Fitlog - Food/Sport')
        self.resize(380, 720)
        self.setFixedHeight(720)
        self.setFixedWidth(380)
        widgetprincipal = QWidget()
        widgetprincipal.setObjectName('widgetprincipal')
        widgetprincipal.setStyleSheet(
            "#widgetprincipal{"
            "border-image:url(C:/Users/HP/Desktop/PCLPPython/pozabackground.jpeg);"
            "}"
        )
        widgetprincipal.setContentsMargins(40, 70, 40, 70)
        layout = QVBoxLayout(widgetprincipal)
        textwelcome = QLabel("Welcome to\nyour fitness\n  journal!")
        textwelcome.setStyleSheet("color: white; font-size: 40px; font-weight: bold; font-family: Comic Sans MS;")
        layout.addWidget(textwelcome,alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addSpacing(40)
        textinterest = QLabel("Choose your interest")
        textinterest.setStyleSheet("color: white; font-size: 25px; font-weight: bold; font-family: Comic Sans MS;")
        layout.addWidget(textinterest,alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addSpacing(35)
        Sport = QPushButton("Sport")
        Sport.setFixedHeight(50)
        Sport.setFixedWidth(200)
        Sport.setStyleSheet(
            "QPushButton{"
            "background-color: white;"
            "border: none;"
            "border-radius: 25px;"
            "font-size: 25px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QPushButton:hover{"
            "color: white;"
            "background-color: black;"
            "}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(85, 85, 85))
        Sport.setGraphicsEffect(shadow)
        layout.addWidget(Sport, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.addSpacing(15)

        Food = QPushButton("Food")
        Food.setFixedHeight(50)
        Food.setFixedWidth(200)
        Food.setStyleSheet(Sport.styleSheet())
        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(0)
        shadow2.setOffset(0, 5)
        shadow2.setColor(QColor(85, 85, 85))
        Food.setGraphicsEffect(shadow2)
        layout.addWidget(Food, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.addStretch()
        Sport.clicked.connect(self.meniusport)
        Food.clicked.connect(self.meniumancare)
        self.setCentralWidget(widgetprincipal)
    def meniusport(self):
        self.fereastranoua=sport(fereastra_sport=self)
        self.fereastranoua.show()
        self.hide()
    def meniumancare(self):
        self.fereastranoua = food(fereastra_food=self)
        self.fereastranoua.show()
        self.hide()


class inregistrare2(QMainWindow):
    def __init__(self, fereastra_sign2=None):
        super().__init__()
        self.fereastra_sign2 = fereastra_sign2
        self.setWindowTitle('Fitlog - Sign in')
        self.resize(380, 720)
        self.setFixedHeight(720)
        self.setFixedWidth(380)
        widgetprincipal = QWidget()
        widgetprincipal.setObjectName('widgetprincipal')
        widgetprincipal.setStyleSheet(
            "#widgetprincipal{"
            "border-image:url(C:/Users/HP/Desktop/PCLPPython/pozabackground.jpeg);"
            "}"
        )
        widgetprincipal.setContentsMargins(40, 5, 40, 70)
        layout = QVBoxLayout(widgetprincipal)
        textsignin = QLabel("Sign in")
        textsignin.setStyleSheet("color: white; font-size: 25px; font-weight: bold; font-family: Comic Sans MS;")
        layout.addWidget(textsignin)
        layout.addSpacing(60)
        textpagina = QLabel("2/2")
        textpagina.setStyleSheet("color: white; font-size: 15px; font-weight: bold; font-family: Comic Sans MS;")
        layout.addWidget(textpagina, 0, alignment=Qt.AlignmentFlag.AlignRight)
        card = QWidget()
        card.setObjectName('card')
        card.setStyleSheet(
            "#card{"
            "background-color: white;"
            "border: 1px solid black;"
            "border-radius: 10px;"
            "}"
        )
        layoutcard = QVBoxLayout(card)
        Height = QLabel("Height:")
        Height.setStyleSheet(
            "color: black;"
            " font-size: 25px; "
            "font-weight: bold; "
            "font-family: Comic Sans MS;"

        )
        Heighttext = QLineEdit()
        Heighttext.setPlaceholderText("Write...")
        Heighttext.setFixedHeight(40)
        Heighttext.setStyleSheet(
            "QLineEdit{"
            "color:gray;"
            "background-color: white;"
            "border: 1px solid black;"
            "border-radius: 20px;"
            "font-size: 15px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QLineEdit::focus{"
            "border : 1px solid pink;"
            "}"
        )

        Weight = QLabel("Age:")
        Weight.setStyleSheet(
            "color: black;"
            " font-size: 25px; "
            "font-weight: bold; "
            "font-family: Comic Sans MS;"

        )
        Weighttext = QLineEdit("")
        Weighttext.setFixedHeight(40)
        Weighttext.setPlaceholderText("Write....")
        Weighttext.setStyleSheet(
            "QLineEdit{"
            "color:gray;"
            "background-color: white;"
            "border: 1px solid black;"
            "border-radius: 20px;"
            "font-size: 15px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QLineEdit:focus{"
            "border : 1px solid pink;"
            "}"
        )
        Goal = QLabel("Goal:")
        Goal.setStyleSheet(
            "color: black;"
            " font-size: 25px; "
            "font-weight: bold; "
            "font-family: Comic Sans MS;"

        )
        sagetica1=QComboBox()
        sagetica1.addItem("Get toned")
        sagetica1.addItem("Gain muscle and weight")
        sagetica1.addItem("Gain muscle and lose weight")
        sagetica1.setPlaceholderText("Choose")
        sagetica1.setFixedHeight(40)
        sagetica1.setStyleSheet(
            "QComboBox {"
    "    background-color: white;"
    "    color: black;"
    "    border: 1px solid black;"
    "    border-radius: 20px;"
    "    padding: 10px 15px;"
    "    font-size: 15px;"
    "    font-weight: bold;"
            "font-family:Comic Sans MS;"
    "}"
    "QComboBox:hover {"
    "    border: 1px solid pink;"
    "}"
    "QComboBox::drop-down {"
    "    subcontrol-origin: padding;"
    "    subcontrol-position: top right;"
    "    width: 35px;"
    "    border-left: 1px solid white;"
    "}"
    "QComboBox QAbstractItemView {"
    "    background-color: pink;"
    "    color: black;"
        "font-family: Comic Sans MS;"
    "    border: 1px solid white;"
    "    selection-background-color: pink;"
    "    selection-color: white;"
    "    outline: none;"
    "}"
        )
        question=QLabel("Are you an athlete?")
        question.setStyleSheet(
            "color: black;"
            " font-size: 25px; "
            "font-weight: bold; "
            "font-family: Comic Sans MS;"

        )

        sagetica2=QComboBox()
        sagetica2.addItem("Yes")
        sagetica2.addItem("No")
        sagetica2.setPlaceholderText("Choose")
        sagetica2.setFixedHeight(40)
        sagetica2.setStyleSheet(
            "QComboBox {"
            "    background-color: white;"
            "    color: black;"
            "    border: 1px solid black;"
            "    border-radius: 20px;"
            "    padding: 10px 15px;"
            "    font-size: 15px;"
            "    font-weight: bold;"
            "font-family:Comic Sans MS;"
            "}"
            "QComboBox:hover {"
            "    border: 1px solid pink;"
            "}"
            "QComboBox::drop-down {"
            "    subcontrol-origin: padding;"
            "    subcontrol-position: top right;"
            "    width: 35px;"
            "    border-left: 1px solid white;"
            "}"
            "QComboBox QAbstractItemView {"
            "    background-color: pink;"
            "    color: black;"
            "font-family: Comic Sans MS;"
            "    border: 1px solid white;"
            "    selection-background-color: pink;"
            "    selection-color: white;"
            "    outline: none;"
            "}"
        )
        question = QLabel("Are you an athlete?")
        question.setStyleSheet(
            "color: black;"
            " font-size: 25px; "
            "font-weight: bold; "
            "font-family: Comic Sans MS;"

        )
        Createaccount = QPushButton("Create account")
        Createaccount.setFixedHeight(30)
        Createaccount.setFixedWidth(160)
        Createaccount.setStyleSheet(
            "QPushButton{"
            "color: white;"
            "background-color: black;"
            "border: none;"
            "border-radius: 15px;"
            "font-size: 15px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(85, 85, 85))
        Createaccount.setGraphicsEffect(shadow)

        layout.addWidget(card)
        layoutcard.addSpacing(5)
        layoutcard.addWidget(Height)
        layoutcard.addWidget(Heighttext)
        layoutcard.addSpacing(15)
        layoutcard.addWidget(Weight)
        layoutcard.addWidget(Weighttext)
        layoutcard.addSpacing(15)
        layoutcard.addWidget(Goal)
        layoutcard.addWidget(sagetica1)
        layoutcard.addSpacing(15)
        layoutcard.addWidget(question)
        layoutcard.addWidget(sagetica2)
        layoutcard.addSpacing(15)
        layoutcard.addWidget(Createaccount, alignment=Qt.AlignmentFlag.AlignHCenter)
        layoutcard.addSpacing(10)
        layout.addStretch()
        Createaccount.clicked.connect(self.paginadestart)
        self.setCentralWidget(widgetprincipal)
    def paginadestart(self):
        self.fereastranoua = paginadestart(fereastra_alege=self)
        self.fereastranoua.show()
        self.hide()

class inregistrare(QMainWindow):
    def __init__(self, fereastra_sign=None):
        super().__init__()
        self.fereastra_sign = fereastra_sign
        self.setWindowTitle('Fitlog - Sign in')
        self.resize(380, 720)
        self.setFixedHeight(720)
        self.setFixedWidth(380)
        widgetprincipal = QWidget()
        widgetprincipal.setObjectName('widgetprincipal')
        widgetprincipal.setStyleSheet(
            "#widgetprincipal{"
            "border-image:url(C:/Users/HP/Desktop/PCLPPython/pozabackground.jpeg);"
            "}"
        )
        widgetprincipal.setContentsMargins(40, 4, 40, 70)
        layout = QVBoxLayout(widgetprincipal)
        textsignin=QLabel("Sign in")
        textsignin.setStyleSheet("color: white; font-size: 25px; font-weight: bold; font-family: Comic Sans MS;")
        layout.addWidget(textsignin)
        layout.addSpacing(80)
        textpagina=QLabel("1/2")
        textpagina.setStyleSheet("color: white; font-size: 15px; font-weight: bold; font-family: Comic Sans MS;")
        layout.addWidget(textpagina,0,alignment=Qt.AlignmentFlag.AlignRight)
        layout.addSpacing(0)
        card = QWidget()
        card.setObjectName('card')
        card.setStyleSheet(
            "#card{"
            "background-color: white;"
            "border: 1px solid black;"
            "border-radius: 10px;"
            "}"
        )
        layoutcard = QVBoxLayout(card)
        fullname = QLabel("Full Name:")
        fullname.setStyleSheet(
            "color: black;"
            " font-size: 25px; "
            "font-weight: bold; "
            "font-family: Comic Sans MS;"

        )
        fullnametext = QLineEdit()
        fullnametext.setPlaceholderText("Write...")
        fullnametext.setFixedHeight(40)
        fullnametext.setStyleSheet(
            "QLineEdit{"
            "color:gray;"
            "background-color: white;"
            "border: 1px solid black;"
            "border-radius: 20px;"
            "font-size: 15px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QLineEdit::focus{"
            "border : 1px solid pink;"
            "}"
        )

        age = QLabel("Age:")
        age.setStyleSheet(
            "color: black;"
            " font-size: 25px; "
            "font-weight: bold; "
            "font-family: Comic Sans MS;"

        )
        agetext = QLineEdit("")
        agetext.setFixedHeight(40)
        agetext.setPlaceholderText("Write....")
        agetext.setStyleSheet(
            "QLineEdit{"
            "color:gray;"
            "background-color: white;"
            "border: 1px solid black;"
            "border-radius: 20px;"
            "font-size: 15px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QLineEdit:focus{"
            "border : 1px solid pink;"
            "}"
        )
        email = QLabel("Email:")
        email.setStyleSheet(
            "color: black;"
            " font-size: 25px; "
            "font-weight: bold; "
            "font-family: Comic Sans MS;"

        )
        emailtext = QLineEdit()
        emailtext.setPlaceholderText("Write...")
        emailtext.setFixedHeight(40)
        emailtext.setStyleSheet(
            "QLineEdit{"
            "color:gray;"
            "background-color: white;"
            "border: 1px solid black;"
            "border-radius: 20px;"
            "font-size: 15px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QLineEdit::focus{"
            "border : 1px solid pink;"
            "}"
        )

        password = QLabel("Password:")
        password.setStyleSheet(
            "color: black;"
            " font-size: 25px; "
            "font-weight: bold; "
            "font-family: Comic Sans MS;"

        )
        passwordtext = QLineEdit("")
        passwordtext.setFixedHeight(40)
        passwordtext.setPlaceholderText("Write....")
        passwordtext.setStyleSheet(
            "QLineEdit{"
            "color:gray;"
            "background-color: white;"
            "border: 1px solid black;"
            "border-radius: 20px;"
            "font-size: 15px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QLineEdit:focus{"
            "border : 1px solid pink;"
            "}"
        )
        Next = QPushButton("Next")
        Next.setFixedHeight(30)
        Next.setFixedWidth(160)
        Next.setStyleSheet(
            "QPushButton{"
            "color: white;"
            "background-color: black;"
            "border: none;"
            "border-radius: 15px;"
            "font-size: 15px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(85, 85, 85))
        Next.setGraphicsEffect(shadow)

        passwordtext.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(card)
        layoutcard.addSpacing(5)
        layoutcard.addWidget(fullname)
        layoutcard.addWidget(fullnametext)
        layoutcard.addSpacing(15)
        layoutcard.addWidget(age)
        layoutcard.addWidget(agetext)
        layoutcard.addSpacing(15)
        layoutcard.addWidget(email)
        layoutcard.addWidget(emailtext)
        layoutcard.addSpacing(15)
        layoutcard.addWidget(password)
        layoutcard.addWidget(passwordtext)
        layoutcard.addSpacing(15)
        layoutcard.addWidget(Next, alignment=Qt.AlignmentFlag.AlignHCenter)
        layoutcard.addSpacing(10)
        layout.addStretch()
        Next.clicked.connect(self.intrareinregistrare2)
        self.setCentralWidget(widgetprincipal)

    def intrareinregistrare2(self):
        self.fereastranoua = inregistrare2(fereastra_sign2=self)
        self.fereastranoua.show()
        self.hide()

class logare(QMainWindow):
    def __init__(self, fereastra_anterioara=None):
        super().__init__()
        self.fereastra_anterioara = fereastra_anterioara
        self.setWindowTitle('Fitlog - Log In')
        self.resize(380, 720)
        self.setFixedHeight(720)
        self.setFixedWidth(380)
        widgetprincipal = QWidget()
        widgetprincipal.setObjectName('widgetprincipal')
        widgetprincipal.setStyleSheet(
            "#widgetprincipal{"
            "border-image:url(C:/Users/HP/Desktop/PCLPPython/pozabackground.jpeg);"
            "}"
        )
        widgetprincipal.setContentsMargins(40, 5, 40, 70)

        layout = QVBoxLayout(widgetprincipal)
        textlogin = QLabel("Log in")
        textlogin.setStyleSheet("color: white; font-size: 25px; font-weight: bold; font-family: Comic Sans MS;")
        layout.addWidget(textlogin)
        layout.addSpacing(140)
        card=QWidget()
        card.setObjectName('card')
        card.setStyleSheet(
            "#card{"
            "background-color: white;"
            "border: 1px solid black;"
            "border-radius: 10px;"
            "}"
        )
        layoutcard=QVBoxLayout(card)
        email=QLabel("Email:")
        email.setStyleSheet(
            "color: black;"
            " font-size: 25px; "
            "font-weight: bold; "
            "font-family: Comic Sans MS;"

        )
        emailtext=QLineEdit()
        emailtext.setPlaceholderText("Write...")
        emailtext.setFixedHeight(40)
        emailtext.setStyleSheet(
            "QLineEdit{"
            "color:gray;"
            "background-color: white;"
            "border: 1px solid black;"
            "border-radius: 20px;"
            "font-size: 15px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QLineEdit::focus{"
            "border : 1px solid pink;"
            "}"
        )

        password=QLabel("Password:")
        password.setStyleSheet(
            "color: black;"
            " font-size: 25px; "
            "font-weight: bold; "
            "font-family: Comic Sans MS;"

        )
        passwordtext=QLineEdit("" )
        passwordtext.setFixedHeight(40)
        passwordtext.setPlaceholderText("Write....")
        passwordtext.setStyleSheet(
            "QLineEdit{"
            "color:gray;"
            "background-color: white;"
            "border: 1px solid black;"
            "border-radius: 20px;"
            "font-size: 15px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QLineEdit:focus{"
            "border : 1px solid pink;"
            "}"
        )
        passwordtext.setEchoMode(QLineEdit.EchoMode.Password)

        intrebare=QLabel("Forgot your password?")
        intrebare.setStyleSheet(
            "QLabel{"
            "color:black; font-size: 12px; font-family: Comic Sans MS;"
            "}"
            "QLabel:hover{"
             "color:blue;"
            "font:underline 12px 'Comic Sans MS';"
            "}"
        )
        Getin=QPushButton("Get in")
        Getin.setFixedHeight(30)
        Getin.setFixedWidth(160)
        Getin.setStyleSheet(
            "QPushButton{"
            "color: white;"
            "background-color: black;"
            "border: none;"
            "border-radius: 15px;"
            "font-size: 15px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(85, 85, 85))
        Getin.setGraphicsEffect(shadow)

        layoutcard.addWidget(email)
        layoutcard.addWidget(emailtext)
        layoutcard.addSpacing(15)
        layoutcard.addWidget(password)
        layoutcard.addWidget(passwordtext)
        layoutcard.addWidget(intrebare)
        layoutcard.addSpacing(15)
        layoutcard.addWidget(Getin, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(card)
        layout.addStretch()
        self.setCentralWidget(widgetprincipal)

class primaclasa(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Fitlog')
        self.resize(380, 720)
        self.setFixedHeight(720)
        self.setFixedWidth(380)

        widgetprincipal = QWidget()
        widgetprincipal.setObjectName('widgetprincipal')
        widgetprincipal.setStyleSheet(
            "#widgetprincipal{"
            "border-image:url(C:/Users/HP/Desktop/PCLPPython/pozabackground.jpeg);"
            "}"
        )
        widgetprincipal.setContentsMargins(40, 70, 40, 70)

        layout = QVBoxLayout(widgetprincipal)

        titlu = QLabel("Hello!")
        titlu.setStyleSheet("color: white; font-size: 65px; font-weight: bold; font-family: Comic Sans MS;")
        layout.addWidget(titlu, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addSpacing(30)

        signin = QPushButton("Sign in")
        signin.setFixedHeight(50)
        signin.setFixedWidth(200)
        signin.setStyleSheet(
            "QPushButton{"
            "background-color: white;"
            "border: none;"
            "border-radius: 25px;"
            "font-size: 25px;"
            "font-family: Comic Sans MS;"
            "font-weight: bold;"
            "}"
            "QPushButton:hover{"
            "color: white;"
            "background-color: black;"
            "}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(85, 85, 85))
        signin.setGraphicsEffect(shadow)
        layout.addWidget(signin, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.addSpacing(15)

        login = QPushButton("Log in")
        login.setFixedHeight(50)
        login.setFixedWidth(200)
        login.setStyleSheet(signin.styleSheet())
        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(0)
        shadow2.setOffset(0, 5)
        shadow2.setColor(QColor(85, 85, 85))
        login.setGraphicsEffect(shadow2)
        layout.addWidget(login, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.addSpacing(30)

        urare = QLabel("Be prepared to \n  change your \n       life!")
        urare.setStyleSheet("color: white; font-size: 35px; font-weight: bold; font-family: Comic Sans MS;")
        layout.addWidget(urare, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.addStretch()
        login.clicked.connect(self.intrarelogare)
        signin.clicked.connect(self.intrareinregistrare)
        self.setCentralWidget(widgetprincipal)

    def intrarelogare(self):
        self.fereastranoua = logare(fereastra_anterioara=self)
        self.fereastranoua.show()
        self.hide()

    def intrareinregistrare(self):
        self.fereastranoua=inregistrare(fereastra_sign=self)
        self.fereastranoua.show()
        self.hide()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_principal = primaclasa()
    app_principal.show()

    sys.exit(app.exec())