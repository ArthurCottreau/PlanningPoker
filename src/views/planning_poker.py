import flet as ft

def main(page: ft.Page):
    # Configurer les propriétés de base de la page
    page.title = "Planning Poker (Scrum Poker)"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    
    # Suite de Fibonacci et options spéciales
    poker_values = ["0", "1", "2", "3", "5", "8", "13", "21", "34", "55", "89", "☕"]

    # Texte pour afficher le résultat sélectionné
    result_text = ft.Text(
        value="Veuillez choisir une estimation", # Veuillez choisir une estimation
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_GREY_900
    )

    # Variable pour suivre la carte actuellement sélectionnée
    current_selection = None

    def card_clicked(e):
        nonlocal current_selection
        clicked_container = e.control
        
        # 1. Réinitialiser le style de la carte précédente (si elle existe)
        if current_selection:
            current_selection.bgcolor = ft.Colors.WHITE
            current_selection.border = ft.border.all(2, ft.Colors.BLUE_200)
            current_selection.scale = 1.0
            current_selection.update()

        # 2. Définir le style de la carte cliquée (mise en évidence)
        clicked_container.bgcolor = ft.Colors.BLUE_50
        clicked_container.border = ft.border.all(3, ft.Colors.BLUE_700)
        clicked_container.scale = 1.1 # Léger agrandissement lors du clic
        clicked_container.update()

        # 3. Mettre à jour l'état global et le texte
        current_selection = clicked_container
        result_text.value = f"Points d'estimation : {clicked_container.data}"
        page.update()

    # Construire la liste des cartes
    cards = []
    for value in poker_values:
        # Utiliser un Container pour simuler une carte de poker
        card = ft.Container(
            content=ft.Text(
                value=value, 
                size=24, 
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK87
            ),
            data=value,  # Stocker la valeur représentée par la carte
            width=80,    # Largeur de la carte
            height=120,  # Hauteur de la carte
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.all(2, ft.Colors.BLUE_200),
            border_radius=ft.border_radius.all(10),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=5,
                color=ft.Colors.BLUE_GREY_100,
                offset=ft.Offset(0, 2),
            ),
            # Configuration de l'animation
            animate_scale=ft.Animation(300, ft.AnimationCurve.BOUNCE_OUT),
            animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
            # Événement de clic
            on_click=card_clicked,
            # Le curseur devient une main au survol
            ink=True,
        )
        cards.append(card)

    # Utiliser Row pour un alignement horizontal
    cards_row = ft.Row(
        controls=cards,
        wrap=False, # False signifie pas de retour à la ligne, garde une seule ligne
        scroll=ft.ScrollMode.AUTO, # Permet le défilement horizontal
        spacing=20, # Espacement entre les cartes
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Conteneur avec barre de défilement (ajout de remplissage pour l'esthétique)
    layout_container = ft.Container(
        content=cards_row,
        padding=ft.padding.symmetric(vertical=20),
    )

    # Ajouter les composants à la page
    page.add(
        ft.Column(
            controls=[
                result_text,
                ft.Divider(height=50, color=ft.Colors.TRANSPARENT), # Espace vide
                layout_container
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
