import flet as ft
from components.hero import Hero

def main(page: ft.Page) -> None:
    page.theme_mode = ft.ThemeMode.DARK
    theme = ft.Theme()
    page.theme = theme

    hero: object = Hero(page)
    page.add(hero)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)