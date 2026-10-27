import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMainWindow, \
    QGraphicsDropShadowEffect, QLineEdit, QComboBox, QHBoxLayout
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
        Titlul.setStyleSheet("color: white; font-size: 40px; font-weight: bold; font-family: Segoe UI;")
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
            "font-family: Segoe UI;"
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
            "font-family: Segoe UI;"
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
            "font-family: Segoe UI;"
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
            "font-family: Segoe UI;"
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
        Titlul.setStyleSheet("color: white; font-size: 40px; font-weight: bold; font-family: Segoe UI;")
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
            "font-family: Segoe UI;"
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
            "font-family: Segoe UI;"
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
        widgetprincipal.setContentsMargins(40, 100, 40, 70)
        layout = QVBoxLayout(widgetprincipal)
        Question = QLabel("What would you like to do today?")
        Question.setStyleSheet("color: white; font-size: 32px; font-weight: bold; font-family: Segoe UI;")
        Question.setAlignment(Qt.AlignmentFlag.AlignCenter)
        Question.setWordWrap(True)
        layout.addWidget(Question)
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
            "font-family: Segoe UI;"
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
            "font-family: Segoe UI;"
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
            "font-family: Segoe UI;"
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
            "font-family: Segoe UI;"
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
        widgetprincipal.setContentsMargins(40, 120, 40, 70)
        layout = QVBoxLayout(widgetprincipal)
        textwelcome = QLabel("Welcome to your fitness journal!")
        textwelcome.setStyleSheet("color: white; font-size: 35px; font-weight: bold; font-family: Segoe UI;")
        textwelcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        textwelcome.setWordWrap(True)
        layout.addWidget(textwelcome)
        layout.addSpacing(40)
        textinterest = QLabel("Choose your interest")
        textinterest.setStyleSheet("color: white; font-size: 25px; font-weight: bold; font-family: Segoe UI;")
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
            "font-family: Segoe UI;"
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
        header_layout = QHBoxLayout()

        btn_back = QPushButton("←")
        btn_back.setFixedSize(40, 40)
        btn_back.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_back.setStyleSheet(
            "QPushButton {"
            "   color: black; "
            "   font-size: 26px; "
            "   font-weight: bold; "
            "   background: transparent; "
            "   border: none; "
            "}"
            "QPushButton:hover {"
            "   color: white; "
            "}"
        )
        btn_back.clicked.connect(self.go_back)
        header_layout.addWidget(btn_back)

        header_layout.addStretch()
        textsignin = QLabel("Sign in")
        textsignin.setStyleSheet("color: white; font-size: 25px; font-weight: bold; font-family: Segoe UI;")
        header_layout.addWidget(textsignin)

        layout.addLayout(header_layout)

        layout.addSpacing(60)
        textpagina = QLabel("2/2")
        textpagina.setStyleSheet("color: white; font-size: 15px; font-weight: bold; font-family: Segoe UI;")
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
            "font-family: Segoe UI;"

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
            "font-family: Segoe UI;"
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
            "font-family: Segoe UI;"

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
            "font-family: Segoe UI;"
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
            "font-family: Segoe UI;"

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
            "font-family:Segoe UI;"
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
        "font-family: Segoe UI;"
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
            "font-family: Segoe UI;"

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
            "font-family:Segoe UI;"
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
            "font-family: Segoe UI;"
            "    border: 1px solid white;"
            "    selection-background-color: pink;"
            "    selection-color: white;"
            "    outline: none;"
            "}"
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
            "font-family: Segoe UI;"
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
    def go_back(self):
        if self.fereastra_sign2:
            self.fereastra_sign2.show()
            self.close()

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
        header_layout = QHBoxLayout()

        btn_back = QPushButton("←")
        btn_back.setFixedSize(40, 40)
        btn_back.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_back.setStyleSheet(
            "QPushButton {"
            "   color: black; "
            "   font-size: 26px; "
            "   font-weight: bold; "
            "   background: transparent; "
            "   border: none; "
            "}"
            "QPushButton:hover {"
            "   color: white; "
            "}"
        )
        btn_back.clicked.connect(self.go_back)
        header_layout.addWidget(btn_back)

        header_layout.addStretch()

        textsignin=QLabel("Sign in")
        textsignin.setStyleSheet("color: white; font-size: 25px; font-weight: bold; font-family: Segoe UI;")
        header_layout.addWidget(textsignin)

        layout.addLayout(header_layout)
        layout.addSpacing(80)
        textpagina=QLabel("1/2")
        textpagina.setStyleSheet("color: white; font-size: 15px; font-weight: bold; font-family: Segoe UI;")
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
            "font-family: Segoe UI;"

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
            "font-family: Segoe UI;"
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
            "font-family: Segoe UI;"

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
            "font-family: Segoe UI;"
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
            "font-family: Segoe UI;"

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
            "font-family: Segoe UI;"
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
            "font-family: Segoe UI;"

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
            "font-family: Segoe UI;"
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
            "font-family: Segoe UI;"
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
    def go_back(self):
        if self.fereastra_sign:
            self.fereastra_sign.show()
            self.close()
