import flet as ft

class Navegation:
    def navegation(self, page: ft.Page):
        self.page = page

        # Crear diccionarios para gestionar los textos y rutas
        texts = {
            "/ins": ("Instrucciones", ft.icons.INTEGRATION_INSTRUCTIONS_OUTLINED),
            "/test": ("Audiometría", ft.icons.NOISE_CONTROL_OFF_SHARP),
            "/res": ("Resultados", ft.icons.FACT_CHECK_ROUNDED),
            "/per": ("Perfil", ft.icons.ACCOUNT_CIRCLE),
        }
        
        # Colores
        active_color = ft.colors.BLUE_600
        inactive_color = ft.colors.BLUE_300
        text_color_active = ft.colors.WHITE
        text_color_inactive = ft.colors.BLACK
        
        # Crear contenedores para cada sección
        sections = []
        for route, (label, icon_name) in texts.items():
            is_active = route == self.page.route  # Verificar si es la ruta activa
            text_size = 11 if is_active else 0  # Ajustar tamaño del texto
            container_height = None if is_active else 50  # Alto del contenedor

            sections.append(
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(label if is_active else "", size=text_size, 
                                    weight=ft.FontWeight.BOLD, color=text_color_active if is_active else text_color_inactive),
                            ft.Icon(name=icon_name, size=30, color=text_color_active if is_active else text_color_inactive)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    on_click=self.on_click,
                    data=route.strip("/"),
                    bgcolor=active_color if is_active else inactive_color,
                    border_radius=10,
                    expand=True,
                    height=container_height
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
