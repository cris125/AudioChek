import flet as ft

class Start():
    def on_cl(self,e):
        self.txt.value=self.txt_file.value
        self.page.client_storage.set("name",self.txt_file.value)
        self.page.update()
        
    def start(self,page:ft.Page):
        self.page=page
        self.txt=ft.Text(value="")
        self.txt_file=ft.TextField(value="")
        btn=ft.ElevatedButton(text="sumit",on_click=self.on_cl)
        
        if page.client_storage.contains_key("name"):
            self.txt.value = page.client_storage.get("name")
        else:
            self.txt.value = "nada pa"
            
        return(
            ft.Row([
                self.txt_file,
                self.txt,
                btn
            ])
        )