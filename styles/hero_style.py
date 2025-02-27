import flet as ft

# Hero stylesheets
_dark: str = ft.colors.with_opacity(0.5, "white")
_light: str = ft.colors.with_opacity(1, "black")

toggle_style_sheet: dict = {"icon": ft.icons.DARK_MODE_ROUNDED, "icon_size": 18}
add_style_sheet: dict = {"icon": ft.icons.ADD_ROUNDED, "icon_size": 18,
}

item_style_sheet: dict = {
    "height": 50,
    "expand": True,
    "border_color": _dark,
    "cursor_height": 24,
    "content_padding": 15,
    "hint_text": "Descreva a tarefa aqui..." 
}
