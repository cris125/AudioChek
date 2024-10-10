import flet as ft
from pages import Rote

def main():
    rote=Rote()
    ft.app(rote.main ,view=ft.AppView.WEB_BROWSER)
main()
    