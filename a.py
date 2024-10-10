import datetime
import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.client_storage.clear()
    name=page.client_storage.get("name")
    print(name)

    def xd(e):
        a.con
    a=ft.Column([ft.Text("xd")])
    page.add()


ft.app(main)
