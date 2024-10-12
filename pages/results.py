import flet as ft
class Results():
    def results(self,page:ft.Page):
        self.page=page
        if self.page.client_storage.get("res_test_big"):
               pass
        else:
            continer=ft.Container(
                 content=ft.Column([
                    ft.Text(value="Sin datos PRUEBA LARGA",style=ft.TextThemeStyle.LABEL_MEDIUM, 
                            color=ft.colors.WHITE)
                 ]),
                margin=10,
                bgcolor=ft.colors.LIGHT_BLUE_50,  # Fondo azul claro
                width=self.page.width/2.5,
                expand=True,
                padding=20,
                border_radius=20,  # Bordes más redondeados
                border=ft.border.all(2, ft.colors.BLUE_GREY_300),  # Bordes gris claro
                shadow=ft.BoxShadow(  # Añadir sombra suave
                    spread_radius=2,
                    blur_radius=15,
                    color=ft.colors.BLUE_GREY_400,
                    offset=ft.Offset(5, 5)
                )
            )
        if self.page.client_storage.get("res_test_small"):
             pass
        else:
            continer=ft.Container(
                 content=ft.Column([
                    ft.Text(value="Sin datos PRUEBA CORTA",style=ft.TextThemeStyle.LABEL_MEDIUM, 
                            color=ft.colors.WHITE)
                 ]),
                margin=10,
                bgcolor=ft.colors.LIGHT_BLUE_50,  # Fondo azul claro
                width=self.page.width/2.5,
                expand=True,
                padding=20,
                border_radius=20,  # Bordes más redondeados
                border=ft.border.all(2, ft.colors.BLUE_GREY_300),  # Bordes gris claro
                shadow=ft.BoxShadow(  # Añadir sombra suave
                    spread_radius=2,
                    blur_radius=15,
                    color=ft.colors.BLUE_GREY_400,
                    offset=ft.Offset(5, 5)
                )
            )