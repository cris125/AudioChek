import flet as ft
import random 
import time
from api.api_functions import Api_functions
class Audiometria():
    def __init__(self) -> None:
        self.numImg = 0
        self.images = ["./assets/hora.png", "./assets/vol_max.png", "./assets/lugar_silencioso.png","./assets/uso_audifonos.png"]
        self.fre = ['./assets/8000.wav','./assets/10000.wav','./assets/12000.wav','./assets/12000.wav','./assets/15000.wav','./assets/16000.wav','./assets/17000.wav','./assets/18000.wav','./assets/19000.wav','./assets/20000.wav']
        self.fre_dic={'./assets/8000.wav': 8000,'./assets/10000.wav': 10000,'./assets/12000.wav': 12000,'./assets/15000.wav': 15000,'./assets/16000.wav': 16000,'./assets/17000.wav': 17000,'./assets/18000.wav': 18000,'./assets/19000.wav': 19000,'./assets/20000.wav': 20000}

        random.shuffle(self.fre )
        self.vol=[0.03,0.07,0.15,0.2,0.4,0.6,0.8,0.9,1]
        self.current_fre=0
        self.current_vol=0
        self.resul=[]
        self.api=Api_functions()

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
    
    def next_test(self, e, balance=0):
        e.control.disabled = True
        data = e.control.data
        self.current_audio.release()
        self.current_audio.update()

        if data == "yes":
            # Si el usuario escucha el sonido
            self.resul.append([self.fre_dic[self.fre[self.current_fre]], self.vol[self.current_vol] ,balance] )
            # Avanzar en la frecuencia
            if self.current_fre < len(self.fre) - 1:
                self.current_fre += 1
                self.current_vol = 0        
                self.update_test(balance)
            else:
                # si el balance es 1 iniciar la siguente prueba con el balance de 0
                if balance == 1:
                        self.current_fre = 0
                        self.current_vol = 0 
                        balance=-1
                        self.update_test(balance)
                else:
                    if balance == -1:
                        #guarda la prueba larga
                        self.page.client_storage.set("res_test_big",self.resul)
                        self.page.dialog.open = True
                        self.page.update()
                        self.api.add_aud_com(self.resul,self.page.client_storage.get("id"))
                        self.page.dialog.open = False
                        self.page.update()
                        self.resul=[]
                    else:
                        #guarda la prueba corta
                        self.page.client_storage.set("res_test_small",self.resul)
                        self.page.dialog.open = True
                        self.page.update()
                        self.api.add_aud_sim(self.resul,self.page.client_storage.get("id"))
                        self.page.dialog.open  = False
                        self.page.update()
                        self.resul=[]

                    self.page.go("/res")  # Si llegamos al final, mostrar resultados
        else:
            # Si no escucha, avanzamos en el volumen
            if self.current_vol < len(self.vol) - 1:
                self.current_vol += 1
                self.update_test(balance)
            else:
            # si el volumen ya es el maximo se guarda como none y se avanza a la siguente frecuencia
                self.resul.append([self.fre_dic[self.fre[self.current_fre]],None,balance])  
                
                if self.current_fre < len(self.fre) - 1:
                    self.current_fre += 1
                    self.current_vol = 0 
                    self.update_test(balance)
                else:
                    if balance == 1:
                        self.current_fre = 0
                        self.current_vol = 0 
                        balance=-1
                        self.update_test(balance)
                    else:
                        if balance == -1:
                            self.page.client_storage.set("res_test_big",self.resul)
                            self.page.dialog.open  = True
                            self.page.update()
                            self.api.add_aud_com(self.resul,self.page.client_storage.get("id"))
                            self.page.dialog.open  = False
                            self.page.update()
                            self.resul=[]
                        else:
                            self.page.client_storage.set("res_test_small",self.resul)
                            self.page.dialog.open  = True
                            self.page.update()
                            self.api.add_aud_sim(self.resul,self.page.client_storage.get("id"))
                            self.page.dialog.open  = False
                            self.page.update()
                            self.resul=[]

                        self.page.go("/res")  # Si llegamos al final, mostrar resultados
                        
                    

        # Actualizamos la interfaz con la nueva prueba


    def update_test(self, balance):
        """Actualiza la interfaz y reproduce el audio con la frecuencia y volumen actual."""
        
        cont=ft.Container(
                    content=ft.Column([
                        ft.Text(value=f"Presiona 'Sí' si escuchas el sonido, No' si no lo escuchas",
                                    style=ft.TextThemeStyle.LABEL_MEDIUM, 
                                    color=ft.colors.WHITE, 
                                    size=20,expand=True),

                        ],alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,expand=True
                ),
                    
                    padding=20,
                    border_radius=10,
                    bgcolor=ft.colors.LIGHT_BLUE_500,
                    height=self.page.height/4,
                    alignment=ft.alignment.center,
                )
                # Limpiamos el contenido anterior y mostramos la nueva prueba
        self.row_audiometria.controls.clear()
        
        self.current_audio=ft.Audio(src=self.fre[self.current_fre], autoplay=True, volume=self.vol[self.current_vol], balance=balance)
        self.row_audiometria.controls.append(
            ft.Column([
                cont,
                self.current_audio,
                ft.ElevatedButton("Sí", icon=ft.icons.CHECK, on_click=lambda e: self.next_test(e, balance), data="yes"),
                ft.ElevatedButton("No", on_click=lambda e: self.next_test(e, balance), icon=ft.icons.MUSIC_OFF_SHARP, data="no")
            ],expand=True)
        )

        self.page.update()
        

    def audiometria_test_big(self):
        """Realiza la prueba grande para ambos oídos."""
        self.update_test(balance=1)  # Comenzamos con el oído derecho (balance 1) #
        # Luego pasaremos al izquierdo una vez que termine el derecho (esto puede manejarse con estados adicionales)

    def audiometria_test_small(self, e=None):
        """Realiza la prueba pequeña."""
        self.update_test(balance=0)  # Sin balance (prueba general)

    def start_test(self, e):
        """Inicia la prueba con una cuenta regresiva."""
        test = e.control.data
        for i in range(1, 4):
            
            # Limpiamos y mostramos la cuenta regresiva
            self.row_audiometria.controls.clear()
            self.row_audiometria.controls.append(
                ft.Container(
                    content=ft.Text(value=f"La prueba inicia en {i} segundos",
                                    style=ft.TextThemeStyle.LABEL_MEDIUM, 
                                    color=ft.colors.WHITE, 
                                    size=20),
                    padding=20,
                    border_radius=10,
                    bgcolor=ft.colors.LIGHT_BLUE_200,
                    expand=True,
                    alignment=ft.alignment.center,
                )
            )
            self.page.update()
            time.sleep(1)

        if test:  # Prueba grande
            self.audiometria_test_big()
        else:  # Prueba pequeña
            self.audiometria_test_small()
        

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
            width=350,
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
            ],scroll=True)
        ], alignment=ft.MainAxisAlignment.CENTER)  # Centrar la columna en la pantalla
        
        return self.row
