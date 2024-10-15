import flet as ft 

class Instructions():
    def __init__(self):
        self.images=["./assets/1.png","./assets/2.png","./assets/3.png"]
        self.numImg=0
    def next(self, e):
        if self.numImg == 0:
            e.control.text="Siguente" 
        if self.numImg < len(self.images) - 1 and e.control.text !="Atras":
            self.numImg += 1
        else:
            e.control.text="Atras"
            self.numImg -= 1
            
          
        self.image.src = self.images[self.numImg]
        self.page.update()
        
    def instructions(self, page: ft.Page):
        self.page = page
        
        # Crear la imagen que se va a actualizar
        self.image = ft.Image(
            src=self.images[self.numImg],
            width=page.width-100,

            fit=ft.ImageFit.CONTAIN,
        )
        
        # Crear el botón que llama a la función next
        btn_next = ft.ElevatedButton(text="Siguente", icon=ft.icons.NAVIGATE_NEXT, on_click=self.next)
        
        # Crear la fila con los controles
        self.row = ft.Row([
            ft.Column([
                
                ft.Row([self.image]),  # Usar la imagen creada
                # Poner el botón al final del ancho disponible
                ft.Row([btn_next], alignment=ft.MainAxisAlignment.END) 
            ])
        ], alignment=ft.MainAxisAlignment.CENTER)  # Centrar la columna en la pantalla
        
        return self.row
