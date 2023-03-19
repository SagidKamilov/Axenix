from typing import Dict


class Theme:
    def __init__(self, name: str, colors: Dict[str, str]):
        self.name = name
        self.colors = colors


class DarkTheme(Theme):
    def __init__(self):
        name = "dark"
        colors = {
            "background-color": "#212121",
            "text-color": "#fff",
            "accent-color": "#90caf9"
        }
        super().__init__(name, colors)


class LightTheme(Theme):
    def __init__(self):
        name = "light"
        colors = {
            "background-color": "#fff",
            "text-color": "#212121",
            "accent-color": "#1976d2"
        }
        super().__init__(name, colors)


class ThemeManager:
    def __init__(self):
        self.themes = {}

    def add_theme(self, theme: Theme):
        if not isinstance(theme, Theme):
            raise ValueError("The argument should be a Theme instance")

        self.themes[theme.name] = theme

    def get_color(self, color_name: str, theme_name: str):
        theme = self.themes.get(theme_name)
        if not theme:
            raise ValueError(f"Theme '{theme_name}' not found")

        color = theme.colors.get(color_name)
        if not color:
            raise ValueError(f"Color '{color_name}' not found in theme '{theme_name}'")

        return color


theme_manager = ThemeManager()
theme_manager.add_theme(DarkTheme())
theme_manager.add_theme(LightTheme())
