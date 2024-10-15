import flet as ft
from .start import Start
from .window import LayoutManager
from .navegation import Navegation
from .profile import Profile
from .instructions import Instructions
from .audiometria import Audiometria
from .results import Results
class Rote:
    def main(self, page: ft.Page):
        
        page.title = "AudioCheck"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.window.width = 400
        page.theme_mode = ft.ThemeMode.LIGHT
        self.page = page
        self.progress=ft.AlertDialog(
            content=ft.Container(content=ft.Row([ft.Text("Cargando..."),ft.ProgressRing()],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)),
            modal=True,  # Evita que el usuario lo cierre al hacer clic fuera
        )
        self.page.dialog=self.progress
        self.page.on_route_change = self.route_change
        ##self.page.client_storage.clear()
        # Verificar si ya hay un nombre guardado y redirigir según sea necesario
        if self.page.client_storage.contains_key("id"):
            # Redirigir directamente al perfil si ya existe el nombre
            self.page.go("/per")
        else:
            # Redirigir a la pantalla de inicio para registrar el nombre
            self.page.go("/sta")

    def route_change(self, route):
        # Limpiar las vistas antes de agregar las nuevas
        self.page.views.clear()

        # Instanciar las clases necesarias
        nav = Navegation()
        # Ruta para la pantalla de inicio (solo si el nombre no está guardado)
        
        if self.page.route == "/sta":
            st=Start()
            self.page.views.clear()
            self.page.views.append(
                ft.View(
                    "/sta",
                    [st.start(self.page)],
                )
            )
        # Ruta para el perfil (si el nombre está guardado)
        elif self.page.route == "/per":
            prof = Profile()
            profile_nav = LayoutManager(prof.profile(self.page), nav.navegation(self.page))
            self.page.views.clear()
            self.page.views.append(
                ft.View(
                    "/per",
                    [profile_nav.build_layout()],
                )
            )
        # Otras rutas como instrucciones, test y resultados, accesibles después de iniciar
        elif self.page.route == "/ins":
            ins=Instructions()
            ins_nav = LayoutManager(ins.instructions(self.page), nav.navegation(self.page))
            self.page.views.clear()
            self.page.views.append(
                ft.View(
                    "/ins",
                    [ins_nav.build_layout()],
                )
            )
        
            
        elif self.page.route == "/test/audiometria":
            aud=Audiometria()
            ins_nav = LayoutManager(aud.test_audiometria(self.page), nav.navegation(self.page))
            self.page.views.clear()
            self.page.views.append(
                ft.View(
                    "/test/audiometria",
                    [ ins_nav.build_layout()],
                )
            )
            
        elif self.page.route== "/test":
            aud_ins=Audiometria()
            ins_nav = LayoutManager(aud_ins.audiometria_ins(self.page), nav.navegation(self.page))
            self.page.views.clear()
            self.page.views.append(
                ft.View(
                    "/test",
                    [ins_nav.build_layout()],
                )
            )
        elif self.page.route == "/res":
            res=Results()
            ins_nav = LayoutManager(res.results(self.page), nav.navegation(self.page))
            self.page.views.clear()
            self.page.views.append(
                ft.View(
                    "/res",
                    [ins_nav.build_layout()],
                )
            )
        else:
            # En caso de una ruta inválida, redirigir a la pantalla de inicio
            self.page.go("/sta")

        # Actualizar la página para reflejar los cambios
        self.page.update()



