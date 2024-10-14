import flet as ft

url = "https://github.com/mdn/webaudio-examples/blob/main/audio-analyser/viper.mp3?raw=true"

def main(page: ft.Page):
    TXT=ft.TextField(value="")
    audio1 = ft.Audio(
        src=url,
        autoplay=False,
        volume=1,
        balance=0,
        on_loaded=lambda _: print("Loaded"),
        on_duration_changed=lambda e: print("Duration changed:", e.data),
        on_position_changed=lambda e: print("Position changed:", e.data),
        on_state_changed=lambda e: print("State changed:", e.data),
        on_seek_complete=lambda _: print("Seek complete"),
    )
    page.overlay.append(audio1)
    page.add(
        ft.ElevatedButton("Play", on_click=lambda _: audio1.play()),
        ft.ElevatedButton("Pause", on_click=lambda _: audio1.pause()),
        ft.ElevatedButton("Resume", on_click=lambda _: audio1.resume()),
        ft.ElevatedButton("Release", on_click=realise),
        ft.ElevatedButton("Seek 2s", on_click=lambda _: audio1.seek(2000)),
    )

ft.app(main)