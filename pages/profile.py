import flet as ft

import flet as ft

class Profile:
    def on_change(self, e):
        # Actualizar la fecha seleccionada en el campo correspondiente
        self.text_date.value = f"{e.control.value.strftime('%Y-%m-%d')}"
        self.page.update()

    def save(self, e):
        # Guardar la información del perfil en el almacenamiento del cliente
        self.page.client_storage.set("name",  self.name.value)
        self.page.client_storage.set("email",  self.email.value)
        self.page.client_storage.set("date",  self.text_date.value)

        # Limpiar la columna y cargar el perfil actualizado
        self.colum.controls.clear()
        self.page.go("/ins")
        self.page.go("/per")

    def modif(self, e):
        # Limpiar la columna y mostrar los campos de modificación
        self.colum.controls.clear()

        # Campos de texto y botón de fecha
        self.name = ft.TextField(label="Nombre", value=self.name, bgcolor=ft.colors.WHITE, border_radius=8)
        self.email = ft.TextField(label="Email", value=self.email, bgcolor=ft.colors.WHITE, border_radius=8)
        self.text_date = ft.Text(value=self.na_date)
        self.btn_date = ft.ElevatedButton(
            "Fecha de Nacimiento",
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda e: self.page.open(
                ft.DatePicker(on_change=self.on_change)
            ),
            style=ft.ButtonStyle(
                bgcolor=ft.colors.LIGHT_BLUE_400,
                color=ft.colors.WHITE
            )
        )

        # Configurar la interfaz para modificar los datos
        self.colum.controls = [
            ft.Row([ self.name], expand=True, alignment=ft.alignment.center),
            ft.Row([ self.email], expand=True, alignment=ft.alignment.center),
            ft.Row([ self.text_date, self.btn_date], expand=True, alignment=ft.alignment.center),
            ft.Row([ft.ElevatedButton(
                "Guardar Cambios",
                on_click=self.save,
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.CYAN_600,
                    color=ft.colors.WHITE
                )
            )], alignment=ft.alignment.center)
        ]
        self.page.update()

    def profile(self, page: ft.Page):
        self.page = page

        # Obtener los datos del almacenamiento local
        self.name = self.page.client_storage.get("name")
        self.email = self.page.client_storage.get("email")
        self.na_date = self.page.client_storage.get("date")

        # Botón para modificar datos
        self.btn_mod = ft.ElevatedButton(
            "Modificar datos",
            expand=True,
            on_click=self.modif,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.LIGHT_BLUE_500,
                color=ft.colors.WHITE
            )
        )

        # Crear la vista del perfil
        self.colum = ft.Column([
            ft.Row([ft.Text(value=f"Nombre: {self.name}", color=ft.colors.BLACK)], expand=True, alignment=ft.alignment.center),
            ft.Row([ft.Text(value=f"Email: {self.email}", color=ft.colors.BLACK)], expand=True, alignment=ft.alignment.center),
            ft.Row([ft.Text(value=f"Fecha de nacimiento: {self.na_date}", color=ft.colors.BLACK)], expand=True, alignment=ft.alignment.center),
            self.btn_mod
        ], expand=True)

        # Aplicar fondo suave en azul
        return ft.Container(
            content=ft.Row([self.colum], alignment=ft.alignment.center,scroll=True),
            bgcolor=ft.colors.LIGHT_BLUE_50,  # Fondo azul claro
            padding=20,
            border_radius=10,
        )
