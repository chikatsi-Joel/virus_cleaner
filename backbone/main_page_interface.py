from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget
from qfluentwidgets import *
from PyQt5.QtGui import QFont, QIcon
from qfluentwidgets import FluentIcon as FIF
from interface.home_page_interface import barre_title_interface
from qframelesswindow import FramelessWindow, StandardTitleBar
import os, sys, subprocess, threading


class splash_screen(FramelessWindow):

    def __init__(self):
        super().__init__()
        self.resize(700, 520)
        self.setWindowTitle('Clean Windows')
        self.setWindowIcon(QIcon(os.path.join(sys._MEIPASS, 'interface/Images/virus.png')))
        self.vbox = QVBoxLayout(self)
        self.title = TitleLabel("Clean Windows")
        self.description = CaptionLabel("@copiright. Licence GNU, Developpé par Chikatsi Joel")
        self.description.setFont(QFont("ubuntu", 10, 12, True))
        hbx = QHBoxLayout()
        self.splashScreen = SplashScreen(self.windowIcon())
        self.slider = IndeterminateProgressBar(start= True)
        tit = TabBar()
        hbx.addWidget(self.description)
        self.splashScreen.setTitleBar(tit)
        self.vbox.addSpacerItem(QSpacerItem(30, 80))
        self.vbox.addWidget(self.splashScreen)
        self.vbox.addWidget(self.title)
        self.vbox.addWidget(self.slider)
        self.vbox.addLayout(hbx)

        self.title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.description.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        self.setStyleSheet("background-color: white;")

        self.center()
        self.show()

        self.createSubInterface()

        self.splashScreen.finish()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        widget_size = self.geometry()
        self.move((screen.width() - widget_size.width()) // 2, (screen.height() - widget_size.height()) // 2)  


    def createSubInterface(self):
        loop = QEventLoop(self)
        QTimer.singleShot(2000, loop.quit)
        loop.exec()

class main_interface_page(FramelessWindow) :
    def __init__(self, parent: QWidget | None = None) -> None:
        super(main_interface_page, self).__init__(parent)
        self.central = QVBoxLayout(self)
        
        title_bar = StandardTitleBar(self)
        title_bar.setIcon(os.path.join(sys._MEIPASS, "interface/Images/virus.png"))
        title_bar.setTitle("Clean Virus")
        self.setTitleBar(title_bar)
        self.barr_title = barre_title_interface(self)
        self.valider = PrimaryPushButton(text = "Lancer le nettoyage")
        self.description = CaptionLabel("powered by Gradi - Email : kappachikatsi@gmail.com")
        self.description.setFont(QFont("ubuntu", 9, 10, True))
        self.slide = IndeterminateProgressRing(start= True)
        self.slide.setHidden(True)

        self.central.addSpacerItem(QSpacerItem(30, 80))
        self.central.addWidget(self.barr_title)
        self.central.addWidget(self.slide, 0, Qt.AlignmentFlag.AlignHCenter)
        self.central.addSpacerItem(QSpacerItem(30, 50))
        self.central.addWidget(self.valider, 0, Qt.AlignmentFlag.AlignHCenter)
        self.central.addSpacerItem(QSpacerItem(30, 50))
        self.central.addWidget(self.description, 0, Qt.AlignmentFlag.AlignHCenter)

        self.setWindowIcon(QIcon(os.path.join(sys._MEIPASS, "interface/Images/virus.png")))

        self.valider.clicked.connect(self.slots_connect)

    
    def slots_connect(self) : 
        self.slide.setHidden(False)
        script_path = os.path.join(sys._MEIPASS, "backbone/daemon_clean.bat")
        try :
            subprocess.Popen(script_path, shell= True)
        except Exception as e :
            InfoBar.warning(
                "Warning",
                "Le script n'a pas pu être exécuté en tant qu'admin",
                parent = self,
                duration= 2500
            )
            return
        InfoBar.success(
                "Success",
                "Exécution réussie avec succès..",
                parent = self,
                duration = 2500
            )
        self.slide.setVisible(False)
            
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        widget_size = self.geometry()
        self.move((screen.width() - widget_size.width()) // 2, (screen.height() - widget_size.height()) // 2)  


if __name__ == '__main__' :
    import sys
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps) 
    app = QApplication(sys.argv)
    splas = splash_screen()
    splas.show()
    application = main_interface_page()
    splas.close()
    application.show()
    app.exec()

