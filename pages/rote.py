import flet as ft
from .start import Start
from .window import LayoutManager
from .navegation import Navegation
class Rote():
    def main(self,page:ft.Page):
        page.title = "AducioChek"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.window.width=400
        page.theme_mode = ft.ThemeMode.LIGHT
        self.page=page
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.page.go(page.route)

        
    def route_change(self,route):
        self.page.views.clear()
        a=Navegation()
        h=Start()
        
        b=LayoutManager(h.start(self.page),a.navegation(self.page))
        self.page.views.append(
            ft.View(
                "/",
                [
                   b.build_layout()
                ],
            )
        )
        
        if self.page.route == "/ins":
            self.page.views.append(
                ft.View(
                    "/ins",
                    [
                        b.build_layout()
                    ],
                )
            )
        elif self.page.route == "/test":
            self.page.views.append(
                ft.View(
                    "/test",
                    [
                        b.build_layout()
                    ],
                )
            )
        elif self.page.route == "/res":
            self.page.views.append(
                ft.View(
                    "/res",
                    [
                        b.build_layout()
                    ],
                )
            )

        elif self.page.route == "/res":
            self.page.views.append(
                ft.View(
                    "/per",
                    [
                        b.build_layout()
                    ],
                )
            )    
        self.page.update()

    def view_pop(self,view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)

    


