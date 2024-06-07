import flet as ft
from styles.to_do_item_style import _dark, _light, todo_item_style_sheet, delete_style_sheet

# Todo item content
class ToDoItem(ft.Container):
    def __init__(self, hero: object, description: str, theme: str) -> None:
        if theme == "dark":
            todo_item_style_sheet["border"] = ft.border.all(1, _dark)
        else:
            todo_item_style_sheet["border"] = ft.border.all(1, _light)

        super().__init__(**todo_item_style_sheet)
        self.hero: object = hero
        self.description: str = description
        self.tick: ft.Checkbox = ft.Checkbox(on_change=lambda e: self.strike(e))
        self.text: ft.Text = ft.Text(spans=[ft.TextSpan(text=self.description)], size=14)
        self.delete_btn: ft.IconButton = ft.IconButton(**delete_style_sheet, on_click=lambda e: self.delete())

        self.content: ft.Row = ft.Row(
            alignment="spaceBetween",
            controls=[
                ft.Row(controls=[self.tick, self.text]),
                self.delete_btn
            ]
        )
    
    def strike(self, e) -> None:
        if e.control.value == True:
            self.text.spans[0].style = ft.TextStyle(
                decoration=ft.TextDecoration.LINE_THROUGH,
                decoration_thickness=2
            )

        else:
            self.text.spans[0].style = ft.TextStyle()

        self.update()

    def delete(self) -> None:
        self.hero.to_do_area.controls.remove(self)
        self.hero.to_do_area.update()
        self.hero.item_size()