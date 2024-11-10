# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_w_game_scraper(object):
    def setupUi(self, w_game_scraper):
        if not w_game_scraper.objectName():
            w_game_scraper.setObjectName(u"w_game_scraper")
        w_game_scraper.resize(441, 368)
        self.gridLayout = QGridLayout(w_game_scraper)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tw_tags = QTableWidget(w_game_scraper)
        self.tw_tags.setObjectName(u"tw_tags")
        self.tw_tags.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout.addWidget(self.tw_tags, 3, 0, 1, 1)

        self.pb_start = QPushButton(w_game_scraper)
        self.pb_start.setObjectName(u"pb_start")

        self.gridLayout.addWidget(self.pb_start, 2, 0, 1, 2)

        self.groupBox = QGroupBox(w_game_scraper)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rb_popular_releases = QRadioButton(self.groupBox)
        self.rb_popular_releases.setObjectName(u"rb_popular_releases")

        self.gridLayout_2.addWidget(self.rb_popular_releases, 1, 0, 1, 1)

        self.rb_most_played_games = QRadioButton(self.groupBox)
        self.rb_most_played_games.setObjectName(u"rb_most_played_games")

        self.gridLayout_2.addWidget(self.rb_most_played_games, 0, 0, 1, 1)

        self.rb_hot_releases = QRadioButton(self.groupBox)
        self.rb_hot_releases.setObjectName(u"rb_hot_releases")

        self.gridLayout_2.addWidget(self.rb_hot_releases, 1, 1, 1, 1)

        self.rb_trending_games = QRadioButton(self.groupBox)
        self.rb_trending_games.setObjectName(u"rb_trending_games")

        self.gridLayout_2.addWidget(self.rb_trending_games, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)

        self.label = QLabel(w_game_scraper)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(w_game_scraper)

        QMetaObject.connectSlotsByName(w_game_scraper)
    # setupUi

    def retranslateUi(self, w_game_scraper):
        w_game_scraper.setWindowTitle(QCoreApplication.translate("w_game_scraper", u"Steam Database Scraper | by Mathias Dick", None))
        self.pb_start.setText(QCoreApplication.translate("w_game_scraper", u"Start Scraper", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_game_scraper", u"Select what table to scrape", None))
        self.rb_popular_releases.setText(QCoreApplication.translate("w_game_scraper", u"Popular Releases", None))
        self.rb_most_played_games.setText(QCoreApplication.translate("w_game_scraper", u"Most Played Games", None))
        self.rb_hot_releases.setText(QCoreApplication.translate("w_game_scraper", u"Hot Releases", None))
        self.rb_trending_games.setText(QCoreApplication.translate("w_game_scraper", u"Trending Games", None))
        self.label.setText(QCoreApplication.translate("w_game_scraper", u"Find the most common game categories", None))
    # retranslateUi

