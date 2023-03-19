from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QTabWidget, QPushButton, QSplashScreen, QTableWidgetItem, QSplitter
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtGui import QIcon, QPixmap, QBrush
from PyQt5.QtChart import QChartView, QChart, QPieSeries, QPieSlice, QLineSeries
from PyQt5.QtWidgets import QTableWidget, QHeaderView
from ui_i.theme_menu import ThemeMenu
import sys
import json


class Table(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(['ФИО разработчика', 'id_разработчика', 'Отдел разработчика', 'Риск выгорания'])
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Анализатор')
        self.setGeometry(100, 100, 800, 600)

        self.theme_menu = ThemeMenu(self.menuBar())
        self.menuBar().addMenu(self.theme_menu)

        self.tabs = QTabWidget()

        self.home = QWidget()
        self.about = QWidget()

        self.tabs.addTab(self.home, "Главная")
        self.tabs.addTab(self.about, "О нас")

        self.home_layout = QVBoxLayout()
        self.about_layout = QVBoxLayout()

        home_label = QLabel('Таблица "Риск выгорания"')
        about_label = QLabel('Информация о нас')

        self.home_layout.addWidget(home_label)
        self.about_layout.addWidget(about_label)

        self.home_layout.setAlignment(home_label, QtCore.Qt.AlignVCenter)
        self.about_layout.setAlignment(about_label, QtCore.Qt.AlignVCenter)

        self.home_layout.setAlignment(home_label, QtCore.Qt.AlignHCenter)
        self.about_layout.setAlignment(about_label, QtCore.Qt.AlignHCenter)

        self.table = Table()
        self.home_layout.addWidget(self.table)

        splitter = QSplitter(Qt.Vertical)
        self.home_layout.addWidget(splitter)

        # Создаем QPieSeries и добавляем сегменты
        series = QPieSeries()
        slice1 = QPieSlice("Выгорание", 30)
        slice2 = QPieSlice("Психологическая стабильность", 70)
        series.append(slice1)
        series.append(slice2)
        slice1.setExploded(True)
        slice1.setLabelVisible(True)
        slice2.setExploded(True)
        slice2.setLabelVisible(True)

        # Создаем QChart и QChartView для диаграммы
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Диаграмма риска по выгоранию")
        chart.legend().hide()
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        splitter.addWidget(chart_view)
        self.setCentralWidget(splitter)
        chart.resize(300, 300)

        # Назначаем QSplitter в качестве центрального виджета
        central_widget = QWidget()
        central_widget.setLayout(self.home_layout)
        self.setCentralWidget(central_widget)

        self.update_button = QPushButton('Обновить таблицу')
        self.home_layout.addWidget(self.update_button)

        # Добавляем виджет таблицы в QSplitter
        splitter.addWidget(self.table)

        self.home.setLayout(self.home_layout)
        self.about.setLayout(self.about_layout)
        self.setCentralWidget(self.tabs)

        self.update_button.clicked.connect(self.update_table)

    def update_table(self):
        # Очистим таблицу перед добавлением новых данных
        self.table.clearContents()

        # Установим количество строк в таблице
        self.table.setRowCount(100)
        # for row in range(10):
        #     for column in range(4):
        #         self.table.setItem(row, column, QTableWidgetItem())

        self.table.setItem(0, 0, QTableWidgetItem("Элевен Жанна Иоановна"))
        self.table.setItem(0, 1, QTableWidgetItem("567732"))
        self.table.setItem(0, 2, QTableWidgetItem("Программист"))
        self.table.setItem(0, 3, QTableWidgetItem("47%"))

        self.table.setItem(1, 0, QTableWidgetItem("Аметистов Самвел Григорянович"))
        self.table.setItem(1, 1, QTableWidgetItem("507732"))
        self.table.setItem(1, 2, QTableWidgetItem("Системный аналитик"))
        self.table.setItem(1, 3, QTableWidgetItem("69%"))

        self.table.setItem(2, 0, QTableWidgetItem("Петров Петр Петрович"))
        self.table.setItem(2, 1, QTableWidgetItem("567892"))
        self.table.setItem(2, 2, QTableWidgetItem("Инженер-теоретик"))
        self.table.setItem(2, 3, QTableWidgetItem("97%"))

        self.table.setItem(3, 0, QTableWidgetItem("Сидоров Сидор Сидорович"))
        self.table.setItem(3, 1, QTableWidgetItem("600000"))
        self.table.setItem(3, 2, QTableWidgetItem("Системный администратор"))
        self.table.setItem(3, 3, QTableWidgetItem("100%"))

        self.table.setItem(4, 0, QTableWidgetItem("Акакьев Аркадий Самвелович"))
        self.table.setItem(4, 1, QTableWidgetItem("3321321"))
        self.table.setItem(4, 2, QTableWidgetItem("Системный администратор"))
        self.table.setItem(4, 3, QTableWidgetItem("100%"))

        self.table.setItem(5, 0, QTableWidgetItem("Вероникьева Самуила Арменовна"))
        self.table.setItem(5, 1, QTableWidgetItem("654645"))
        self.table.setItem(5, 2, QTableWidgetItem("Системный администратор"))
        self.table.setItem(5, 3, QTableWidgetItem("100%"))
