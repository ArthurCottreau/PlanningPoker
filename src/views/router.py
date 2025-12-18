import flet as ft

from views.login_page import PageLogin
from views.game_page import PageGame
from views.task_page import PageTask

class Router:
    """
    @author COTTREAU Arthur
    @class Router
    @brief Gestion des chemins des pages de l'application
    """
    def __init__(self, page):
        """
        @brief Constructeur de la classe
        @param page: Conteneur pour les Views
        """
        self.page = page
        self.ft = ft
        self.routes = {
            "/": PageLogin(page),
            "/game": PageGame(page),
            "/task": PageTask(page)
        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self, route):
        """
        @brief Méthode qui modifie le chemin utilisé pour ouvrir une autre page
        @param route: Nouveau chemin
        """
        self.body.content = self.routes[route.route]
        self.body.update()
