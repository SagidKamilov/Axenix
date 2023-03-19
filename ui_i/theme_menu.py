from PyQt5.QtWidgets import QAction, QMenu, QActionGroup


class ThemeMenu(QMenu):
    def __init__(self, parent=None):
        super().__init__("Тема", parent)

        # Создаем действия для выбора тем оформления
        self.light_theme = QAction("Светлая", self, checkable=True)
        self.dark_theme = QAction("Темная", self, checkable=True)

        # Группируем действия в один Toggle-Action для выбора одной из тем
        self.theme_group = QActionGroup(self)
        self.theme_group.addAction(self.light_theme)
        self.theme_group.addAction(self.dark_theme)

        # Выбираем действие по умолчанию
        self.light_theme.setChecked(True)

        # Добавляем действия в меню
        self.addAction(self.light_theme)
        self.addAction(self.dark_theme)
