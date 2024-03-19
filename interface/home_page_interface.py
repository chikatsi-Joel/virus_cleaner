from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget
from qfluentwidgets import *
from qfluentwidgets import FluentIcon as FIF
import os, sys


class barre_title_interface(QWidget) :
    def __init__(self, parent: QWidget | None = None) -> None:
        super(barre_title_interface, self).__init__(parent)
        self.central = QVBoxLayout(self)
        
        hbox = QHBoxLayout()
        self.icon = ImageLabel(os.path.join(sys._MEIPASS, "interface/Images/virus.png"))
        self.icon.scaledToWidth(100)
        self.icon.setBorderRadius(8, 0, 8, 0)

        self.title = SubtitleLabel("Clean Windows")
        self.link = HyperlinkButton("https://github.com/chikatsi-Joel", "lien de téléchargement", icon = FIF.DOWNLOAD)
        v = QVBoxLayout()
        v.addStretch()
        v.addWidget(self.title), v.addWidget(self.link)
        v.addStretch()
        hbox.addStretch()
        hbox.addWidget(self.icon), hbox.addLayout(v)
        hbox.addStretch()

        self.central.addLayout(hbox)
