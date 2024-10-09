import flet as ft
class LayoutManager:
    def __init__(self, main_row: ft.Row, navigation_row: ft.Row):
        self.main_row = main_row
        self.navigation_row = navigation_row

    def build_layout(self):
        layout = ft.Column(
            [
                ft.Container(
                    content=self.main_row,
                    expand=20,  # Ocupa el 90% de la pantalla
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=self.navigation_row,
                    expand=3,  # Ocupa el 10% de la pantalla
                    alignment=ft.alignment.center,
                     # Fondo para diferenciar la navegación
                ),
            ],
            expand=True  # Para ocupar todo el espacio disponible
        )
        return layout
