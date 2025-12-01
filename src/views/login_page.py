import flet as ft

def PageLogin(page):

    def next_click(e):
        page.go('/page1')

    page.bgcolor = ft.Colors.GREY

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
                        ft.Text(
                            value="Votre Nom",
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.TextField(
                            label="ex: Thomas, Julie...",
                            expand=1
                        ),
                        ft.Text(
                            value="ID de la partie",
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.TextField(
                            label="ex: Equipe-Alpha",
                            expand=1
                        ),
                        ft.Text(
                            value="Creer une nouvelle partie",
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.TextField(expand=1),
                        ft.Checkbox(
                            label="Mode de jeu Strict",
                            label_position=ft.LabelPosition.RIGHT,
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
                            on_click=next_click,
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
                            on_click=next_click,
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
