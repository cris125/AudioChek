import flet as ft
from api.api_functions import Api_functions
class Profile:
    def on_change(self, e):
        # Actualizar la fecha seleccionada en el campo correspondiente
        self.text_date.value = f"{e.control.value.strftime('%Y-%m-%d')}"
        self.page.update()

    def save(self, e):
        # Guardar la información del perfil en el almacenamiento del cliente
        e.control.disabled = True 
        self.page.client_storage.set("name", self.name.value)
        self.page.client_storage.set("email", self.email.value)
        self.page.client_storage.set("date", self.text_date.value)
        self.page.client_storage.set("gender", self.gender.value)
        self.page.client_storage.set("occupation", self.occupation.value)
        api=Api_functions()
        self.page.dialog.open = True
        self.page.update()
        api.add_user(id=self.page.client_storage.get("id"),
                     name=self.page.client_storage.get("name"),
                     email=self.page.client_storage.get("email"),
                     date=self.page.client_storage.get("date"),
                     gender=self.page.client_storage.get("gender"),
                     occupation=self.page.client_storage.get("occupation"),)
        # Limpiar la columna y cargar el perfil actualizado
        self.page.dialog.open = False
        self.page.update()
        self.page.go("/")
        self.page.go("/per")

    def del_data(self,e):
        self.page.client_storage.clear()
        self.page.go("/")
        
    def modif(self, e):
        # Limpiar la columna y mostrar los campos de modificación
        self.cont.content=None

        # Campos de texto y botón de fecha
        self.name = ft.TextField(label="Nombre", value=self.name, bgcolor=ft.colors.WHITE, border_radius=8)
        self.email = ft.TextField(label="Email", value=self.email, bgcolor=ft.colors.WHITE, border_radius=8)
        self.text_date = ft.Text(value=self.na_date)
        self.btn_date=ft.ElevatedButton(
            "Fecha de \nNacimiento",width=150,
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda e: self.page.open(
                ft.DatePicker(on_change=self.on_change)
            ),
            style=ft.ButtonStyle(
                bgcolor=ft.colors.LIGHT_BLUE_400,
                color=ft.colors.WHITE
            )
        )
        

        # Dropdown para género
        self.gender = ft.Dropdown(
            label="Género",
            options=[
                ft.dropdown.Option("Masculino"),
                ft.dropdown.Option("Femenino"),
                ft.dropdown.Option("No binario")
            ],
            value=self.gender if self.gender else "Masculino",  # Establecer el valor si está guardado
            bgcolor=ft.colors.WHITE, border_radius=8
        )

        # Dropdown para ocupación
        occupations = ocupaciones = [
            "Ingeniero/a de sistemas", "Administrador/a de empresas", "Médico/a", 
            "Ingeniero/a civil", "Psicólogo/a", "Contador/a", "Abogado/a", "Enfermero/a", 
            "Arquitecto/a", "Economista", "Carpintero/a", "Fontanero/a", "Electricista", 
            "Mecánico/a", "Panadero/a", "Albañil", "Pintor/a", "Soldador/a", 
            "Jardinero/a", "Cocinero/a", "Desarrollador/a web", "Diseñador/a gráfico", 
            "Estudiante", "Trabajador independiente", "Trabajador de la construcción", 
            "Músico/a", "DJ", "Trabajador de fábrica", "Piloto/a", "Personal de aeropuerto", 
            "Leñador/a", "Conductor de ambulancia","otro"
        ]
        self.occupation = ft.Dropdown(
            label="Ocupación",
            options=[ft.dropdown.Option(occ) for occ in occupations],
            value=self.occupation if self.occupation else occupations[0],  # Valor predeterminado
            bgcolor=ft.colors.WHITE, border_radius=8
        )

        # Configurar la interfaz para modificar los datos
        self.cont.content = ft.Column([
            ft.Row([self.name], expand=True, alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([self.email], expand=True, alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([self.text_date, self.btn_date], expand=True, alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([self.gender], expand=True, alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([self.occupation], expand=True, alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.ElevatedButton(
                "Guardar Cambios",
                on_click=self.save,
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.CYAN_600,
                    color=ft.colors.WHITE
                )
            )], alignment=ft.MainAxisAlignment.CENTER)
        ],scroll=True)
        self.page.update()

    def profile(self, page: ft.Page):
        self.page = page

        # Obtener los datos del almacenamiento local
        self.name = self.page.client_storage.get("name")
        self.email = self.page.client_storage.get("email")
        self.na_date = self.page.client_storage.get("date")
        self.gender = self.page.client_storage.get("gender")
        self.occupation = self.page.client_storage.get("occupation")

        # Botón para modificar datos
        self.btn_mod = ft.ElevatedButton(
            "Modificar datos",
            on_click=self.modif,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.LIGHT_BLUE_500,
                color=ft.colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=10),  # Borde redondeado para el botón
                shadow_color=ft.colors.BLUE_GREY_900  # Sombras más marcadas
            )
        )
        self.btn_del_data = ft.ElevatedButton(
            "Borrar datos ",
            on_click=self.del_data,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.RED_300,
                color=ft.colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=10),  # Borde redondeado para el botón
                shadow_color=ft.colors.BLUE_GREY_900  # Sombras más marcadas
            )
        )

        # Crear la vista del perfil con estilo mejorado
        self.cont = ft.Container(
            content=ft.Column([
                ft.Text(value=f"Nombre: {self.name}", color=ft.colors.BLACK, size=18, weight="bold"),
                ft.Divider(height=1, color=ft.colors.BLUE_GREY_200),  # Línea divisoria
                ft.Text(value=f"Fecha de nacimiento: {self.na_date}", color=ft.colors.BLACK, size=16),
                ft.Divider(height=1, color=ft.colors.BLUE_GREY_200),
                ft.Text(value=f"Ocupación: {self.occupation}", color=ft.colors.BLACK, size=16),
                ft.Divider(height=1, color=ft.colors.BLUE_GREY_200),
                ft.Text(value=f"Email: {self.email}", color=ft.colors.BLACK, size=16),
                ft.Divider(height=1, color=ft.colors.BLUE_GREY_200),
                ft.Text(value=f"Género: {self.gender}", color=ft.colors.BLACK, size=16),
                self.btn_mod , self.btn_del_data
            ], spacing=10,scroll=True),  # Añadir espacio entre los elementos
            margin=10,
            bgcolor=ft.colors.LIGHT_BLUE_50,  # Fondo azul claro
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

        # Aplicar fondo suave en azul
        return ft.Row([self.cont], alignment=ft.MainAxisAlignment.CENTER,expand=True)
        
