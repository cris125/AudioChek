import flet as ft

class Navegation:
    def navegation(self, page: ft.Page):
        self.page=page
        # Contenedor para Instrucciones
        con_inst = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Instrucciones", size=11, weight=ft.FontWeight.BOLD,color=ft.colors.WHITE),
                    ft.Icon(name=ft.icons.INTEGRATION_INSTRUCTIONS_OUTLINED, size=35,color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            on_click=self.on_click,
            data="ins",
            bgcolor=ft.colors.TEAL_400,
            border_radius=10,
            expand=True  # Se ajusta al espacio disponible
        )

        # Contenedor para Test Audiometría
        con_test = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Test Audiometría", size=11, weight=ft.FontWeight.BOLD,color=ft.colors.WHITE),
                    ft.Icon(name=ft.icons.HEARING_OUTLINED, size=35,color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            on_click=self.on_click,
            data="test",
            bgcolor=ft.colors.TEAL_400,
            border_radius=10,
            expand=True  # Se ajusta al espacio disponible
        )

        # Contenedor para Resultados
        con_results = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Resultados", size=11, weight=ft.FontWeight.BOLD,color=ft.colors.WHITE),
                    ft.Icon(name=ft.icons.FACT_CHECK_ROUNDED, size=35,color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            on_click=self.on_click,
            data="res",
            bgcolor=ft.colors.TEAL_400,
            border_radius=10,
            expand=True  # Se ajusta al espacio disponible
        )

        con_data = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Perfil", size=11, weight=ft.FontWeight.BOLD,color=ft.colors.WHITE),
                    ft.Icon(name=ft.icons.FACT_CHECK_ROUNDED,  size=35,color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            on_click=self.on_click,
            data="per",
            bgcolor=ft.colors.TEAL_400,
            border_radius=10,
            expand=True  # Se ajusta al espacio disponible
        )
        # Fila con los contenedores
        row = ft.Row(
            [con_inst, con_test, con_results,con_data],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
            expand=True  # Fila expandida para ajustarse al ancho de la pantalla
        )

        return row

    def on_click(self, e):
        if e.control.data == "ins":
            print(self.page.route)
            print("Instrucciones")
        elif e.control.data == "test":
            print("Test Audiometría")
        elif e.control.data == "res":
            print("Resultados")
        elif e.control.data == "per":
            print("Perfil")
