import flet as ft

from misc.save_data import SaveData

def PageLogin(page):
    """
    @author COTTREAU Arthur
    @brief Page menu
    @param page: Page de l'application
    @var content: Contenu de la page de connexion et création d'interface
    """

    def create_game(e):
        """
        @brief Création d'une nouvelle partie et ouverture de la page "task"
        """
        page.go('/task')

    def load_game(e: ft.FilePickerResultEvent):
        """
        @brief Chargement d'une partie existante
        @param e: Fichier JSON de sauvegarde a charger
        """
        file = e.files[0]

        mySD = SaveData()
        mySD.reset()
        mySD.load_json(file.path)

        if mySD.get_element("users"):
            if mySD.get_element("tasks"):
                page.go('/game')
            else:
                 print("Cette sauvegarde n'a pas de taches...")
        else:
            print("Cette sauvegarde n'a pas d'utilisateurs..")

    page.bgcolor = ft.Colors.GREY

    file_picker_load = ft.FilePicker(on_result=load_game)
    page.overlay.append(file_picker_load)

    content = ft.Row(
        [
            ft.Container(
                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text(value="Planning Poker", 
                                theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                                color=ft.Colors.INDIGO,
                                weight=ft.FontWeight.W_900)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [ft.Text(value="Conception Agile")],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.CupertinoButton(
                            content=ft.Row(
                                [
                                    ft.Icon(
                                        name=ft.Icons.PLAY_ARROW_OUTLINED,
                                        color=ft.Colors.WHITE
                                    ),
                                    ft.Text(
                                        value="Creer Partie",
                                        color=ft.Colors.WHITE
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            bgcolor=ft.Colors.INDIGO,
                            opacity_on_click=0.3,
                            on_click=create_game,
                            width=page.width
                        ),
                        ft.CupertinoButton(
                            content=ft.Row(
                                [
                                    ft.Icon(
                                        name=ft.Icons.PEOPLE_OUTLINED,
                                        color=ft.Colors.WHITE
                                    ),
                                    ft.Text(
                                        value="Rejoindre Partie",
                                        color=ft.Colors.WHITE
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            bgcolor=ft.Colors.GREEN_700,
                            opacity_on_click=0.3,
                            on_click=lambda _: file_picker_load.pick_files(
                                allow_multiple=False,
                                allowed_extensions=["json"]
                            ),
                            width=page.width
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                bgcolor=ft.Colors.WHITE,
                width=500,
                height=580,
                border_radius=10,
                padding = 35
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    return content
