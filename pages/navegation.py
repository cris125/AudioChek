import flet as ft

class Navegation:
    def navegation(self, page: ft.Page):
        self.page = page

        # Crear diccionarios para gestionar los textos y rutas
        texts = {
            "/ins": ("Instrucciones", ft.icons.INTEGRATION_INSTRUCTIONS_OUTLINED),
            "/test": ("Audiometría", ft.icons.HEARING_OUTLINED),
            "/res": ("Resultados", ft.icons.FACT_CHECK_ROUNDED),
            "/per": ("Perfil", ft.icons.FACT_CHECK_ROUNDED),
        }
        
        # Asignar los valores de texto e íconos según la ruta
        text, icon = texts.get(self.page.route, ("", None))

        # Crear contenedores para cada sección
        sections = []
        for route, (label, icon_name) in texts.items():
            is_active = route == self.page.route  # Verificar si es la ruta activa
            text_size = 11 if is_active else 0  # Asignar tamaño del texto
            container_height = None if is_active else 50  # Asignar ancho del contenedor

            sections.append(
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(label if is_active else "", size=text_size, 
                                    weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                            ft.Icon(name=icon_name, size=35, color=ft.colors.WHITE)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    on_click=self.on_click,
                    data=route.strip("/"),
                    bgcolor=ft.colors.TEAL_200 if is_active else ft.colors.TEAL_400,
                    border_radius=10,
                    expand=True,
                    height=container_height # Ancho del contenedor cuando no está activo
                )
            )

        # Fila con los contenedores
        row = ft.Row(
            sections,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
            expand=True
        )

        return row

    def on_click(self, e):
        self.page.go(f"/{e.control.data}")
        print(e.control.data.capitalize())
