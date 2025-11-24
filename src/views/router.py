import flet as ft

from views.def_page import defPage
from views.page1 import Page1
from views.page2 import Page2

class Router:
    def __init__(self, page):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": defPage(page),
            "/page1": Page1(page),
            "/page2": Page2(page)
        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()
