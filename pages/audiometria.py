import flet as ft

class Audiometria():
    def audiometria(self,page:ft.Page):
        
        img_hora = ft.Image(
            src=f"./assets/hora.png",
            width=page.width-50,
            fit=ft.ImageFit.CONTAIN,
        )
        img_lugar_silencioso = ft.Image(
            src=f"./assets/lugar_silencioso.png",
            width=page.width-50,
            fit=ft.ImageFit.CONTAIN,
        )
        img_uso_audifonos = ft.Image(
            src=f"./assets/uso_audifonos.png",
            width=page.width-50,
            fit=ft.ImageFit.CONTAIN,
        )
        images = ft.Row([img_hora,img_lugar_silencioso,img_uso_audifonos],
            expand=1, wrap=False, scroll="always")
        
        return(images)