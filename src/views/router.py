import flet as ft

from views.login_page import PageLogin
from views.game_page import PageGame
from views.page1 import Page1

class Router:
    def __init__(self, page):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": PageLogin(page),
            "/game": PageGame(page),
            "/page1": Page1(page)
        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()
