import flet as ft
from styles.hero_style import _dark, _light, toggle_style_sheet, item_style_sheet, add_style_sheet
from .to_do_item import ToDoItem

# Hero content
class Hero(ft.SafeArea):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(minimum=10, maintain_bottom_view_padding=True)
        self.page = page
        self.title: ft.Text = ft.Text("Lista de Tarefas", size=20, weight="w800")
        self.toggle: ft.IconButton = ft.IconButton(**toggle_style_sheet, on_click=lambda e: self.switch(e))
        self.item: ft.TextField = ft.TextField(**item_style_sheet, on_submit=lambda e: self.add_item(e))
        self.add_btn: ft.IconButton = ft.IconButton(**add_style_sheet, on_click=lambda e: self.add_item(e))
        self.to_do_area: ft.Column = ft.Column(expand=True, spacing=18)
        self.counter: ft.Text = ft. Text("0 items", italic=True)

        self.main: ft.Column = ft.Column(
            controls=[
                ft.Row(alignment="spaceBetween", controls=[self.title, self.toggle]),
                ft.Divider(height=20),
                ft.Text("Adicione sua tarefa abaixo:"),
                ft.Row(alignment="spaceBetween", controls=[self.item, self.add_btn]),
                ft.Divider(height=10, color="transparent"), 
                ft.Row(
                    alignment="spaceBetween",
                    controls=[ft.Text("Lista de tarefas a fazer"), self.counter],
                ),
                self.to_do_area,
            ]
        )

        self.content = self.main
    
    def switch(self, e) -> None:
        if self.page.theme_mode == ft.ThemeMode.DARK:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.toggle.icon = ft.icons.LIGHT_MODE_ROUNDED
            self.item.border_color = _light

            for item in self.to_do_area.controls[:]:
                item.border = ft.border.all(1, _light)
        else:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.toggle.icon = ft.icons.DARK_MODE_ROUNDED
            self.item.border_color = _dark

            for item in self.to_do_area.controls[:]:
                item.border = ft.border.all(1, _dark)

        self.page.update()

    def add_item(self, e) -> None:
        if self.item.value != "":
            if self.page.theme_mode == ft.ThemeMode.DARK:
                self.to_do_area.controls.append(ToDoItem(self, self.item.value, "dark"))
            else:
                self.to_do_area.controls.append(ToDoItem(self, self.item.value, "light"))
            
            self.to_do_area.update()
            self.item_size()
            self.item.value = ""
            self.item.update()

        else:
            pass

    def item_size(self) -> None:
        if len(self.to_do_area.controls[:]) == 1:
            self.counter.value = f"{len(self.to_do_area.controls[:])} item"
        else:
            self.counter.value = f"{len(self.to_do_area.controls[:])} items"
        
        self.update()

   