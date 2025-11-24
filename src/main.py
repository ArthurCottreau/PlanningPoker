import flet as ft

from views.router import Router

def main(page: ft.Page):
    page.title = "Planning Poker"

    myRouter = Router(page)

    page.on_route_change = myRouter.route_change

    page.add(
        myRouter.body
    )

ft.app(main)
