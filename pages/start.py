import flet as ft
import time
import hashlib
from api.api_functions import Api_functions


class Start:
    def id_unique(self):
        data=self.txt_name.value
        str_id = str(time)+data
        id = hashlib.sha256(str_id.encode()).hexdigest()
        return(id)
    def on_cl(self, e):
        e.control.disabled = True 
        id_un=self.id_unique()
        # Guardar la información en el almacenamiento local
        self.page.client_storage.set("name", self.txt_name.value)
        self.page.client_storage.set("email", self.txt_email.value)
        self.page.client_storage.set("date", self.date_age.value)
        self.page.client_storage.set("gender", self.gender.value)  # Guardar el género seleccionado
        self.page.client_storage.set("occupation", self.occupation.value)  # Guardar la ocupación seleccionada
        self.page.client_storage.set("id",id_un ) 
        self.page.dialog.open = True
        self.page.update()
        api=Api_functions()
        api.add_user(id=id_un,name=self.txt_name.value,
                     email=self.txt_email.value,
                     date=self.date_age.value,
                     gender=self.gender.value,
                     occupation=self.occupation.value)
        self.page.dialog.open = False
        self.page.update()
        self.page.go("/per")

    def on_change(self, e):
        # Actualizar la fecha de nacimiento seleccionada
        self.date_age.value = f"{e.control.value.strftime('%Y-%m-%d')}"
        self.page.update()

    def start(self, page: ft.Page):
        self.page = page
       
        
        # Crear campos de texto para nombre y correo
        self.txt_name = ft.TextField(label="Nombre", expand=True)
        self.txt_email = ft.TextField(label="Correo Electrónico", expand=True)
        
        # Campo de fecha de nacimiento, solo lectura
        self.date_age = ft.TextField(label="Fecha de Nacimiento", read_only=True, expand=True)
        
        # Botón para seleccionar la fecha de nacimiento
        btn_date = ft.ElevatedButton(
            "Seleccionar\nFecha de\nNacimiento",width=150,
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda e: self.page.open(
                ft.DatePicker(on_change=self.on_change)
            )
        )
        
        # Desplegable para género
        self.gender = ft.Dropdown(
            label="Género",
            options=[
                ft.dropdown.Option("Masculino"),
                ft.dropdown.Option("Femenino"),
                ft.dropdown.Option("No binario"),
            ],
            expand=True,
        )

        # Desplegable para ocupación
        ocupaciones = [
            "Ingeniero/a de sistemas", "Administrador/a de empresas", "Médico/a", 
            "Ingeniero/a civil", "Psicólogo/a", "Contador/a", "Abogado/a", "Enfermero/a", 
            "Arquitecto/a", "Economista", "Carpintero/a", "Fontanero/a", "Electricista", 
            "Mecánico/a", "Panadero/a", "Albañil", "Pintor/a", "Soldador/a", 
            "Jardinero/a", "Cocinero/a", "Desarrollador/a web", "Diseñador/a gráfico", 
            "Estudiante", "Trabajador independiente", "Trabajador de la construcción", 
            "Músico/a", "DJ", "Trabajador de fábrica", "Piloto/a", "Personal de aeropuerto", 
            "Leñador/a", "Conductor de ambulancia"
        ]
        options_ocupation = [ft.dropdown.Option(i) for i in ocupaciones]
        self.occupation = ft.Dropdown(
            label="Ocupación",
            options=options_ocupation,
            expand=True
        )

        # Botón para enviar el formulario
        btn_submit = ft.ElevatedButton(text="Enviar", on_click=self.on_cl,style=ft.ButtonStyle(
                    bgcolor=ft.colors.CYAN_600,
                    color=ft.colors.WHITE
                ))

        # Organizar los controles en una fila para la fecha y el botón de fecha
        self.row_data = ft.Row([self.date_age, btn_date], expand=True)

        # Organizar los controles en una columna
        form_column = ft.Column([
            ft.Text(value="llena la información",style=ft.TextThemeStyle.TITLE_MEDIUM, 
                            weight=ft.FontWeight.BOLD),
            self.txt_name, self.txt_email, self.row_data, self.gender, self.occupation, btn_submit], expand=True)
        
        continer_2=ft.Container(
            content= ft.Column([
                ft.Container(
                content=ft.Row(
                    [ft.Text(value="AudioChek",style=ft.TextThemeStyle.TITLE_MEDIUM, 
                            weight=ft.FontWeight.BOLD),
                     ft.Image(src="./assets/logo.png" ,width=65)],alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
                ),
                
            ] , expand=True ,spacing=10),
            margin=10,
            bgcolor=ft.colors.WHITE,  # Fondo azul claro
            height=100,
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
        continer=ft.Container(
            content= form_column ,
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
        
        return ft.Column([continer_2,continer],expand=True,scroll=True)
