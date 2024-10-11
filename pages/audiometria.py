import flet as ft

class Audiometria():
    def __init__(self) -> None:
        self.numImg = 0
        self.images = ["./assets/hora.png", "./assets/lugar_silencioso.png", "./assets/uso_audifonos.png"]
        self.fre = ['./assets/8000.wav','./assets/9000.wav','./assets/10000.wav','./assets/11000.wav','./assets/12000.wav','./assets/13000.wav','./assets/14000.wav','./assets/15000.wav','./assets/16000.wav','./assets/17000.wav','./assets/18000.wav','./assets/19000.wav','./assets/20000.wav']
        vol=[i/10 for i in range(1,11,1)]
    def test_audiometria(self,page:ft.Page):
        pass
        
        
        
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
