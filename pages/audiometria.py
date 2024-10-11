import flet as ft
import time
class Audiometria():
    def __init__(self) -> None:
        self.numImg = 0
        self.images = ["./assets/hora.png", "./assets/lugar_silencioso.png", "./assets/uso_audifonos.png"]
        self.fre = ['./assets/8000.wav','./assets/9000.wav','./assets/10000.wav','./assets/11000.wav','./assets/12000.wav','./assets/13000.wav','./assets/14000.wav','./assets/15000.wav','./assets/16000.wav','./assets/17000.wav','./assets/18000.wav','./assets/19000.wav','./assets/20000.wav']
        self.vol=[i/10 for i in range(10,-1,-1)]

    import flet as ft

    def test_audiometria(self, page: ft.Page):
        self.page=page
    # Contenedor para la prueba corta
        container_test_small = ft.Container(
            content=ft.Column(
                [
                    ft.Text(value="Prueba corta", size=15,
                            style=ft.TextThemeStyle.TITLE_MEDIUM, 
                            weight=ft.FontWeight.BOLD),
                    ft.Text(value="(general)", size=15,
                            style=ft.TextThemeStyle.TITLE_MEDIUM, 
                            weight=ft.FontWeight.BOLD),
                    ft.Icon(name=ft.icons.HEARING_OUTLINED, color=ft.colors.BLUE, size=40),
                    ft.Text(value="4 Min", size=15,
                            style=ft.TextThemeStyle.LABEL_MEDIUM, 
                            color=ft.colors.GREY_100)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=20,
            
            border_radius=10,
            bgcolor=ft.colors.LIGHT_BLUE_100,
            expand=True,
            height=300,
            margin=10,
            alignment=ft.alignment.center,
            on_click=self.test  ,data=0# Cambiado para usar una lambda
        )

        # Contenedor para la prueba larga
        container_test_big = ft.Container(
            content=ft.Column(
                [
                    ft.Text(value="Prueba larga", 
                            style=ft.TextThemeStyle.TITLE_MEDIUM, 
                            weight=ft.FontWeight.BOLD,size=15),
                    ft.Text(value="(más completa)", size=15,
                            style=ft.TextThemeStyle.TITLE_MEDIUM, 
                            weight=ft.FontWeight.BOLD),
                    ft.Icon(name=ft.icons.HEARING_OUTLINED, color=ft.colors.BLUE, size=40),
                    ft.Text(value="8 Min", size=15,
                            style=ft.TextThemeStyle.LABEL_MEDIUM, 
                            color=ft.colors.WHITE)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=15,
            border_radius=5,
            bgcolor=ft.colors.LIGHT_BLUE_200,
            expand=True,
            height=300,
            margin=10,
            alignment=ft.alignment.center,
            on_click=self.test, data=1  # Cambiado para usar una lambda
        )

        # Fila con ambos contenedores
        self.row_audiometria = ft.Row(
            [
                container_test_small, 
                container_test_big
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,  # Distribuye uniformemente los contenedores
            expand=True
        )
        
        return self.row_audiometria
    def start_test(self,e):
        txt_test=ft.Text(value="Preciona 'si' si escuchas el \nsonido y 'no' si no lo escuchas" ,size=25)
        btn_yes=ft.ElevatedButton("Si",icon=ft.icons.CHECK,on_click=None)
        btn_no=ft.ElevatedButton("No",on_click=None,icon=ft.icons.MUSIC_OFF_SHARP)
        icon_yes=ft.Icon(name=ft.icons.MUSIC_NOTE)
        icon_no=ft.Icon(name=ft.icons.MUSIC_OFF_SHARP)

        test=e.control.data
        for i in range(1,6):
            
            self.row_audiometria.controls.clear()
            self.row_audiometria.controls=[ft.Container(
            content=ft.Text(value=f"La prueba inicia en {i} seg",style=ft.TextThemeStyle.LABEL_MEDIUM, 
                            color=ft.colors.WHITE,size=20),
            padding=20,
            border_radius=10,
            bgcolor=ft.colors.LIGHT_BLUE_200,
            expand=True,
            alignment=ft.alignment.center,
            )]
            time.sleep(1)
            self.page.update()

        if test: #prueba grande
            resultados=[]
            for fre in range(len(self.fre)):
                
                for vol in range(len(self.vol)):
                    print(vol,fre)
                    self.row_audiometria.controls.clear()
                    self.row_audiometria.controls=[
                        ft.Column([
                        txt_test,
                        ft.Audio(src=self.fre[fre],autoplay=True,volume=self.vol[vol]),
                        ft.ElevatedButton("Si",icon=ft.icons.CHECK,on_click=None),
                        ft.ElevatedButton("No",on_click=None,icon=ft.icons.MUSIC_OFF_SHARP)
                        ]),
                    ]

                    self.page.update()

        else:
            # oido derecho
            for fre in range(len(self.fre)):
                for vol in range(len(self.vol)):
                    print(vol,fre)
                    self.row_audiometria.controls.clear()
                    self.row_audiometria.controls=[
                        ft.Column([
                        txt_test,
                        ft.Audio(src=self.fre[fre],autoplay=True,volume=self.vol[vol] ,balance=1),
                        ft.ElevatedButton("Si",icon=ft.icons.CHECK,on_click=None),
                        ft.ElevatedButton("No",on_click=None,icon=ft.icons.MUSIC_OFF_SHARP)
                        ]),
                    ]

                    self.page.update()
            #oido izquierdo
            for fre in range(len(self.fre)):
                for vol in range(len(self.vol)):
                    print(vol,fre)
                    self.row_audiometria.controls.clear()
                    self.row_audiometria.controls=[
                        ft.Column([
                        txt_test,
                        ft.Audio(src=self.fre[fre],autoplay=True,volume=self.vol[vol] ,balance=1),
                        ft.ElevatedButton("Si",icon=ft.icons.CHECK,on_click=None),
                        ft.ElevatedButton("No",on_click=None,icon=ft.icons.MUSIC_OFF_SHARP)
                        ]),
                    ]

                    self.page.update()


    def test(self,e):
        test=e.control.data
        self.row_audiometria.controls.clear()
        self.row_audiometria.controls=[ft.Container(
            content=ft.Column(
                [
                    ft.Text(value="Prueba larga (más completa)", 
                            style=ft.TextThemeStyle.TITLE_MEDIUM, 
                            weight=ft.FontWeight.BOLD),
                    ft.Icon(name=ft.icons.START, color=ft.colors.BLUE, size=40),
                    ft.Text(value="Iniciar prueba", 
                            style=ft.TextThemeStyle.LABEL_MEDIUM, 
                            color=ft.colors.WHITE)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=20,
            border_radius=10,
            bgcolor=ft.colors.LIGHT_BLUE_200,
            expand=True,
            alignment=ft.alignment.center,
            on_click=self.start_test, data=test # Cambiado para usar una lambda
        )]
        self.page.update()

        


        
        
    def next(self, e):
        # Asegurarte de que no te sales del rango de imágenes
        if self.numImg < len(self.images) - 1:
            self.numImg += 1
        else:
            self.page.go("/test/audiometria")  # Reinicia a la primera imagen cuando llegues al final
        
        # Actualiza la imagen en el control existente
        self.image.src = self.images[self.numImg]
        self.page.update()
        
    def audiometria_ins(self, page: ft.Page):
        self.page = page
        
        # Crear la imagen que se va a actualizar
        self.image = ft.Image(
            src=self.images[self.numImg],
            width=page.width - 50,
            fit=ft.ImageFit.CONTAIN,
        )
        
        # Crear el botón que llama a la función next
        btn_next = ft.ElevatedButton(text="Siguente", icon=ft.icons.NAVIGATE_NEXT, on_click=self.next)
        
        # Crear la fila con los controles
        self.row = ft.Row([
            ft.Column([
                ft.Container(
                    content=ft.Row([ft.Text(value="Recomendaciones",size=25,text_align=ft.TextAlign.CENTER,color=ft.colors.WHITE, weight=ft.FontWeight.W_900, selectable=True )],alignment=ft.alignment.center), 
                    bgcolor=ft.colors.BLUE_500,border_radius=10 ,padding=5,
                    ),
                
                ft.Row([self.image]),  # Usar la imagen creada
                # Poner el botón al final del ancho disponible
                ft.Row([btn_next], alignment=ft.MainAxisAlignment.END) 
            ])
        ], alignment=ft.MainAxisAlignment.CENTER)  # Centrar la columna en la pantalla
        
        return self.row
