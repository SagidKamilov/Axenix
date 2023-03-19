from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QTabWidget, QPushButton, QSplashScreen, QTableWidgetItem, QSplitter
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtChart import QChartView, QChart, QPieSeries, QPieSlice
from PyQt5.QtWidgets import QTableWidget, QHeaderView
from ui_i.theme_menu import ThemeMenu


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

        self.update_button = QPushButton('Обновить таблицу')
        self.home_layout.addWidget(self.update_button)

        splitter = QSplitter(Qt.Horizontal)
        self.home_layout.addWidget(splitter)

        # Создаем QPieSeries и добавляем сегменты
        series = QPieSeries()
        slice1 = QPieSlice("Slice 1", 10)
        slice2 = QPieSlice("Slice 2", 20)
        slice3 = QPieSlice("Slice 3", 30)
        series.append(slice1)
        series.append(slice2)
        series.append(slice3)
        slice2.setExploded(True)
        slice2.setLabelVisible(True)

        # Создаем QChart и QChartView для диаграммы
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Example Pie Chart")
        chart.legend().hide()
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        splitter.addWidget(chart_view)

        # Назначаем QSplitter в качестве центрального виджета
        central_widget = QWidget()
        central_widget.setLayout(self.home_layout)
        self.setCentralWidget(central_widget)

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

        # Добавим данные в таблицу
        self.table.setItem(0, 0, QTableWidgetItem("Иванов Иван Иванович"))
        self.table.setItem(0, 1, QTableWidgetItem("1"))
        self.table.setItem(0, 2, QTableWidgetItem("Отдел 1"))
        self.table.setItem(0, 3, QTableWidgetItem("Средний"))

        self.table.setItem(1, 0, QTableWidgetItem("Петров Петр Петрович"))
        self.table.setItem(1, 1, QTableWidgetItem("2"))
        self.table.setItem(1, 2, QTableWidgetItem("Отдел 2"))
        self.table.setItem(1, 3, QTableWidgetItem("Высокий"))

        self.table.setItem(2, 0, QTableWidgetItem("Сидоров Сидор Сидорович"))
        self.table.setItem(2, 1, QTableWidgetItem("3"))
        self.table.setItem(2, 2, QTableWidgetItem("Отдел 1"))
        self.table.setItem(2, 3, QTableWidgetItem("Низкий"))