class Parolanoua(QMainWindow):
    def __init__(self, fereastra_parola=None):
        super().__init__()
        self.fereastra_parola = fereastra_parola
        self.setWindowTitle('Fitlog - Forgot your password')
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
        header_layout = QHBoxLayout()

        btn_back = QPushButton("←")
        btn_back.setFixedSize(40, 40)
        btn_back.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_back.setStyleSheet(
            "QPushButton {"
            "   color: black; "
            "   font-size: 26px; "
            "   font-weight: bold; "
            "   background: transparent; "
            "   border: none; "
            "}"
            "QPushButton:hover {"
            "   color: white; "
            "}"
        )
        btn_back.clicked.connect(self.go_back)
        header_layout.addWidget(btn_back)
        header_layout.addStretch()

        textlogin = QLabel("Code")
        textlogin.setStyleSheet("color: white; font-size: 25px; font-weight: bold; font-family: Segoe UI;")
        header_layout.addWidget(textlogin)

        layout.addLayout(header_layout)
        layout.addSpacing(150)
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
        password1 = QLabel("New password:")
        password1.setStyleSheet(
            "color: black;"
            " font-size: 23px; "
            "font-weight: bold; "
            "font-family: Segoe UI;"

        )
        passwordtext1 = QLineEdit("")
        passwordtext1.setFixedHeight(40)
        passwordtext1.setPlaceholderText("Write....")
        passwordtext1.setStyleSheet(
            "QLineEdit{"
            "color:gray;"
            "background-color: white;"
            "border: 1px solid black;"
            "border-radius: 20px;"
            "font-size: 15px;"
            "font-family: Segoe UI;"
            "font-weight: bold;"
            "}"
            "QLineEdit:focus{"
            "border : 1px solid pink;"
            "}"
        )
        passwordtext1.setEchoMode(QLineEdit.EchoMode.Password)
        password2 = QLabel("Confirm new password:")
        password2.setStyleSheet(
            "color: black;"
            " font-size: 23px; "
            "font-weight: bold; "
            "font-family: Segoe UI;"

        )
        passwordtext2 = QLineEdit("")
        passwordtext2.setFixedHeight(40)
        passwordtext2.setPlaceholderText("Write....")
        passwordtext2.setStyleSheet(
            "QLineEdit{"
            "color:gray;"
            "background-color: white;"
            "border: 1px solid black;"
            "border-radius: 20px;"
            "font-size: 15px;"
            "font-family: Segoe UI;"
            "font-weight: bold;"
            "}"
            "QLineEdit:focus{"
            "border : 1px solid pink;"
            "}"
        )
        passwordtext2.setEchoMode(QLineEdit.EchoMode.Password)
        Reset = QPushButton("Reset")
        Reset.setFixedHeight(40)
        Reset.setFixedWidth(150)
        Reset.setStyleSheet(
            "QPushButton{"
            "color: white;"
            "background-color: black;"
            "border: none;"
            "border-radius: 20px;"
            "font-size: 20px;"
            "font-family: Segoe UI;"
            "font-weight: bold;"
            "}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(85, 85, 85))
        Reset.setGraphicsEffect(shadow)
        layoutcard.addWidget(password1)
        layoutcard.addWidget(passwordtext1)
        layoutcard.addSpacing(20)
        layoutcard.addWidget(password2)
        layoutcard.addWidget(passwordtext2)
        layoutcard.addSpacing(20)
        layoutcard.addWidget(Reset, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(card)
        layout.addStretch()
        Reset.clicked.connect(self.reseteaza)
        self.setCentralWidget(widgetprincipal)
    def reseteaza(self):
        self.fereastranoua = logare(fereastra_anterioara=self)
        self.fereastranoua.show()
        self.hide()

    def go_back(self):
        if self.fereastra_parola:
            self.fereastra_parola.show()
            self.close()
class Code(QMainWindow):
    def __init__(self, fereastra_send=None):
        super().__init__()
        self.fereastra_send = fereastra_send
        self.setWindowTitle('Fitlog - Forgot your password')
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

        header_layout = QHBoxLayout()

        btn_back = QPushButton("←")
        btn_back.setFixedSize(40, 40)
        btn_back.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_back.setStyleSheet(
            "QPushButton {"
            "   color: black; "
            "   font-size: 26px; "
            "   font-weight: bold; "
            "   background: transparent; "
            "   border: none; "
            "}"
            "QPushButton:hover {"
            "   color: white; "
            "}"
        )
        btn_back.clicked.connect(self.go_back)
        header_layout.addWidget(btn_back)
        header_layout.addStretch()

        textlogin = QLabel("Code")
        textlogin.setStyleSheet("color: white; font-size: 25px; font-weight: bold; font-family: Segoe UI;")
        header_layout.addWidget(textlogin)

        layout.addLayout(header_layout)
        layout.addSpacing(120)
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
        cod = QLabel("Enter your code:")
        cod.setStyleSheet(
            "color: black;"
            " font-size: 25px; "
            "font-weight: bold; "
            "font-family: Segoe UI;"

        )

        layoutcard.addWidget(cod)
        layoutcard.addSpacing(10)
        layout_code_boxes = QHBoxLayout()
        stil_liniuta = "QLineEdit { border: none; border-bottom: 3px solid black; font-size: 22px; font-weight: bold; background: transparent; } QLineEdit:focus { border-bottom: 3px solid pink; }"

        self.inputs = []
        for i in range(4):
            box = QLineEdit()
            box.setFixedWidth(35)
            box.setFixedHeight(45)
            box.setMaxLength(1)
            box.setAlignment(Qt.AlignmentFlag.AlignCenter)
            box.setStyleSheet(stil_liniuta)
            layout_code_boxes.addWidget(box)
            self.inputs.append(box)


        self.inputs[0].textChanged.connect(lambda t: self.inputs[1].setFocus() if t else None)
        self.inputs[1].textChanged.connect(lambda t: self.inputs[2].setFocus() if t else None)
        self.inputs[2].textChanged.connect(lambda t: self.inputs[3].setFocus() if t else None)

        layoutcard.addLayout(layout_code_boxes)
        layoutcard.addSpacing(15)
        intrebare = QPushButton("Resend code")
        intrebare.setCursor(Qt.CursorShape.PointingHandCursor)
        intrebare.setStyleSheet(
            "QPushButton {"
            "   color: black; "
            "   font-size: 16px; "
            "   font-family: 'Segoe UI'; "
            "   background: transparent; "
            "   border: none; "
            "   text-align: left; "
            "}"
            "QPushButton:hover {"
            "   color: blue; "
            "   text-decoration: underline; "
            "}"
        )
        Verify = QPushButton("Verify")
        Verify.setFixedHeight(40)
        Verify.setFixedWidth(160)
        Verify.setStyleSheet(
            "QPushButton{color: white; background-color: black; border-radius: 15px; font-size: 15px; font-weight: bold; font-family: Segoe UI;}")

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(85, 85, 85))
        Verify.setGraphicsEffect(shadow)
        layoutcard.addWidget(intrebare, alignment=Qt.AlignmentFlag.AlignRight)
        layoutcard.addSpacing(20)
        layoutcard.addWidget(Verify, alignment=Qt.AlignmentFlag.AlignHCenter)
        layoutcard.addSpacing(10)
        layout.addWidget(card)
        layout.addStretch()
        Verify.clicked.connect(self.facemparolanoua)
        self.setCentralWidget(widgetprincipal)
    def facemparolanoua(self):
        self.fereastranoua = Parolanoua(fereastra_parola=self)
        self.fereastranoua.show()
        self.hide()
    def go_back(self):
        if self.fereastra_send:
            self.fereastra_send.show()
            self.close()
class Uitareparola(QMainWindow):
    def __init__(self, fereastra_uitare=None):
        super().__init__()
        self.fereastra_uitare = fereastra_uitare
        self.setWindowTitle('Fitlog - Forgot your password')
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
        header_layout = QHBoxLayout()

        btn_back = QPushButton("←")
        btn_back.setFixedSize(40, 40)
        btn_back.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_back.setStyleSheet(
            "QPushButton {"
            "   color: black; "
            "   font-size: 26px; "
            "   font-weight: bold; "
            "   background: transparent; "
            "   border: none; "
            "}"
            "QPushButton:hover {"
            "   color: white; "
            "}"
        )
        btn_back.clicked.connect(self.go_back)
        header_layout.addWidget(btn_back)
        header_layout.addStretch()

        textlogin = QLabel("Code")
        textlogin.setStyleSheet("color: white; font-size: 25px; font-weight: bold; font-family: Segoe UI;")
        header_layout.addWidget(textlogin)

        layout.addLayout(header_layout)
        layout.addSpacing(140)
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
        email = QLabel("Write your email to \nreceive a code:")
        email.setStyleSheet(
            "color: black;"
            " font-size: 20px; "
            "font-weight: bold; "
            "font-family: Segoe UI;"

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
            "font-family: Segoe UI;"
            "font-weight: bold;"
            "}"
            "QLineEdit::focus{"
            "border : 1px solid pink;"
            "}"
        )
        sendcode=QPushButton("Send Code")
        sendcode.setFixedHeight(40)
        sendcode.setFixedWidth(150)
        sendcode.setStyleSheet(
            "QPushButton{"
            "color: white;"
            "background-color: black;"
            "border: none;"
            "border-radius: 20px;"
            "font-size: 15px;"
            "font-family: Segoe UI;"
            "font-weight: bold;"
            "}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(85, 85, 85))
        sendcode.setGraphicsEffect(shadow)
        layoutcard.addWidget(email)
        layoutcard.addWidget(emailtext)
        layoutcard.addSpacing(20)
        layoutcard.addWidget(sendcode, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(card)
        layout.addStretch()
        sendcode.clicked.connect(self.primirecod)
        self.setCentralWidget(widgetprincipal)
    def primirecod(self):
        self.fereastranoua=Code(fereastra_send=self)
        self.fereastranoua.show()
        self.hide()
    def go_back(self):
        if self.fereastra_uitare:
            self.fereastra_uitare.show()
            self.close()

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
        header_layout = QHBoxLayout()

        btn_back = QPushButton("←")
        btn_back.setFixedSize(40, 40)
        btn_back.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_back.setStyleSheet(
            "QPushButton {"
            "   color: black; "
            "   font-size: 26px; "
            "   font-weight: bold; "
            "   background: transparent; "
            "   border: none; "
            "}"
            "QPushButton:hover {"
            "   color: white; "
            "}"
        )
        btn_back.clicked.connect(self.go_back)
        header_layout.addWidget(btn_back)

        header_layout.addStretch()

        textlogin = QLabel("Log in")
        textlogin.setStyleSheet("color: white; font-size: 25px; font-weight: bold; font-family: Segoe UI;")
        header_layout.addWidget(textlogin)

        layout.addLayout(header_layout)
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
            "font-family: Segoe UI;"

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
            "font-family: Segoe UI;"
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
            "font-family: Segoe UI;"

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
            "font-family: Segoe UI;"
            "font-weight: bold;"
            "}"
            "QLineEdit:focus{"
            "border : 1px solid pink;"
            "}"
        )
        passwordtext.setEchoMode(QLineEdit.EchoMode.Password)

        intrebare = QPushButton("Forgot your password?")
        intrebare.setCursor(Qt.CursorShape.PointingHandCursor)
        intrebare.setStyleSheet(
            "QPushButton {"
            "   color: black; "
            "   font-size: 12px; "
            "   font-family: 'Segoe UI'; "
            "   background: transparent; "
            "   border: none; "
            "   text-align: left; "
            "}"
            "QPushButton:hover {"
            "   color: blue; "
            "   text-decoration: underline; "
            "}"
        )
        intrebare.clicked.connect(self.uitareparola)
        Getin=QPushButton("Get in")
        Getin.setFixedHeight(40)
        Getin.setFixedWidth(150)
        Getin.setStyleSheet(
            "QPushButton{"
            "color: white;"
            "background-color: black;"
            "border: none;"
            "border-radius: 20px;"
            "font-size: 20px;"
            "font-family: Segoe UI;"
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
        Getin.clicked.connect(self.intrarecont)
        self.setCentralWidget(widgetprincipal)
    def intrarecont(self):
        self.fereastranoua = paginadestart(fereastra_alege=self)
        self.fereastranoua.show()
        self.hide()
    def uitareparola(self):
        self.fereastranoua = Uitareparola(fereastra_uitare=self)
        self.fereastranoua.show()
        self.hide()

    def go_back(self):
        if self.fereastra_anterioara:
            self.fereastra_anterioara.show()
            self.close()
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
        titlu.setStyleSheet("color: white; font-size: 65px; font-weight: bold; font-family: Segoe UI;")
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
            "font-family: Segoe UI;"
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

        urare = QLabel("Be prepared to change your life!")
        urare.setStyleSheet("color: white; font-size: 40px; font-weight: bold; font-family: Segoe UI;")

        urare.setAlignment(Qt.AlignmentFlag.AlignCenter)
        urare.setWordWrap(True)

        layout.addWidget(urare)

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