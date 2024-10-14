import flet as ft
import time
def main(page: ft.Page):
    dlg = ft.AlertDialog(
            content=ft.Container(content=ft.Row([ft.Text("Cargando..."),ft.ProgressRing()],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)),
            modal=True,  # Evita que el usuario lo cierre al hacer clic fuera
        )
    def test(e):
        show_dialog()
        time.sleep(2)
        page.dialog.open = False
        page.update()
    def show_dialog():
        page.dialog = dlg
        page.dialog.open = True
        page.update()

    page.add(
        ft.ElevatedButton("Mostrar diálogo", on_click=test)
    )

ft.app(target=main)