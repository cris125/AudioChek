import flet as ft

def main(page: ft.Page):
    audio1 = ft.Audio(
        src="output_stereo.wav", autoplay=True, balance=1
    )
    page.overlay.append(audio1)

    def next_test(e):
        e.control.disabled = True  # Deshabilitar el botón después de hacer clic
        page.update()  # Actualizar la página para reflejar el cambio

    page.add(
        ft.ElevatedButton(text="Presionar una vez", on_click=lambda e: next_test(e))
    )

ft.app(main)
