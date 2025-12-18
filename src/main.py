import flet as ft

from views.router import Router

"""
@file
@author COTTREAU Arthur
"""

def main(page: ft.Page):
    """
    @brief Fonction principale de l'application
    @param page: Page de l'application
    """
    page.title = "Planning Poker"

    myRouter = Router(page)

    page.on_route_change = myRouter.route_change

    page.add(
        myRouter.body
    )

ft.app(main)
